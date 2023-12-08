import utils

inp = utils.get_input()
instr = inp[0]
ways_with_lr = [i.replace("= (", "").replace(",", "").replace(")", "").split(" ") for i in inp if "=" in i]
ways = [way[0] for way in ways_with_lr]
current_way = "AAA"
ways_index = ways.index("AAA")
step_ctr = 0

while current_way != "ZZZ":
    for ins in instr:
        print(current_way)
        if ins == "L":
            current_way = ways_with_lr[ways_index][1]
        else:
            current_way = ways_with_lr[ways_index][2]
        ways_index = ways.index(current_way)
        step_ctr += 1

print(step_ctr)
