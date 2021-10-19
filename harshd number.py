# i=1
# while i <= 1000:
#     temp=i
#     sum=0
#     while temp!=0:
#         remd=temp%10
#         sum=sum+remd
#         temp=int(temp//10)
#     if i%sum==0:
#         print(i,end=" ")  
#     i+=1




for i in range (1,1000):
    sum=0
    tem = i
    while tem!=0:
        r=tem%10
        sum=sum+r
        tem=tem//10
    if i%sum==0:
        print(i,end=" ")

    
# i=1
# while i<=1000:
#     sum=0
#     tem = i
#     while tem!=0:
#         r=tem%10
#         sum=sum+r
#         tem=tem//10
#     if i%sum==0:
#         print(i,end="  ")
#     i+=1
    