original_scores = []

for _ in range(3):
    original_scores.append(int(input()))

alias_scores = original_scores

replacement_score = int(input())
alias_scores[0]=replacement_score
additional_score = int(input())
alias_scores.append(additional_score)

print("Original:",original_scores)
print("Alias:",alias_scores) 
print("Shared Object:",original_scores is alias_scores)