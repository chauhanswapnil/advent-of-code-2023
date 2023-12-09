def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part_1():
    inputs = read_file_as_string("../inputs/day_09.txt")
    lines = inputs.split("\n")
    oasis_report = []
    for line in lines:
        oasis_report.append(list(map(int, line.split())))
    reading_tree = []
    for reading in oasis_report:
        current_reading = reading
        extrapolate = [current_reading]
        while current_reading != [0] * len(current_reading):
            temp = []
            for i in range(1, len(current_reading)):
                temp.append(current_reading[i] - current_reading[i-1])
            extrapolate.append(temp)
            current_reading = temp
        reading_tree.append(extrapolate)
    # print(reading_tree)

    answer = 0
    for i in range(0, len(reading_tree)):
        current_ans_tree = reading_tree[i]
        length_to_iterate = len(current_ans_tree) - 2
        prediction = 0
        while length_to_iterate != -1:
            # print(f"CAT = {current_ans_tree[length_to_iterate][-1]}")
            prediction += current_ans_tree[length_to_iterate][-1]
            length_to_iterate -= 1
        answer += prediction
        # print(prediction)

    print(f"Answer is {answer}")


def part_2():
    inputs = read_file_as_string("../inputs/day_09.txt")
    lines = inputs.split("\n")
    oasis_report = []
    for line in lines:
        oasis_report.append(list(map(int, line.split())))
    reading_tree = []
    for reading in oasis_report:
        current_reading = reading
        extrapolate = [current_reading]
        while current_reading != [0] * len(current_reading):
            temp = []
            for i in range(1, len(current_reading)):
                temp.append(current_reading[i] - current_reading[i-1])
            extrapolate.append(temp)
            current_reading = temp
        reading_tree.append(extrapolate)
    # print(reading_tree)

    answer = 0
    for i in range(0, len(reading_tree)):
        current_ans_tree = reading_tree[i]
        length_to_iterate = len(current_ans_tree) - 2
        next_prediction = 0
        while length_to_iterate != -1:
            # print(f"CAT = {current_ans_tree[length_to_iterate][0]}")
            next_prediction =  current_ans_tree[length_to_iterate][0] - next_prediction
            length_to_iterate -= 1
        answer += next_prediction
        # print(next_prediction)

    print(f"Answer is {answer}")


if __name__ == "__main__":
    part_2()
