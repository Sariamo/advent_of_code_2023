import utils

inp = utils.get_input()

time = int(inp[0].replace("Time:", "").replace(" ", ""))
distance_to_beat = int(inp[1].replace("Distance:", "").replace(" ", ""))
win_pos_ctr = 0

for hold_the_button in range(time):
    distance = hold_the_button * (time - hold_the_button)
    if distance > distance_to_beat:
        win_pos_ctr += 1

print(win_pos_ctr)
