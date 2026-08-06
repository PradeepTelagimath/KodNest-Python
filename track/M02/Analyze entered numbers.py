#Read how many numbers will be entered
number_count = int(input()) 

#Initialize counter and total
positive_count = 0
negative_count = 0
zeros_count = 0
total_sum = 0   

#Read and analyze each number 
for i in range(number_count):
    num = int(input())  
    total_sum +=num 

    if num > 0:
        positive_count += 1
    elif num <0:
        negative_count += 1
    else:
        zeros_count += 1    

#Display the results
print(f"Positive Count: {positive_count}")
print(f"Negative Count: {negative_count}")
print(f"Zeros Count: {zeros_count}")
print(f"Total Sum: {total_sum}")    
