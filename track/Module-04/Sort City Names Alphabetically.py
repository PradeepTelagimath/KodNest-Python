n = int(input())
cities = []

for _ in range(n):
    cities.append(input().strip())

sorted_cities = sorted(cities)

for city in sorted_cities:
    print(city)