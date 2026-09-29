inventory = {
    "Electronics": {
        "Mouse": 15,
        "Keyboard": 8
    },
    "Stationery": {
        "Notebook": 20,
        "Pen": 30
    },
    "Groceries": {
        "Rice": 12,
        "Milk": 10
    }
}

# Read inputs and strip whitespace
category = input().strip()
product = input().strip()
new_stock = int(input().strip())

# Ensure the category exists in the dictionary
if category not in inventory:
    inventory[category] = {}

# Update the product stock
inventory[category][product] = new_stock

# Print the updated dictionary
print(inventory)