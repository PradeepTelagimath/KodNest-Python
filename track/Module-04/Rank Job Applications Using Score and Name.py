n = int(input())
applications = []

for _ in range(n):
    name, score = input().split()
    applications.append((name, int(score)))

ranked_applications = sorted(applications, key=lambda x: (-x[1], x[0]))

for name, score in ranked_applications:
    print(name, score)