number1=int(input("enter the 1st number"))
number2=int(input("enter the 2nd number"))
number3=int(input("enter the 3rd number"))
if number1>number2 and number1>number3:
    print(number1 ,":is grater")
elif number2>number1 and number2>number3:
    print(number2,":is grater")
else:
    print(number3,":is grater")