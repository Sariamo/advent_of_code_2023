import utils

inp = utils.get_input()

s = 0
for i, game in enumerate(inp):

    mins = [None, None, None]
    draws = game.split(": ")[1].split("; ")

    for d in draws:
        if "red" in d:
            red = d.split(" red")[0].split(", ")[-1].replace(": ", "")
            if mins[0] is None or int(red) > mins[0]:
                mins[0] = int(red)

        if "green" in d:
            green = d.split(" green")[0].split(", ")[-1].replace(": ", "")
            if mins[1] is None or int(green) > mins[1]:
                mins[1] = int(green)

        if "blue" in d:
            blue = d.split(" blue")[0].split(", ")[-1].replace(": ", "")
            if mins[2] is None or int(blue) > mins[2]:
                mins[2] = int(blue)

    s += mins[0] * mins[1] * mins[2]

print(s)
