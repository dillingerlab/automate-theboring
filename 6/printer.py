def print_table(list_of_lists):
    for x in list_of_lists:
        max_length = 0
        for y in x:
            if len(y) > max_length:
                max_length = len(y)
        for a in x:
            print(a.rjust(max_length))


input_list = [['apples', 'oranges', 'cherries', 'banana'],
        ['alices', 'bob', 'carol', 'david'],
        ['dogs', 'cats', 'moose', 'goose']]

print_table(input_list)
