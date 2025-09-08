n = 0
sum = 0
x = 0

g = [x*3 for x in range(0, 334)]
f = [x*5 for x in range(0, 201)]
list = g + f
list.sort()

for i in range (0, 534):
    x = list[i]
    n = list[i - 1]
    if x != n:
        sum = sum + list[i]
print(sum)


#alternate method
result = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        result = result + i
print(result)