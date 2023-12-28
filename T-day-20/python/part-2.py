import collections
import numpy as np


LOW_PULSE = False
HIGH_PULSE = True

OFF_STATE = False
ON_STATE = True


class System:
    def __init__(self, input_path):
        self.adjacency_list = dict()
        self.flip_flop = dict()

        conjunctions = set()
        with open(input_path, 'r') as input_file:
            for line in input_file:
                node_name, pulses = line.strip().split(" -> ")
                node_name_pure = node_name.replace("%", "").replace("&", "")
                self.adjacency_list[node_name_pure] = [pulse.strip() for pulse in pulses.split(",")]

                if node_name[0] == "%":
                    self.flip_flop[node_name_pure] = OFF_STATE

                elif node_name[0] == "&":
                    conjunctions.add(node_name_pure)

        self.conjunction_states = collections.defaultdict(dict)
        for node in self.adjacency_list:
            for adj in self.adjacency_list[node]:
                if adj in conjunctions:
                    self.conjunction_states[adj][node] = LOW_PULSE

        self.queue = collections.deque()

    def press_button(self):
        self.queue.append((None, "broadcaster", LOW_PULSE))

    def send_to_adjacent(self, module_name, pulse):
        for adj in self.adjacency_list[module_name]:
            self.queue.append((module_name, adj, pulse))

    def do_flip_flop(self, module_name, pulse):
        if pulse == HIGH_PULSE:
            return

        self.flip_flop[module_name] = not self.flip_flop[module_name]
        self.send_to_adjacent(module_name, HIGH_PULSE if self.flip_flop[module_name] == ON_STATE else LOW_PULSE)

    def do_conjunction(self, pulse_from, pulse_to, pulse):
        self.conjunction_states[pulse_to][pulse_from] = pulse
        all_high = all(
            self.conjunction_states[pulse_to][adj] == HIGH_PULSE
            for adj in self.conjunction_states[pulse_to]
        )

        self.send_to_adjacent(pulse_to, LOW_PULSE if all_high else HIGH_PULSE)

    def process_queue(self):
        process_completions = []
        while self.queue:
            pulse_from, pulse_to, pulse = self.queue.popleft()

            if pulse_to in self.flip_flop:
                self.do_flip_flop(pulse_to, pulse)

            elif pulse_to in self.conjunction_states:
                self.do_conjunction(pulse_from, pulse_to, pulse)

                if pulse_to in ("hn", "mp", "xf", "fz") and pulse == LOW_PULSE:
                    process_completions.append(pulse_to)

            elif pulse_to == "broadcaster":
                self.send_to_adjacent("broadcaster", pulse)

        return process_completions


if __name__ == '__main__':
    system = System("../input.txt")

    scan_length = 1000000000000000
    cycle_completions = collections.defaultdict(lambda: float('inf'))

    for num_presses in range(scan_length):
        system.press_button()
        for completed in system.process_queue():
            cycle_completions[completed] = min(cycle_completions[completed], num_presses + 1)

        if len(cycle_completions) == 4:
            break

    fewest_presses = np.lcm.reduce(list(cycle_completions.values()))
    print(f"The fewest button presses required for a low pulse in 'rx' is: {fewest_presses}")
