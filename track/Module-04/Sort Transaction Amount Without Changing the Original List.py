n = int(input())
transactions = list(map(int, input().split()))

sorted_transactions = sorted(transactions)

print(*sorted_transactions)
print(*transactions)
