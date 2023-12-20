import math
from collections import deque

def read_file_as_string(file_path: str):
    with open(file_path, 'r') as file:
        return file.read()


# broadcast -> Same pulse to all
# % flip-flop -> off by default ->
# receives sends state
#    1       -     -
#    0       1     if 0 then 1
#    0       0      if 1 then 0

# Conjunction % (remembers most recent pulse) defaults to low pulse
# remembers state of all connected modules
# update the pulse for all first then if all are high then send low else send high

class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}

    def __repr__(self):
        return self.name + " { type=" + self.type + ", outputs=" + ", ".join(self.outputs) + ", memory=" + str(self.memory)


def part_1():
    inputs = read_file_as_string("../inputs/day_20.txt")
    config_lines = inputs.splitlines()
    modules = {}
    broadcast_targets = []
    for line in config_lines:
        module, module_list = line.split(" -> ")
        module_list = module_list.split(", ")
        if module == "broadcaster":
            broadcast_targets = module_list
        else:
            type = module[0]
            name = module[1:]
            modules[name] = Module(name, type, module_list)

    print(broadcast_targets)
    print(modules)

    for name, module in modules.items():
        for output in module.outputs:
            print(name, output)
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"
    print(modules)
    lo = hi = 0
    for _ in range(1000):
        lo += 1
        # origin, target, pulse
        q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
        while q:
            origin, target, pulse = q.popleft()
            if pulse == "lo":
                lo += 1
            else:
                hi += 1

            if target not in modules:
                continue
            module = modules[target]

            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
    print(lo * hi)


def part_2():
    inputs = read_file_as_string("../inputs/day_20.txt")
    config_lines = inputs.splitlines()
    modules = {}
    broadcast_targets = []
    for line in config_lines:
        module, module_list = line.split(" -> ")
        module_list = module_list.split(", ")
        if module == "broadcaster":
            broadcast_targets = module_list
        else:
            type = module[0]
            name = module[1:]
            modules[name] = Module(name, type, module_list)

    # print(broadcast_targets)
    # print(modules)

    for name, module in modules.items():
        for output in module.outputs:
            # print(name, output)
            if output in modules and modules[output].type == "&":
                modules[output].memory[name] = "lo"
    # print(modules)
    (feed, ) = [name for name, module in modules.items() if "rx" in module.outputs]

    cycle_lengths = {}
    seen = {name: 0 for name, module in modules.items() if feed in module.outputs}
    # print(cycle_lengths)
    # exit(0)
    presses = 0
    while True:
        presses += 1
        # origin, target, pulse
        q = deque([("broadcaster", x, "lo") for x in broadcast_targets])
        while q:
            origin, target, pulse = q.popleft()
            if target not in modules:
                continue
            module = modules[target]
            if module.name == feed and pulse == "hi":
                seen[origin] += 1

                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses
                else:
                    assert presses == seen[origin] * cycle_lengths[origin]

                if all(seen.values()):
                    print(cycle_lengths)
                    x = 1
                    for cycle_length in cycle_lengths.values():
                        x = math.lcm(x, cycle_length)
                    print(x)
                    exit(0)
            if module.type == "%":
                if pulse == "lo":
                    module.memory = "on" if module.memory == "off" else "off"
                    outgoing = "hi" if module.memory == "on" else "lo"
                    for x in module.outputs:
                        q.append((module.name, x, outgoing))
            else:
                module.memory[origin] = pulse
                outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))


if __name__ == "__main__":
    # part_1()
    part_2()
