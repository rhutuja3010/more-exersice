sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
# string=sentence.split( ) 
# print(string)

a=[]
b=" "
for i in sentence:
    if i==" ":
        a.append(b)
        b=" "
    else:
        b+=i
if b:
    a.append(b)
print(a)
    






# words = "navgurukul is great"
# counter = 0
# while counter < len(words):
#     print (words[counter])
#     counter+=1