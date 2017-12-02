import itertools

with open('data.txt', 'r') as f:
    matrix = [list(map(int, row.split())) for row in f.readlines()]

answer_part_1 = sum(max(row) - min(row) for row in matrix)

answer_part_2 = sum(
    max([a // b, b // a])
    for row in matrix for (a, b) in itertools.combinations(row, 2)
    if a % b == 0 or b % a == 0
)

print(answer_part_1, answer_part_2)
