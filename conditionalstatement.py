temperature = 13
if temperature > 25:
    print("it is hot")
else:
    print("it is cold")

    # A program that returns the largest number among three numbers
num1 = 45
num2 = 56
num3 = 21
if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")
    # A program that checks whether a number is even or odd
number = 56
if number % 2 == 0:
    print(number, " is even")
else:
    print(number, " is odd")
    # A program that checks whether a number is prime or not
number = 17
if number == 1:
    print(number, "is not a prime number")
elif number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            print(i, "times", number // i, "is", number)
            break
else:
    print(number, "is a prime number")
