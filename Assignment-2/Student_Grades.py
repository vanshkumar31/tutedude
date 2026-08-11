student_data={
    "Abhi":80,
    "Abhilash":85,
    "Anurag":78,
    "Ansh": 98,
    "Ashish":100,
    "Ajay":78,
    "Akshat":88,
}
user_pref=input("Hi Want you want to do \n1.Add a new student and grade.\n2.Update an existing student’s grade.\n3.Print all student grades.\t: ")

if (user_pref=="1"):
    new_student_name=input("Enter Student Name: ")
    new_student_grade=int(input("Enter Student Grade: "))
    student_data[new_student_name]=new_student_grade
    print("Student added successfully ")
    print(student_data)

elif(user_pref=="2"):
    student_name=input("Enter Student Name: ").title()
    if student_name in student_data:
        print(f'{student_name} score {student_data[student_name]}')
        student_grade=int(input("Enter Student New Grade: "))
        student_data[student_name]=student_grade
        print(f'Result updated successfully {student_name} new score {student_data[student_name]}')
    
    else :  print("Student not exist or may be spelling error ")
elif (user_pref=="3"):
    print(student_data)
else :print ("Enter correct option")


