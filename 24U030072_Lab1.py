def grade(marks):  #function that takes input as marks and returns the grade
    if marks<=100 and marks>=90:
        return "A"
    elif marks<=89 and marks>=75:
        return "B"
    elif marks<=74 and marks>=60:
        return "C"
    elif marks<=59 and marks>=40:
        return "D"
    elif marks<40:
        return "F"
    else:
        return "Invalid Input"
    
ans="YES"
while(ans!="EXIT"):
    marks=int(input("Enter the marks"))   #give the input of your marks
    
    gd=grade(marks)  #function called to give the grade
    print("Your Grade is",gd,"\n")

    ans=input("Would you like to continue==>")  # type EXIT to stop otherwise type yes
