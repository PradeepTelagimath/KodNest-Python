n = int(input())
marks = list(map(int, input().split()))

ascending_marks = sorted(marks)
descending_marks = sorted(marks, reverse=True)

print(*ascending_marks)
print(*descending_marks)

