captcha = '91212129'

captcha = captcha + captcha[0]  # "cirricular" list tail
captcha = list(map(int, captcha))

consecutive_pairs = zip(captcha[:], captcha[1:])

answer = sum(a for (a, b) in consecutive_pairs if a == b)

print(answer)
