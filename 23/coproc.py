from math import sqrt
from itertools import count, islice

''' Look at the code:
        There are two loops which stupidly test if 
        b has dividors, if it does f is set to 0 and
        h is incremented
'''


# taken from:
#  https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


b = 108400
c = b+17000+1  # to use range correctly in python
cnt = 0
for x in range(b, c, 17):
    if not is_prime(x):
        cnt += 1

print(cnt)



