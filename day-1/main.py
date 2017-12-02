with open('data.txt', 'r') as f:
    captcha = f.read()


def values_pairs(jump_length):
    yield from zip(captcha, captcha[jump_length:] + captcha)


answer_p_1 = sum(int(a) for a, b in values_pairs(1) if a == b)
answer_p_2 = sum(int(a) for a, b in values_pairs(len(captcha) // 2) if a == b)

print(answer_p_1, answer_p_2)
