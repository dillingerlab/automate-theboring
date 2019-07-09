def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return (number * 3) + 1
try:
    number = input("Enter a number")
    print(int(number))
    new_number = collatz(int(number))
    print(new_number)
    while new_number != 1:
        new_number = collatz(new_number)
        print(new_number)
except ValueError:
    print("Bad input")
