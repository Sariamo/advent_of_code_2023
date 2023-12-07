import utils


def get_max_num_of_same_card(card):
    return max([[c for c in card].count(v) for v in set(card)])


def compare(a, b):
    if get_max_num_of_same_card(a) == get_max_num_of_same_card(b):
        if len(set(a)) == len(set(b)):
            order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
            for i in range((len(a))):
                if order.index(a[i]) == order.index(b[i]):
                    continue
                else:
                    return order.index(a[i]) < order.index(b[i])
        else:
            return len(set(a)) < len(set(b))
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

print(sum([(i + 1) * int(card[1]) for i, card in enumerate(hands_and_bids)]))
