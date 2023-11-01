# Assessement 
 
print(" ~~~~~~~ WELCOME TO STUDENT MANAGEMENT SYSTEM ~~~~~~~")
print("-"*55)
print("""
        Press 1 for Counsellor
        Press 2 for Faculty
        Press 3 for Student
""")

roleid=int(input("Enter a role id : "))
student={}      # Creating main empty dictionary to add data.
status=True
while status:
    if roleid==1:
        print("""
            1. Add Student
            2. Remove Student 
            3. View all Students
            4. View Specific Student
    """)
        choice=int(input("Enter a Choice by Counsellor : "))
        if choice==1:
            sn=int(input("Enter a Serial Number : "))
            fname=input("Enter a First Name : ")
            lname=input("Enter a Last Name : ")
            pnum=int(input("Enter a Contact Number : "))
            sub=input("Enter a subject : ")
            marks=int(input("Enter a marks : "))
            fee=int(input("Enter a fees : "))
            sub1=input("Enter another subject : ")
            marks1=int(input("Enter a marks : "))
            fee1=int(input("Enter a fees : "))

            student[sn]={
                    'First name' : fname,
                    'Last name' : lname,
                    'Phone number' : pnum,
                    'Subject' : sub,
                    'Marks' : marks,
                    'Fees'  : fee,
                    'Anothe Subject' : sub1,
                    'Marks' : marks1,
                    'Fees'  : fee1

                }
            print("Student Added successfully.")
            choice=input("Do you want to add more student? ").lower()
            if choice=='y' or choice=='yes':
                status=True

        elif choice==2:
            print(student)
            remove=int(input("Enter Serial Number of student you want to remove : "))
            if remove in student.keys():
                student.pop(remove)
            print("Student renoved successfully.",student)



        elif choice==3:
            print(student)


    elif roleid==2:
        print("""
            1. Add marks of student
            2. View all student 
    """)
        choice=int(input("Enter a Choice by Faculty : "))
        if choice==1:
            pass
        elif choice==2:
            print(student)
        
    elif roleid==3:
        print("""
            1. View Details
    """)
        choice=int(input("Enter a Choice by Student : "))
        if choice==1:
            user=int(input("Enter your Serial Number : "))
            print(student.keys())
        status=True
        
    else:
        print("Invalid Input please enter proper input.")