def collatz(number):
    if number % 2 == 0:
        return number // 2

number = input("Enter a number")
list = [number]
print(list)
status = True
while status == True:
    number2 = input("Enter a number")
    list.append(number2)
    user_input = input("Do you want to add another number (Y/N)?")
    print(user_input)
    if user_input == 'Y':
        counter = True
    else:
        counter = False
        break
print(list)
