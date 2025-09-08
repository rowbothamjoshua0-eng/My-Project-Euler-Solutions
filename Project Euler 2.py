first = 1
second = 2
sum = 2

for i in range(0,100):
    new = first + second
    first = second
    second = new
    if new%2 == 0 and new < 4000000:
        sum = sum + new
        print(sum)
