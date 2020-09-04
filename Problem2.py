i = 1
j = 2
sum1 = 0
k = 0

while k < 4000000:
    k = i + j
    if k % 2 == 0:
        print(k)
        sum1 += k
    i = j
    j = k
# k = i + j
# print(k)
print(sum1)


