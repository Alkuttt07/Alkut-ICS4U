def save_inventory():
    with open("save.txt", "w") as file:
        for item in inventory.items:
            weapon = item.item
            file.write(f"{item.grid_x}%{item.grid_y}%{item.width}%{item.height}%{weapon.level}%{weapon.damage}%{weapon.durability}%{weapon.cd}%{weapon.hc}%{weapon.cost}\n")

def load_inventory():
    global inventory
    inventory = Inventory()
    with open("save.txt", "r") as file:
        for line in file:
            data = line.split("%")
            grid_x = int(data[0])
            grid_y = int(data[1])
            width = int(data[2])
            height = int(data[3])
            level = int(data[4])
            damage = int(data[5])
            durability = int(data[6])
            cd = float(data[7])
            hc = float(data[8])
            cost = float(data[9])
            weapon = Weapon(level,durability,damage,cd,hc,cost,None)
            item = InventoryItem(weapon,width,height)
            item.grid_x = grid_x
            item.grid_y = grid_y
            inventory.items.append(item)