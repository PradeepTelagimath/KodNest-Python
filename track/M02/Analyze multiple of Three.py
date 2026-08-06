limit = int(input()) #10
target = int(input()) #3 

count = 0
total = 0
found = False 

#Examine every number from 1 to the limit 
for i in range(1,limit+1):
    if i % 3 == 0:
        count += 1
        total += i
        if i == target:
            found = True 

#Display the count, total and search result
print("Count:",count)
print("Sum:",total)
if found:
    print("Target Found: Yes")
else:
    print("Target Found: No")