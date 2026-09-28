def build_square_dictionary(numbers):
    return {x: x ** 2 for x in numbers}


n = int(input())
numbers = list(map(int, input().split()))

square_by_number = build_square_dictionary(numbers)

for number, square in square_by_number.items():
    print(number, square)