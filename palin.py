str1="mal#yalam is our mother tong#e.It is a langua#e spok#n in the Indian state of Kerala.madam ha#nah teaches Malayalam.neve# is a #tudent of hannah."
words=str1.split(".")  
print(words)
l=[]
for i in words:
    l.append(i)
    print(l)

asd=l[0].split()[::-1]
asd1=l[1].split()[::-1]
asd2=l[2].split()[::-1]
asd3=l[3].split()[::-1]
asd4=asd+asd1+asd2+asd3
print(" ".join(asd4))
t=[]
for i in asd4:
    t.append(i)
print(t)


t[4]=t[-10]
t[18]=t[-6]
t[-1]='neven'
t[0]="@@@@@"
t[-4]="@@@@@@@"
t[11]="@@@@@@"
t[12]="@@@@@@@"

print(t)
print(" ".join(t))
