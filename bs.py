x = int(input())
n = int(input())
best = 20
s = 7
last = 0


if n == 0:
    print(best)
elif n == s:
    print(x)
elif n < s:
    last = x - n
    if last <= 0:
        print(0)
    else:
        print(last)
elif n > s:
    last = x - n
    if last <= 0:
        print(0)
    else:
        print(last)
