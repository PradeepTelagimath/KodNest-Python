#Read the value of n
N=int(input())

#initialize total to counter
Total = 0
count = 1

#loop until count exceeds N
while count <= N:
    Total = Total + count
    count = count + 1

#Display the total
print(f"Total: {Total}")
