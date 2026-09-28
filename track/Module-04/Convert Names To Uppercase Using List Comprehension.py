def convert_to_uppercase(names):
    return [name.upper() for name in names]


n = int(input())
names = input().split()

uppercase_names = convert_to_uppercase(names)

print(*uppercase_names)