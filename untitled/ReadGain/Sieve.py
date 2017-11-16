a = int(input())


def seiveoferroth(m1, m2):
    count = 0
    count2 = 0
    prime = [True for i in range(m2+1)]
    p = 2
    while p*p <= m2:
        if prime[p]:
            for k in range(p*2, m2+1, p):
                prime[k] = False
        p += 1

    for g in range(m1, m2+1):
        for t in range(2, g+1):
            if prime[t]:
                count += 1
        if prime[count]:
            count2 += 1
        count = 0
    return count2


for i in range(a):
    b = input()
    c = b.split(' ')
    m1, m2 = int(c[0]), int(c[1])
    l = seiveoferroth(m1, m2)
    print(l)


