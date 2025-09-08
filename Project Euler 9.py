import math
square_numbers = [x for x in range(1, 710)]

#find triplets
for a in range(1, 501):
    for b in range(1, 501):
        c = pow(a, 2) + pow(b, 2)
        for i in range(0, 709):
            if math.sqrt(c) == square_numbers[i] and a+b+math.sqrt(c) == 1000:
              answer = a*b*math.sqrt(c)

print(answer)