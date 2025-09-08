for i in range(100000000, 1000000000):
    if all(i%j == 0 for j in range(1,21)):
        print(i)