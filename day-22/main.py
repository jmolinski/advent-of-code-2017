import copy

matrix = dict(enumerate([dict(enumerate(l.replace('\n', '')))
                         for l in open('data.txt', 'r').readlines()]))
matrix_center = (len(matrix) // 2, len(matrix[0]) // 2)
N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)
INFECTED, CLEAN, WEAKENED, FLAGGED = '#.WF'


DIRS = {
    'right': {
        N: E,
        S: W,
        E: S,
        W: N,
    },
    'left': {
        N: W,
        S: E,
        E: N,
        W: S,
    },
    'reversed': {
        N: S,
        S: N,
        W: E,
        E: W,
    },
    'forward': {
        N: N,
        S: S,
        W: W,
        E: E,
    }
}


def get_cell(matrix, x, y):
    if x not in matrix:
        matrix[x] = {y: CLEAN}
    if y not in matrix[x]:
        matrix[x][y] = CLEAN

    return matrix[x][y]


def simulate_virus(matrix, bursts=10000, part=1):
    x, y = matrix_center
    infected_cells = 0
    current_direction = N

    direction_changes = {
        INFECTED: 'right',
        CLEAN: 'left',
        WEAKENED: 'forward',
        FLAGGED: 'reversed',
    }

    cell_mapping = {
        1: {
            CLEAN: INFECTED,
            INFECTED: CLEAN,
        },
        2: {
            CLEAN: WEAKENED,
            WEAKENED: INFECTED,
            INFECTED: FLAGGED,
            FLAGGED: CLEAN,
        }
    }[part]

    for _ in range(bursts):
        cell = get_cell(matrix, x, y)

        matrix[x][y] = cell_mapping[cell]
        infected_cells += [cell == CLEAN, cell == WEAKENED][part - 1]

        next_dir = DIRS[direction_changes[cell]][current_direction]
        current_direction = next_dir
        x_v, y_v = next_dir

        x, y = x + x_v, y + y_v

    return infected_cells


answer_part_1 = simulate_virus(copy.deepcopy(matrix), bursts=10 ** 4, part=1)
answer_part_2 = simulate_virus(copy.deepcopy(matrix), bursts=10 ** 7, part=2)

print(answer_part_1, answer_part_2)
