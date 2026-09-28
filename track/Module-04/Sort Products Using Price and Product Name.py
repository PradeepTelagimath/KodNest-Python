n = int(input())
products = []

for _ in range(n):
    product_name, price = input().split()
    products.append((product_name, int(price)))

sorted_products = sorted(products, key=lambda x: (x[1], x[0]))

for product_name, price in sorted_products:
    print(product_name, price)