n = int(input())
scores = [] #[78,92,61,84,67]

#Read and store all scores in the list 
for i in range(n):
    score = int(input())
    scores.append(score)
search_score = int(input())

#Dispaly the highest ,lowest and total scores
print(f"Highest Score: {max(scores)}")
print(f"lowest Score: {min(scores)}")
print(f"Total Score: {sum(scores)}")    

#Display wheather serach_score is present
if search_score in scores:
    print("Search Result: Found")
else:
    print("Search Result: Not Found")
        


