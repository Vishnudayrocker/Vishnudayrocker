from msvcrt import kbhit


a=[2,2,4,4]
a.sort(reverse=True)
print(a)
k=len(a)
if k==3:
    total_price=a[0]+a[1]+a[2]+a[3]
total_price=a[0]+a[1]
print(total_price)