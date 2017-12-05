import itertools
from collections import Counter

with open('data.txt', 'r') as f:
    offsets = [int(row) for row in f.readlines()]


def exit_maze(offsets, get_offset_change):
    required_jumps = 0
    current_offset = 0
    while 0 <= current_offset < len(offsets):
        required_jumps += 1
        offset_value_change = get_offset_change(offsets[current_offset])
        offsets[current_offset] += offset_value_change
        current_offset += (offsets[current_offset] - offset_value_change)
    return required_jumps


answer_part_1 = exit_maze(offsets[:], lambda offset: 1)
answer_part_2 = exit_maze(offsets[:], lambda offset: -1 if offset >= 3 else 1)

print(answer_part_1, answer_part_2)
