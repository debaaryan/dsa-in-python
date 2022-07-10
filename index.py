import math


def A(n):
    for i in range(math.floor(n/2), n+1):
        j = 1
        while j <= n:
            j = 2*j
            k = 1
            while k <= n:
                print('Deb')
                k = k*2

# (n/2 + 1)(log_2 n + 1)(log_2 n + 1)=n/2 * (log_2 n)^2


A(10)
