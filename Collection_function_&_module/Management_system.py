# Assessement 
 
menu=("""
                MENU
      
        Press 1 for Counsellor
        Press 2 for Faculty
        Press 3 for Student
""")

student={}      # Creating main empty dictionary to add data.
status=True
while status:
    print(" ~~~~~~~ WELCOME TO STUDENT MANAGEMENT SYSTEM ~~~~~~~")
    print("-"*55)
    print(menu)
    roleid=int(input("Enter a role id : "))
    if roleid==1:       # 1st Counsellor's Choice.
        cmenu=("""
            1. Add Student
            2. Remove Student 
            3. View all Students
            4. View Specific Student
    """)
        print(cmenu)
        choice=int(input("Enter a Choice by Counsellor : "))
        if choice==1:       # 1st To Add Student.
            sn=int(input("Enter a Serial Number : "))
            fname=input("Enter a First Name : ")
            lname=input("Enter a Last Name : ")
            pnum=int(input("Enter a Contact Number : "))
            sub=input("Enter a subject : ")
            marks=int(input("Enter a marks : "))
            fee=int(input("Enter a fees : "))

            student[sn]={
                    'First name' : fname,
                    'Last name' : lname,
                    'Phone number' : pnum,
                    'Subject' : sub,
                    'Marks' : marks,
                    'Fees'  : fee}
            print("Student Added successfully.")
            choice=input("Do you want to add more student? If yes then enter y or yes. : ").lower()
            if choice=='y' or choice=='yes':
                status=True
                continue
            else:
                continue

        elif choice==2:     # 2nd To Remove Student.
            print(student)
            remove=int(input("Enter Serial Number of student you want to remove : "))
            if remove in student.keys():
                student.pop(remove)
            print("Student removed successfully, Ramaining are :- ",student)

        elif choice==3:     # 3rd To View All Students.
            print(student)
        
        elif choice==4:     # 4th To View Specific Student.
            view=int(input("Enter Serial number to View Student Details : "))
            if view in student.keys():
                print(student[sn])
            else:
                print("No Details Available.")

        else:
            print("Please select from the given choice.")

    elif roleid==2:     # 2nd Faculty's Choice
        fmenu=("""
            1. Add marks of student
            2. View all student 
    """)
        print(fmenu)
        choice=int(input("Enter a Choice by Faculty : "))
        if choice==1:       # 1st To Add Markes of Student.
            std_id=int(input("\nEnter student serial number in which you want to add marks : "))
            if std_id in student.keys():
                marks=int(input("Enter new marks : "))
                student[std_id]['Marks']=marks
                print("Marks updated successfully.")
                print("Updated Student Database:")
                for sn, si in student.items:
                    print(f"Student Information {si}")

        elif choice==2:     # 2nd To View All Students.
            print(student)
        
    elif roleid==3:     # 3rd Student's Choice.
        smenu=("""
            1. View Details
    """)
        print(smenu)
        choice=int(input("Enter a Choice by Student : "))
        if choice==1:       # 1st View Details.
            user=int(input("Enter your Serial Number : "))
            if user in student:
                print(f"{student[sn]}")
            else:
                print("No Details Available.")
                print("~"*50)
        else:
            print("Invalid Input, Enter from the given options.")
            print("~"*50)
            status=True
        
    else:
        print("Invalid Input please enter proper input.")
        status=False