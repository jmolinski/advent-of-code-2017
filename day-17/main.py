step = int(open('data.txt', 'r').read())


def track(n, rounds=1):
    lst, pos = [0, 1], 1
    for i in range(2, rounds):
        pos = (pos + step + 1) % (i)
        lst.insert(pos, i)

    return lst[(lst.index(n) + 1) % len(lst)]


def track_after_zero(rounds=1):
    pos, zero_pos, after_zero = 1, 0, 0
    for i in range(2, rounds):
        pos = (pos + step + 1) % (i)
        if pos == zero_pos + 1:
            after_zero = i
        zero_pos += (zero_pos >= pos)
    return after_zero


answer_part_1 = track(2017, 2018)
answer_part_2 = track_after_zero(50 * 1000 * 1000)

print(answer_part_1, answer_part_2)
