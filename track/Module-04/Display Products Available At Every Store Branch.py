n = int(input())
branches = []

for _ in range(n):
    data = input().split()
    branch_name = data[0]
    products = data[1:]
    branches.append({
        "branch": branch_name,
        "products": products
    })

# Iterate through each branch and display branch: product
for item in branches:
    branch = item["branch"]
    for product in item["products"]:
        print(f"{branch}: {product}")