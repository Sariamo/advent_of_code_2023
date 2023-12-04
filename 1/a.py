import utils

inp = utils.get_input()
nums = []
for ls in inp:
    num = ""
    for lss in ls:
        if lss.isnumeric():
            num += lss

    num = int(num[0]+num[-1])
    nums.append(num)

print(sum(nums))
