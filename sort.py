def main():
  myList = [1,4,3,5]
  sort_List(myList)
  print(myList)

#sort_list will take a list input and return it sorted
def sort_List(myList):
 n = len(myList) #n is the length of the list
 for i in range(n): #through the list
  for i2 in range(i, n-i-1):
   if myList[i] > myList[i+1]:
    temp = myList[i]
    myList[i] = myList[i+1]
    myList[i+1] = temp
 return myList

main()
