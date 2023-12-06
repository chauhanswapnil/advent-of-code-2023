from functools import reduce


def read_file(file_path: str):
    with open(file_path, 'r') as file:
        return file.readlines()


def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part_1():
    inputs = read_file_as_string("../inputs/day_06.txt").split("\n")
    record_time = list(map(int, inputs[0].split(":")[1].split()))
    distances = list(map(int, inputs[1].split(":")[1].split()))

    # print(record_time)
    # print(distances)
    output = []
    for i in range(0, len(record_time)):
        to_beat_count = 0
        for j in range(1, record_time[i]):
            distance_travelled = j * (record_time[i] - j)
            if distance_travelled > distances[i]:
                to_beat_count += 1
        output.append(to_beat_count)
    print(reduce(lambda x, y: x*y, output))


def part_2():
    inputs = read_file_as_string("../inputs/day_06.txt").split("\n")
    record_time = int(inputs[0].split(":")[1].replace(" ", ""))
    distance = int(inputs[1].split(":")[1].replace(" ", ""))

    # print(record_time)
    # print(distance)
    to_beat_count = 0
    for j in range(1, record_time):
        distance_travelled = j * (record_time - j)
        if distance_travelled > distance:
            to_beat_count += 1
    print(to_beat_count)


if __name__ == "__main__":
    part_1()
    part_2()
