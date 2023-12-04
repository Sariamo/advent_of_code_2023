import utils

m = utils.get_input_as_matrix()
sum = 0
i = 0

while i < len(m):
    j = 0
    while j < len(m[i]):

        if str(m[i][j]).isnumeric():
            num_ends = False
            num_counts = False
            num = ""

            while not num_ends:

                num += str(m[i][j])
                if not num_counts:

                    for i2 in range(i - 1, i + 2):
                        for j2 in range(j - 1, j + 2):

                            if (i == i2 and j == j2) or not 0 <= i2 < len(m) or not 0 <= j2 < len(m[i]):
                                continue

                            neighbor = str(m[i2][j2])

                            if (not neighbor.isnumeric()) and (not neighbor == "."):
                                num_counts = True

                if j < len(m[i]) - 1 and str(m[i][j+1]).isnumeric():
                    j += 1

                else:
                    sum += int(num) if num != "" and num_counts else 0
                    num_ends = True

        j += 1
    i += 1

print(sum)
