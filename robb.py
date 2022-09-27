lst = []
  
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
    e = int(input())
    lst.append(e) 
print(lst)

max_1=max(lst)



if n==3:
  print("the possible outcomes to rob is",max_1)
else:
  print("")  


if n==4:
   if lst.index(max_1)==0:
     print("the possible outcomes are",max_1+lst[2])
   elif lst.index(max_1)==1:
    print("the possible outcomes are",max_1+lst[3])
   elif lst.index(max_1)==2:
    print("the possible outcomes are",max_1+lst[0])
   elif lst.index(max_1)==3:
    print("the possible outcomes are",max_1+lst[1])
   else:
    print("no possible outcomes")
    
    

     



