def Student_result():
    student=input("Enter Your Name :")
    Age=int(input("Enter Your Age :"))
    Roll_No=int(input("Enter Your Roll No :"))
    DOB=input("Enter Your Date of Birth (DD/MM/YYYY) :")
    DIVISION=input("Enter Your Division :")

    m1=int(input("Enter Your Marks :"))
    m2=int(input("Enter Your Marks :"))
    m3=int(input("Enter Your Marks :"))

    if m1<0 or m1>100:
        return "Invalid Marks"
    
    if m2<0 or m2>100:
        return "Invalid Marks"

    if m3<0 or m3>100:
        return "Invalid Marks"
    

    Total=m1+m2+m3
    AVG=int(Total/3)

    if AVG>=90:
        Grade="A"
        result="Pass"

    elif AVG>=75:
        Grade="B"
        result="Pass"

    elif AVG>=50:
        Grade="C"
        result="Pass"

    else:
        Grade="F"
        result="Fail"

    return f"""

=====WELCOME TO YOUR REPORT CARD=====

Student Name : {student}
Age          : {Age}
Roll No      : {Roll_No}
Division     : {DIVISION}
Total Marks : {Total}
Average : {AVG}
Result : {result}

"""
print(Student_result())
