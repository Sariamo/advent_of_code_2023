import utils

inp = utils.get_input()
copies = [1 for _ in range(len(inp))]
for index, card in enumerate(inp):

    winning_nums = card.split(": ")[1].strip().split(" | ")[0].replace("  ", " ").strip().split(" ")
    own_nums = card.split(": ")[1].strip().split(" | ")[1].replace("  ", " ").strip().split(" ")

    for copy in range(copies[index]):
        copy_ctr = 0
        for num in own_nums:
            if num in winning_nums:
                copy_ctr += 1
        for i in range(1, copy_ctr + 1):
            if i + index < len(copies):
                copies[i + index] += 1
print(sum(copies))
