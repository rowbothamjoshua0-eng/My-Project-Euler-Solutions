primes = [x for x in range(1, 100000)]
number = 600851475143
list = []
list2 = []
store = []

for n in range(1, 3):
    for i in range(0, len(primes)):
        if number % primes[i] == 0:
            factors = number/primes[i]
            list.append(factors)
            list.append(primes[i])

    number = list[2]
    for i in range(0, len(primes)):
        if number % primes[i] == 0:
            factors = number/primes[i]
            list2.append(factors)
            list2.append(primes[i])

    store.append(list[3])
    store.append(list2[3])
    number = list2[2]
    list.clear()
    list2.clear()

print(store)