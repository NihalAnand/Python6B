
def binary_search(sortedlist,n,x):
 
 start = 0
 end = n - 1

 while(start <= end):
  mid = (start + end)//2
  if (x == sortedlist[mid]):
   return mid
  elif(x < sortedlist[mid]):
   end = mid - 1
  else:
   start = mid + 1 
 
 return -1

n = int(input("Enter the size of the list: "))

sortedlist = []

for i in range(n):
 sortedlist.append(input("Enter {}th element: ".format(i)))

x = input("Enter the number to search: ")
position = binary_search(sortedlist, n, x)

if(position != -1):
 print("Entered number {} is present at position: {}".format(x,position))
else:
 print("Entered number {} is not present in the list".format(x))