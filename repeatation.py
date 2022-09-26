


main_str=[]
index_str=[]
repeat=[]
name=input("enter the word=")
for i in name:
    index_str.append(name.count(i))
    main_str.append(i)
print(main_str)
print(index_str)
m=index_str.index(max(index_str))
print(main_str[m],"is the most repeating word")
letter=input("enter the letter=")
for i in range(len(name)):
    if(name[i]==letter):
        print(letter,"is found at position",i)