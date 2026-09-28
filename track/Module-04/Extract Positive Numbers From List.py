def extract_positive_numbers(numbers):
    return [x for x in numbers if x > 0]


n = int(input())
numbers = list(map(int, input().split()))

positive_numbers = extract_positive_numbers(numbers)

if positive_numbers:
    print(*positive_numbers)
else:
    print("No positive numbers")