def collatz(number):  # The Collatz Sequence 
    try:
        if number % 2 == 0:
            result = number // 2
            print(result)
            return result
        else:
            result = 3 * number + 1
            print(result)
            return result
    except ValueError:
        print("Input integer!")

number = int(input("Enter number: "))
while number != 1:
    number = collatz(number)
