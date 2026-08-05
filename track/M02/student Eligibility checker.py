#Read marks, attendence and project completion status 
Marks = int(input("Enter the marks"))
Attendence = int(input("Enter the attendence"))
Project_status = input("Enter the project completion status")

#check the academic requriments
if(Marks>=60 and Attendence>=75):

    #check the project completion status 
    if(Project_status=="yes"):
        print("Student is Eligible")
    else:
        print("Student is not Eligible")
else:
    print("Student is not Eligible")

