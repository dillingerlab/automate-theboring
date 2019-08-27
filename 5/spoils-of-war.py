stuff = {'rope': 1, 'torch': 4}
kill = ['rope', 'brick']


def display(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(k,v)
        item_total = item_total + v
    print("Total Items: " + str(item_total))

def addToStuffs(inventory, additions):
    for x in additions:
        if x in inventory:
            inventory[x] = inventory[x] + 1
        else:
            inventory[x] = 1
    return inventory

stuff = addToStuffs(stuff, kill)
display(stuff)
