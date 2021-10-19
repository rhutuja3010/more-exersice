password=input("enter the Strong password")
if len(password)>=6 and len(password)<=16:
    # print("right")
    # if password=="$" or password=="@" or password=="&":
    if password == "$" or password=="@":
        print("password is right")
        if 2 in password  or 8 in password:
            print("2 and 8 in password")
            if "A" in password or "Z" in password:
                print("this is strong password")
            else:
                print("this is weak password")
        else:
            print("wrong")
    else:
        print("invalid")
else:
    ("no")


# a=[2,4,-8,7,-3,5]
# i=0
# b=[]
# while i<len(a):
#     if a[i]<0:
#         b.append(0)
#     else:
#         b.append(a[i])
#     i+=1
# print(b)
    


