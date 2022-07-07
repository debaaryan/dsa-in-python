import math


def A(n):
    count = 0
    for i in range(1, n+1):
        for j in range(1, (i ^ 2)+1):
            for k in range(1, math.floor(n/2)+1):
                print('Deb')
                count += 1
    print(count)


A(4)
