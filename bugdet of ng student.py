student = int(input("enter the number of student"))
expenses = int(input("enter the expenses of per student"))
total_expenses = student * expenses
if total_expenses <= 50000:
    print("hum budget ke andar hai")
else:
    print("hum budget ke bahar hai")

