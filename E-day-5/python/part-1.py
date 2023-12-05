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


def process_text_map(previous_step, text_map):
    map_object = ResourceMap(text_map)
    return [map_object.map_val(resource) for resource in previous_step]


if __name__ == '__main__':
    with open("../input.txt", "r") as input_file:
        seeds, seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location = input_file.read().split(
            "\n\n")

    seeds = [int(seed) for seed in seeds.split(":")[-1].strip().split(" ")]

    soils = process_text_map(seeds, seed_soil)
    fertilizers = process_text_map(soils, soil_fertilizer)
    water = process_text_map(fertilizers, fertilizer_water)
    light = process_text_map(water, water_light)
    temperature = process_text_map(light, light_temperature)
    humidity = process_text_map(temperature, temperature_humidity)
    location = process_text_map(humidity, humidity_location)

    print(f"The lowest location number that corresponds to the initial seeds is: {min(location)}")
