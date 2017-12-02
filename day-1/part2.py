original_captcha = '12131415'

captcha = 2 * original_captcha

jump_length = len(original_captcha) // 2

values_pairs = zip(captcha[:len(original_captcha)], captcha[jump_length:])

answer = sum(int(a) for (a, b) in values_pairs if a == b)

print(answer)