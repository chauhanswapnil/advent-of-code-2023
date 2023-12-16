def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def hash(str):
    v = 0
    for ch in str:
        v += ord(ch)
        v *= 17
        v %= 256
    return v


def part_1():
    inputs = read_file_as_string("../inputs/day_15.txt")
    print(sum(map(hash, inputs.split(","))))


def part_2():
    inputs = read_file_as_string("../inputs/day_15.txt")
    boxes = [[] for _ in range(256)]
    focal_lengths = {}
    for instruction in inputs.split(","):
        if "-" in instruction:
            label = instruction[:-1]
            index = hash(label)
            if label in boxes[index]:
                boxes[index].remove(label)
        else:
            label, length = instruction.split("=")
            length = int(length)
            index = hash(label)
            if label not in boxes[index]:
                boxes[index].append(label)

            focal_lengths[label] = length
    # print(boxes)
    # print(focal_lengths)
    total = 0
    for box_num, box in enumerate(boxes, 1):
        for lens_slot, label in enumerate(box, 1):
            total += box_num * lens_slot * focal_lengths[label]
    print(total)


if __name__ == "__main__":
    part_1()
    part_2()
