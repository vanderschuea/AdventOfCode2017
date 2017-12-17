

fact_a = 16807
fact_b = 48271
a = 703 #65#
b = 516 #8921#
match = 0
for _ in range(int(40e6)):
    a = (a * fact_a) % 2147483647
    b = (b * fact_b) % 2147483647
    if a & 0b1111111111111111 == b & 0b1111111111111111:
        match += 1

print(match)



