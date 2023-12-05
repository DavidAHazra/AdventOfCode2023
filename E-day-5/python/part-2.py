class ResourceMap:
    def __init__(self, text_map):
        self.destination_ranges = []
        self.source_ranges = []

        for line in text_map.split("\n")[1:]:
            destination_start, source_start, length = (int(num) for num in line.split(" "))
            self.destination_ranges.append((destination_start, destination_start + length - 1))
            self.source_ranges.append((source_start, source_start + length - 1))

    def map_val(self, key):
        for source_index, (source_start, source_end) in enumerate(self.source_ranges):
            if source_start <= key <= source_end:
                return self.destination_ranges[source_index][0] + key - source_start

        return key

    def map_range(self, key_range):
        # If ranges overlap then extract the overlaps
        output = []
        overlaps = []
        for source in self.source_ranges:
            if key_range[0] <= source[1] and key_range[1] >= source[0]:
                overlap = (max(key_range[0], source[0]), min(key_range[1], source[1]))
                overlaps.append(overlap)

                mapped_start = self.map_val(overlap[0])
                mapped_end = overlap[1] - overlap[0] + mapped_start
                output.append((mapped_start, mapped_end))

        # Subtract the ranges from key_range to find the ranges that have no mapping
        no_mapping_intervals = []
        key_start, key_end = key_range
        for start, end in overlaps:
            if start > key_end:
                # Done - we've passed the end of the
                break

            if end < key_start:
                # We've not reached the interval yet
                continue

            if start > key_start:
                no_mapping_intervals.append((key_start, start - 1))

            key_start = max(end + 1, key_start)

        if key_start <= key_end:
            no_mapping_intervals.append((key_start, key_end))

        output.extend(no_mapping_intervals)
        return output


def process_text_map(previous_step, text_map):
    map_object = ResourceMap(text_map)
    new_ranges = []
    for previous_range in previous_step:
        new_ranges.extend(map_object.map_range(previous_range))

    return new_ranges


if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        seed_line, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location = input_file.read().split("\n\n")

    seed_line = [int(seed) for seed in seed_line.split(":")[-1].strip().split(" ")]

    seed_ranges = []
    for i in range(0, len(seed_line), 2):
        start, length = seed_line[i], seed_line[i + 1]
        seed_ranges.append((start, start+length))

    soils = process_text_map(seed_ranges, seed_soil)
    fertilizers = process_text_map(soils, soil_fertilizer)
    water = process_text_map(fertilizers, fertilizer_water)
    light = process_text_map(water, water_light)
    temperature = process_text_map(light, light_temperature)
    humidity = process_text_map(temperature, temperature_humidity)
    location = process_text_map(humidity, humidity_location)

    lowest_location = min(location, key=lambda x: x[0])[0]
    print(f"The lowest location number that corresponds to the initial seeds is: {lowest_location}")


