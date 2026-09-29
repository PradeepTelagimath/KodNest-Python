n = int(input())
inventory = {}

for _ in range(n):
    category, product_count = input().split()
    product_count = int(product_count)
    
    products = input().split()
    
    # Store the list of products under the category key
    inventory[category] = products

print(inventory)