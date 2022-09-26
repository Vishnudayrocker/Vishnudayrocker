num=[1,2,3,1]
total=0
for i in range(len(num)):
    if(i%2)!=0:
        print(num[i])
        total=total+num[i]
        print("sum of numbers",total)