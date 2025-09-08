largest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        number = str(i * j)
        last = len(number) - 1
        if len(number) <= 5:
            int_number = int(number)
            if number[0] == number[last] and number[1] == number[last - 1] and int_number > largest_palindrome:
                largest_palindrome = int(number)      
        else:
            int_number = int(number)
            if number[0] == number[last] and number[1] == number[last - 1] and number[2] == number[last - 2] and int_number > largest_palindrome:
                largest_palindrome = int(number)
       
print(largest_palindrome)        