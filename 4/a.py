import utils

inp = utils.get_input()
sum = 0
for card in inp:
    winning_nums = card.split(": ")[1].strip().split(" | ")[0].replace("  ", " ").strip().split(" ")
    own_nums = card.split(": ")[1].strip().split(" | ")[1].replace("  ", " ").strip().split(" ")
    multiply_ctr = 0
    for num in own_nums:
        if num in winning_nums:
            multiply_ctr += 1
    sum += 0 if multiply_ctr == 0 else 2**(multiply_ctr - 1)
print(sum)
