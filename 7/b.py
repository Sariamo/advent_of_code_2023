import utils


def get_max_num_of_same_card(card):
    return max([[c for c in card if c != "J"].count(v) for v in set(card)]) + card.count("J")


def get_len_set(card):
    return len(set(card)) if "J" not in card else max(1, len(set(card)) - 1)


def compare(a, b):
    if get_max_num_of_same_card(a) == get_max_num_of_same_card(b):
        if get_len_set(a) == get_len_set(b):
            order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
            for i in range((len(a))):
                if order.index(a[i]) == order.index(b[i]):
                    continue
                else:
                    return order.index(a[i]) < order.index(b[i])
        else:
            return get_len_set(a) < get_len_set(b)
    else:
        return get_max_num_of_same_card(a) > get_max_num_of_same_card(b)


inp = utils.get_input()
hands_and_bids = []

for i in inp:
    hands_and_bids.append(i.split(" "))

finished = False
while not finished:
    finished = True
    for i in range(len(hands_and_bids) - 1):
        a = hands_and_bids[i]
        b = hands_and_bids[i + 1]
        if compare(a[0], b[0]):
            hands_and_bids[i] = b
            hands_and_bids[i + 1] = a
            finished = False

print(hands_and_bids)
print(sum([(i + 1) * int(card[1]) for i, card in enumerate(hands_and_bids)]))
