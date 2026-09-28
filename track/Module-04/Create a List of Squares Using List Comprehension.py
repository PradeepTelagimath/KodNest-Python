def create_squares(numbers):
    return [x ** 2 for x in numbers]

n = int(input())
numbers = list(map(int, input().split()))
squares = create_squares(numbers)
print(*squares)