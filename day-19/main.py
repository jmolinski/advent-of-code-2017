from itertools import count


def available_routes(matrix, x, y):
    return [(x + v[0], y + v[1]) for v in (N, S, W, E)
            if matrix.get(x + v[0], {}).get(y + v[1], ' ') != ' ']


matrix = dict(zip(
    count(),
    [dict(zip(count(), line.replace('\n', '')))
     for line in open('data.txt', 'r').readlines()]
))

N, S, W, E = (-1, 0), (1, 0), (0, -1), (0, 1)

x_prev, y_prev = 0, [k for k, v in matrix[0].items() if v == '|'][0]
x, y = x_prev + S[0], y_prev + S[1]
preferred_vector = S

step = 1
visited_letters = []

while True:
    step += 1

    if matrix.get(x, {}).get(y, '').isalpha():
        visited_letters.append(matrix[x][y])

    routes = available_routes(matrix, x, y)
    if len(routes) == 1:
        break

    routes_without_previous = [r for r in routes if r != (x_prev, y_prev)]
    preferred_route = x + preferred_vector[0], y + preferred_vector[1]

    if preferred_route in routes_without_previous:
        x_next, y_next = preferred_route
    else:
        x_next, y_next = routes_without_previous[0]
        preferred_vector = x - x_next, y - y_prev

    x_prev, y_prev = x, y
    x, y = x_next, y_next

answer_part_1 = ''.join(visited_letters)
answer_part_2 = step

print(answer_part_1, answer_part_2)
