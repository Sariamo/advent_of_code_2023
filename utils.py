def get_input():
    l = []
    with open("input") as i:
        for inp in i.readlines():
            l.append(str(inp))
    return l


def get_input_as_matrix():
    inp = get_input()
    inp_matrix = []
    for row in inp:
        inp_row = []
        for column in row:
            if column == "\n":
                break
            else:
                inp_row.append(str(column).replace("\n", ""))
        inp_matrix.append(inp_row)
    return inp_matrix
