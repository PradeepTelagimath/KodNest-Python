def convert_to_fahrenheit(celsius_temperatures):
    return [round((c * 9 / 5) + 32, 2) for c in celsius_temperatures]


n = int(input())
celsius_temperatures = list(map(int, input().split()))

fahrenheit_temperatures = convert_to_fahrenheit(
    celsius_temperatures
)

print(*fahrenheit_temperatures)