a=[]
def numbers_less_than_twenty(list):
  counter = 0
  while counter < len(list):
    item = list[counter]
    a.append(list[counter])
    if item > 20:
      list.remove(item)
    else:
        # a.append(list[counter])
        counter += 1
  return list

num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]

num_list_sub_20 = numbers_less_than_twenty(num_list)

print ("Initial list", a)
print ("List that doesn't contain numbers greate than 20", num_list_sub_20)