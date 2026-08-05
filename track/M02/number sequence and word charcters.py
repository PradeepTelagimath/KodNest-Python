#Read the number and word
n = int(input())
word = input()

#print the number sequence 
print("Number: ")
for i in range(1,n+1):
    print(i,end=" ")

#print the word characters
print("Character: ")
for ch in word:
    print(ch,end="")
