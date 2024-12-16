l=[5,8,1,6,2,4,3,7]
for i in range(len(l)):
    min=i
    for j in range(i+1,len(l)):
        if l[min]>l[j]:
            min=j
    l[i],l[min]=l[min],l[i]
print(l)