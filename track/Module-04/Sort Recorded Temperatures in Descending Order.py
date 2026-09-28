n = int(input())
temperatures = list(map(int, input().split()))

temperatures.sort(reverse=True)

print(*temperatures)