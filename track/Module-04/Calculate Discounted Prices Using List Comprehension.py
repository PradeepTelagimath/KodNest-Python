def calculate_discounted_prices(prices, discount_percentage):
    return [round(price - (price * discount_percentage / 100), 2) for price in prices]

n = int(input())
prices = list(map(int, input().split()))
discount_percentage = int(input())

discounted_prices = calculate_discounted_prices(
    prices, discount_percentage
)

print(*discounted_prices)