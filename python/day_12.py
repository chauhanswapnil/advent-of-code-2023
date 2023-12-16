def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part1():
    inputs = read_file_as_string("../inputs/day_12.txt")
    # print(inputs)
    total = 0
    for line in inputs.splitlines():
        config, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        total += count1(config, nums)

    print(total)


def count1(config, nums):
    if config == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if "#" in config else 1
    result = 0

    if config[0] in ".?":
        result += count1(config[1:], nums)
    if config[0] in "#?":
        if nums[0] <= len(config) and "." not in config[:nums[0]] and (nums[0] == len(config) or config[nums[0]] != "#"):
            result += count1(config[nums[0] + 1:], nums[1:])

    return result


memo = {}


def part2():
    inputs = read_file_as_string("../inputs/day_12.txt")
    # print(inputs)
    total = 0
    for line in inputs.splitlines():
        config, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        config = "?".join([config] * 5)
        nums *= 5
        total += count2(config, nums)

    print(total)


def count2(config, nums):
    if config == "":
        return 1 if nums == () else 0
    if nums == ():
        return 0 if "#" in config else 1
    key = (config, nums)
    if key in memo:
        return memo[key]
    result = 0

    if config[0] in ".?":
        result += count2(config[1:], nums)
    if config[0] in "#?":
        if nums[0] <= len(config) and "." not in config[:nums[0]] and (nums[0] == len(config) or config[nums[0]] != "#"):
            result += count2(config[nums[0] + 1:], nums[1:])
    memo[key] = result
    return result


if __name__ == "__main__":
    # part1()
    part2()
