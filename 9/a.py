import utils

inp = utils.get_input()
sum = 0
for seq in inp:

    seq_els = [int(val.strip()) for val in seq.split(" ")]
    diff_history = [seq_els]
    while not all([d == 0 for d in seq_els]):
        diffs = []
        for i in range(1, len(seq_els)):
            diffs.append(seq_els[i] - seq_els[i - 1])
        seq_els = diffs
        if all([d == 0 for d in seq_els]):
            seq_els.append(0)
        diff_history.append(seq_els)

    diff_history.reverse()
    for j in range(1, len(diff_history)):
        diff_history[j].append(diff_history[j][-1] + diff_history[j - 1][-1])
    sum += diff_history[-1][-1]

print(sum)