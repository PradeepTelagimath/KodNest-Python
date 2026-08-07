#Read teh course details 
course_name = input()
current_week = input()
course_status = input()

#create the original tuple
course_detiles = (course_name,current_week,course_status)

#Read the updated week
updated_week = input()

#Create and assign new tuple
Updated_details = (course_name,updated_week,course_status)
course_detiles=Updated_details

#Display the details
print(course_detiles)
