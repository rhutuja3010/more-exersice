# new_list = [1, 2, 5, 10, 12, 13, 16, 20]

list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
list3=[]
for i in list1:
    if i not in list3:
            list3.append(i)
for j in list2:
        if j not in list3:
                list3.append(j)
print(list3)

# a=[1,4,6,7,5,6]
# b={}
# for i in a[::-1]:
#         b={i:b}
# print(b)



