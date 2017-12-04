import itertools
from collections import Counter

with open('data.txt', 'r') as f:
    passphrases = [row.split() for row in f.readlines()]

answer_part_1 = sum(Counter(pp) == Counter(set(pp)) for pp in passphrases)

answer_part_2 = sum(
    Counter(pp) == Counter(set(pp))
    and
    Counter(str(sorted(word)) for word in pp).most_common(1)[0][1] <= 1
    for pp in passphrases
)

print(answer_part_1, answer_part_2)
