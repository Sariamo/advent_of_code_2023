import math
import utils


def finished(current_ways):
    return all([cw.endswith("Z") for cw in current_ways])


inp = utils.get_input()
instr = inp[0]
ways_with_lr = [i.replace("= (", "").replace(",", "").replace(")", "").split(" ") for i in inp if "=" in i]
ways = [way[0] for way in ways_with_lr]
current_ways = []
way_indices = []

for way in ways:
    if way.endswith("A"):
        current_ways.append(way)
        way_indices.append(ways.index(way))
step_ctr = 0
first_on_z_field = [None for _ in range(len(current_ways))]

while not finished(current_ways):
    for ins in instr:
        step_ctr += 1
        for j, way in enumerate(current_ways):
            if ins == "L":
                current_ways[j] = ways_with_lr[way_indices[j]][1]
            else:
                current_ways[j] = ways_with_lr[way_indices[j]][2]
            way_indices[j] = ways.index(current_ways[j])

            if current_ways[j].endswith("Z") and first_on_z_field[j] is None:
                if first_on_z_field[j] is None:
                    first_on_z_field[j] = step_ctr
            if first_on_z_field.count(None) == 0:
                print(math.lcm(*first_on_z_field))
                exit()
