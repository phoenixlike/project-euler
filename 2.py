x1 = 1
x2 = 2
temp = 0
sum = 0

while x2 < 4000000:
    if x2%2 == 0:
        sum = sum + x2
    temp = x2
    x2 = x2 + x1
    x1 = temp

print sum

