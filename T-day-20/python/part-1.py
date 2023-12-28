import collections


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

        self.queue = []

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
        num_low, num_high = 0, 0

        while self.queue:
            pulse_from, pulse_to, pulse = self.queue.pop(0)

            if pulse == LOW_PULSE:
                num_low += 1

            else:
                num_high += 1

            if pulse_to in self.flip_flop:
                self.do_flip_flop(pulse_to, pulse)

            elif pulse_to in self.conjunction_states:
                self.do_conjunction(pulse_from, pulse_to, pulse)

            elif pulse_to == "broadcaster":
                self.send_to_adjacent("broadcaster", pulse)

        return num_low, num_high


if __name__ == '__main__':
    system = System("../input.txt")

    total_lows, total_highs = 0, 0

    for _ in range(1000):
        system.press_button()
        process_lows, process_highs = system.process_queue()
        total_lows += process_lows
        total_highs += process_highs

    print(f"The product of the number of high and low pulses is: {total_lows * total_highs}")
