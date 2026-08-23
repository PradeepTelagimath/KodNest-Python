word = input()

first = int(input())
second = int(input())
third = int(input())

numbers = (first,second,third)
record = (first,second,third)

#slice the string, List and Tuple
print(f"Middle: {word[1:-1]}")
print(f"First Two: {numbers[:2]}")
print(f"Reserved Tuple: {record[::-1]}")