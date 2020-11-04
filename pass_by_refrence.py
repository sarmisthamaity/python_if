def numbers_less_than_twenty(num_list):
  counter = 0
  num_list_sub=[ ]
  while counter < len(num_list):
    if num_list[counter] < 20:
      # list1.remove(list1[counter])
      num_list_sub.append(num_list[counter])
      num_list.remove(num_list[counter])
    counter=counter+1
  # return(num_list_sub)
  # num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
  print ("Initial list",num_list)
  print ("List that doesn't contain numbers greate than 20", num_list_sub)
  return(num_list_sub)
num_list = [12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
num_list_sub_20 = numbers_less_than_twenty(num_list)
print(num_list_sub_20)



