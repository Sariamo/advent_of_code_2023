l = []
with open("input") as i:
    for inp in i.readlines():
        l.append(inp)

sum = 0
max_num = [12, 13, 14]
for i, game in enumerate(l):
    game_outcome = True
    draws = game.split(": ")[1].split("; ")
    for d in draws:
        if "red" in d:
            red = d.split(" red")[0].split(", ")[-1].replace(": ", "")
            if int(red) > max_num[0]:
                game_outcome = False
                break

        if "green" in d:
            green = d.split(" green")[0].split(", ")[-1].replace(": ", "")
            if int(green) > max_num[1]:
                game_outcome = False
                break

        if "blue" in d:
            blue = d.split(" blue")[0].split(", ")[-1].replace(": ", "")
            if int(blue) > max_num[2]:
                game_outcome = False
                break

    if game_outcome:
        sum += i + 1

print(sum)
