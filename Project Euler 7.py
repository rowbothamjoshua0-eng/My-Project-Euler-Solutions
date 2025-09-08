import math
#make list of prime numbers and output prime[10000]
primes = [0]
num = int(input('Which prime would you like? '))
#generating primes
for i in range(2, 110000):
    ran = math.floor(i/2)
    if all(i%j != 0 for j in range(2, ran)):
            primes.append(i)

print(primes)
primes.remove(3)
answer = primes[num]
print(answer)