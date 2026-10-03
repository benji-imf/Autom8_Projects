def collatz(number):  # The Collatz Sequence 
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = 3 * number + 1
        print(result)
        return result
    

try:
    number = int(input("Enter number: "))
    while number != 1:
        number = collatz(number)

except ValueError:
    print("Input integer!")

