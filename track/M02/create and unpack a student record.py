name = (input())
course = input()
score = int(input())

#Create the tuple
student_record = (name,course,score)

#Unpack the tuple
name,course,score = student_record

#Display the unpacked values
print(f"Name: {name}")
print(f"Course: {course}")
print(f"Score: {score}")            