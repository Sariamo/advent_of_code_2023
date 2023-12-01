l = []
with open("input") as i:
    for inp in i.readlines():
        l.append(inp)

nums = []
for ls in l:
    num = ""
    for lss in ls:
        if lss.isnumeric():
            num += lss

    num = int(num[0]+num[-1])
    nums.append(num)

print(sum(nums))
