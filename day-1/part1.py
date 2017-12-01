captcha = '91212129'

captcha = captcha + captcha[0]  # "cirricular" list tail

consecutive_pairs = zip(captcha[:], captcha[1:])

answer = sum(int(a) for (a, b) in consecutive_pairs if a == b)

print(answer)
