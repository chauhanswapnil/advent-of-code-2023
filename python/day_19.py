def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


def part_1():
    inputs = read_file_as_string("../inputs/day_19.txt")
    block1, block2 = inputs.split("\n\n")
    workflows = {}
    for line in block1.splitlines():
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    total = 0

    for line in block2.splitlines():
        item = {}
        for segment in line[1:-1].split(","):
            ch, n = segment.split("=")
            item[ch] = int(n)
        if accept(workflows, item):
            total += sum(item.values())
    print(total)


def accept(workflows, item, name="in"):
    if name == "R":
        return False
    if name == "A":
        return True
    rules, fallback = workflows[name]
    for key, cmp, n, target in rules:
        if eval(f"{item[key]} {cmp} {n}"):
            return accept(workflows, item, target)
    return accept(workflows, item, fallback)


def part_2():
    inputs = read_file_as_string("../inputs/day_19.txt")
    block1, _ = inputs.split("\n\n")
    workflows = {}
    for line in block1.splitlines():
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    print(count(workflows, {key: (1, 4000) for key in "xmas"}))


def count(workflows, ranges, name="in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for low, high in ranges.values():
            product *= high - low + 1
        return product

    rules, fallback = workflows[name]
    total = 0
    for key, cmp, n, target in rules:
        low, high = ranges[key]
        if cmp == "<":
            T = (low, min(n - 1, high))
            F = (max(n, low), high)
        else:
            T = (max(n + 1, low), high)
            F = (low, min(n, high))
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(workflows, copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(workflows, ranges, fallback)
    return total


if __name__ == "__main__":
    part_1()
    part_2()
