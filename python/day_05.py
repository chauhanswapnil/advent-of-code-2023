def read_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.readlines()

def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()

def part_1():
    lines = read_file("../inputs/day_05.txt")
    seeds = lines[0].split(":")[1].strip().split()

    map_counter = -1
    seeds_conversion = {i: [] for i in seeds}
    array_of_maps = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    # print(seeds_conversion)
    for i in range(2, len(lines)):
        if "map" in lines[i]:
            map_counter += 1
            continue
        if lines[i].strip() != "":
            dest_range, source_range, range_start = lines[i].split()
            array_of_maps[map_counter].append((dest_range, source_range, range_start))

    for seed in seeds:
        current_seed = seed
        for i in range(0, 7):
            current_map = array_of_maps[i]
            appended = False
            for current in current_map:
                dest_range, source_range, range_start = current
                if int(source_range) <= int(current_seed) < int(source_range) + int(range_start):
                    appended = True
                    current_seed = int(current_seed) + (int(dest_range) - int(source_range))
                    break
            if not appended:
                current_seed = int(current_seed)
            seeds_conversion[seed].append(current_seed)

    locations = []
    for values in seeds_conversion.values():
        locations.append(values[-1])
    print(min(locations))


def process_seeds(seeds, ranges):
    if not seeds:
        return []

    start_seed, end_seed = seeds.pop()
    found = False
    seeds_traversed = []

    for dest_range, source_range, range_start in ranges:
        overlap_start = max(start_seed, source_range)
        overlap_end = min(end_seed, source_range + range_start)

        if overlap_start < overlap_end:
            seeds_traversed.append(
                (overlap_start - source_range + dest_range, overlap_end - source_range + dest_range)
            )
            if overlap_start > start_seed:
                seeds.append((start_seed, overlap_start))
            if end_seed > overlap_end:
                seeds.append((overlap_end, end_seed))
            found = True
            break

    if not found:
        seeds_traversed.append((start_seed, end_seed))

    # print(seeds_traversed)
    return seeds_traversed + process_seeds(seeds, ranges)


def part_2():
    # Reading it this way to get the maps while parsing the original input instead of getting the lines then
    # converting back
    seeds, *maps_block = read_file_as_string("../inputs/day_05.txt").split("\n\n")
    seeds_with_range = list(map(int, seeds.split(":")[1].split()))
    seeds = []

    # seeds are now tuple of start_seed to end_seed
    for i in range(0, len(seeds_with_range), 2):
        seeds.append((seeds_with_range[i], seeds_with_range[i] + seeds_with_range[i + 1]))

    for map_block in maps_block:
        ranges = []
        for line in map_block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        seeds = process_seeds(seeds, ranges)

    print(min(seeds))

    # Brute Force Approach Below. Doesn't Work
    # total_seeds = []
    # for i in range(0, len(seeds)):
    #     if i % 2 == 0:  # actual seed number
    #         total_seeds.append(int(seeds[i]))
    #     else:
    #         for j in range(int(seeds[i-1]) + 1, int(seeds[i-1])+int(seeds[i])):
    #             total_seeds.append(j)
    #
    # map_counter = -1
    # seeds_conversion = {i: [] for i in total_seeds}
    # array_of_maps = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    # # print(seeds_conversion)
    # for i in range(2, len(lines)):
    #     if "map" in lines[i]:
    #         map_counter += 1
    #         continue
    #     if lines[i].strip() != "":
    #         dest_range, source_range, range_start = lines[i].split()
    #         array_of_maps[map_counter].append((dest_range, source_range, range_start))
    #
    # for seed in total_seeds:
    #     current_seed = seed
    #     for i in range(0, 7):
    #         current_map = array_of_maps[i]
    #         print(current_map)
    #         for current in current_map:
    #             dest_range, source_range, range_start = current
    #             if int(source_range) <= int(current_seed) < int(source_range) + int(range_start):
    #                 current_seed = int(current_seed) + (int(dest_range) - int(source_range))
    #                 break
    #         current_seed = int(current_seed)
    #         seeds_conversion[seed].append(current_seed)
    #
    # locations = []
    # print(seeds_conversion)
    # for values in seeds_conversion.values():
    #     locations.append(values[-1])
    # print(min(locations))
    #

if __name__ == "__main__":
    part_1()
    part_2()
