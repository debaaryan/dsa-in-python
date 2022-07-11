import math


def A(k):
    n = pow(2, 2 ** k)
    for i in range(1, n+1):
        j = 2
        while j <= n:
            print('Deb {}'.format(j))
            j = int(math.pow(j, 2))


A(2)
