l = []
with open("input") as i:
    for inp in i.readlines():
        l.append(inp)

nums = []
nums_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for ls in l:
    num = ""
    word = ""
    for lss in ls:
        if lss.isnumeric():
            num += lss
            word = ""
        else:
            word += lss
            for nw in nums_words:
                if word.endswith(nw):
                    num += str(numbers[nums_words.index(nw)])

    num = int(num[0]+num[-1])
    nums.append(num)

print(sum(nums))
