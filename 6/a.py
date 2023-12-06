import utils

inp = utils.get_input()

times = [int(t) for t in inp[0].replace("Time:", "").strip().replace("  ", " ").split(" ") if t != ""]
distances = [int(d) for d in inp[1].replace("Distance:", "").strip().replace("  ", " ").split(" ") if d != ""]

win_pos_ctr = 1

for race_num in range(len(times)):

    win_pos_ctr_per_race = 0
    time = times[race_num]
    distance_to_beat = distances[race_num]

    for hold_the_button in range(time):
        distance = hold_the_button * (time - hold_the_button)
        if distance > distance_to_beat:
            win_pos_ctr_per_race += 1

    win_pos_ctr *= win_pos_ctr_per_race

print(win_pos_ctr)
