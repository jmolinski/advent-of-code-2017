from itertools import cycle, chain, islice
from collections import Counter

with open('data.txt', 'r') as f:
    banks = tuple(int(bank) for bank in f.readline().split())

cycles = []
while banks not in cycles:
    cycles.append(banks)

    max_index, max_value = max(enumerate(banks), key=lambda p: p[1])
    add_to_bank = Counter(
        islice(cycle(chain(range(max_index + 1, len(banks)), range(max_index + 1))),
               max_value)
    )
    banks = tuple(a + add_to_bank[i] for (i, a) in
                  enumerate(banks[:max_index] + (0,) + banks[max_index + 1:]))

answer_part_1, answer_part_2 = len(cycles), len(cycles) - cycles.index(banks)

print(answer_part_1, answer_part_2)
