marks1 = int(input("Enter your 1st  sub marks out of 100: "))
marks2 = int(input("Enter your 2nd  sub marks out of 100: "))
marks3 = int(input("Enter your 3rd sub marks out of 100: "))
marks4 = int(input("Enter your 4th  sub marks out of 100: "))
marks5 = int(input("Enter your 5th  sub marks out of 100: "))

sum=marks1+marks2+marks3+marks4+marks5
avg=sum/5

if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")
elif avg >= 60:
    print("Grade: D")
elif avg >= 50:
    print("Grade: E")
else :
    print("Grade: F")

