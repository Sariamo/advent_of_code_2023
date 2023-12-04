import utils

m = utils.get_input_as_matrix()
sum = 0
i = 0
while i < len(m):
    j = 0
    while j < len(m[i]):

        token = m[i][j]

        if token == "*":
            num_ctr = 0
            nums = []
            for i2 in range(i - 1, i + 2):
                in_num = False
                for j2 in range(j - 1, j + 2):
                    if m[i2][j2].isnumeric():
                        if not in_num:
                            num = ""
                            num_ctr += 1
                            in_num = True
                            sel_token = j2
                            while sel_token > 0 and m[i2][sel_token - 1].isnumeric():
                                sel_token -= 1
                            while sel_token < len(m[i2]) and m[i2][sel_token].isnumeric():
                                num += m[i2][sel_token]
                                sel_token += 1
                            nums.append(num)
                    else:
                        in_num = False

            if num_ctr == 2:
                sum += int(nums[0])*int(nums[1])

        j += 1
    i += 1

print(sum)
