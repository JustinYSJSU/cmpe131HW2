def main():
  myList = [1,2,3,7]
  sort_List(myList)
  print(myList)

#sort_list will take a list input and return it sorted
def sort_List(myList):
 if isinstance(myList, list) == False: #parameter is not a list
  return None

 n = len(myList) #n is the length of the list

 if(n == 0): #list is empty  return None
  return None

 i = 0
 while i < n:
  i2 = i + 1
  while i2 < n:
   if myList[i] > myList[i2]:
    temp = myList[i]
    myList[i] = myList[i2]
    myList[i2] = temp
   i2+=1
  i+=1
 return myList

main()
