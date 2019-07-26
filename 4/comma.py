def sentence(list):
    total = len(list) 
    final = ''
    count = 0
    while count < total:
        if count < (total - 1):
            final = final + "'" + list[count] + "', "
            count = count + 1
        else:
            final = final +  "'" + list[count] + "'"
            count = count + 1
    print(final)


number = input("Enter an item for the list ")
list = [number]
print(list)
status = True
while status == True:
    number2 = input("Enter an item for the list  ")
    list.append(number2)
    user_input = input("Do you want to add another item (Y/N)? ")
    if user_input == 'Y':
        counter = True
    else:
        counter = False
        break
print("You provided the following list: " + str(list))
sentence(list)
