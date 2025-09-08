import math
remove = []
for i in range(2, 2000000):
    ran = math.ceil(math.sqrt(i))
    if all(i%j != 0 for j in range(2, ran + 1)):
            remove.append(i)
print(remove)
print(max(remove))

sum = 0
for i in remove:
    sum += i
print(sum + 2)


    