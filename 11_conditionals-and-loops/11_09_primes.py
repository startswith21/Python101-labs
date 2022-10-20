# Print out every prime number between 1 and 1000.

num = range(1, 1001)

for num in range(1, 1001):
    if num > 1:
        for onum in range(2, num):
            if num % onum == 0:
                break
        else:
            print(num)



    