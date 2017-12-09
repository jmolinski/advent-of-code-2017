with open('data.txt', 'r') as f:
    stream = (c for c in f.read())


def read_garbage(input_stream):
    ommited = 0
    for c in input_stream:
        if c == '!':
            next(input_stream)
        elif c == '>':
            return ommited
        else:
            ommited += 1


depth, total_score, garbage_size = 0, 0, 0

for c in stream:
    if c == '<':
        garbage_size += read_garbage(stream)
    elif c == '{':
        depth += 1
    elif c == '}':
        total_score += depth
        depth -= 1


answer_part_1, answer_part_2 = total_score, garbage_size

print(answer_part_1, answer_part_2)
