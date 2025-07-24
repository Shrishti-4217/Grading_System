
ans="YES"
while(ans!="EXIT"):
    marks=int(input("Enter the marks"))   #give the input of your marks
    if marks<=100 and marks>=90:
        print("A\n")
    elif marks<=89 and marks>=75:
        print("B\n")
    elif marks<=74 and marks>=60:
        print("C\n")
    elif marks<=59 and marks>=40:
        print("D\n")
    elif marks<40:
        print("F\n")
    else:
        print("Invalid Input")
        continue
    ans=input("Would you like to continue==>")  # type EXIT to stop otherwise type yes