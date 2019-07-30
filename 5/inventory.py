stuff = {'rope': 1, 'torch': 4}

def display(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(k,v)
        item_total = item_total + v
    print("Total Items: " + str(item_total))

display(stuff)
