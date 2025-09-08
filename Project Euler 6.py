#sum of squares of natural numbers
number = 0
sum = 0
sum_one = 0
sum_two = 0

for i in range(1, 101):
    sum_one += pow(i, 2)

#square of sum of natural numbers
for i in range(1,101):
    sum += i
    sum_two = pow(sum, 2)
    
answer = abs(sum_two - sum_one)
print(answer)