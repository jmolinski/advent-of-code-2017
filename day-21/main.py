from itertools import chain, product
from functools import reduce

puzzle_data = open('data.txt', 'r').read()

initial = ('.#.', '..#', '###',)

raw_patterns = [
    tuple([r for r in rows])
    for rows in
    [[x.strip() for x in p.split('=>')]
     for p in puzzle_data.split('\n')]
]


def rotate_90(matrix):
    return tuple(zip(*matrix[::-1]))


def flip(matrix):
    return tuple(tuple(r[::-1]) for r in matrix)


def pattern_combinations(pattern):
    pattern = tuple([tuple(p) for p in pattern.split('/')])

    modifiers_combinations = chain.from_iterable(
        product([flip, rotate_90], repeat=i) for i in range(4)
    )

    comb = [reduce(lambda p, m: m(p), modifiers, pattern)
            for modifiers in modifiers_combinations]

    return ['/'.join(''.join(r) for r in m) for m in comb]


def enrich_patterns(original):
    eneriched = dict()

    for input_pattern, output_pattern in original:
        eneriched.update(
            dict.fromkeys(
                pattern_combinations(input_pattern), output_pattern)
        )

    return eneriched


def split_into_chunks(l, chunk_size):
    return [l[i:i + chunk_size]
            for i in range(0, len(l), chunk_size)]


def split_grid(grid):
    side_size = len(grid)
    split_size = 2 if side_size % 2 == 0 else 3
    chunks = split_into_chunks(grid, split_size)

    chunks = [tuple('/'.join([r for r in rows])
                    for rows in zip(*[split_into_chunks(x, split_size) for x in grid_part]))
              for grid_part in chunks]

    return chunks


def merge_grid(subgrids):
    grid = [tuple(zip(*[x.split('/') for x in row]))
            for row in subgrids]
    grid = [tuple(''.join(subrow) for subrow in row) for row in grid]

    return tuple(chain.from_iterable(grid))


def run_simulation(grid, mapping, rounds=1):
    for _ in range(rounds):
        grid = merge_grid(
            tuple((mapping[subgrid] for subgrid in subgrids_row))
            for subgrids_row in split_grid(grid)
        )

    return grid


patterns = enrich_patterns(raw_patterns)

p1_grid = run_simulation(initial, patterns, rounds=5)
p2_grid = run_simulation(initial, patterns, rounds=18)

answer_part_1 = ''.join(p1_grid).count('#')
answer_part_2 = ''.join(p2_grid).count('#')

print(answer_part_1, answer_part_2)
