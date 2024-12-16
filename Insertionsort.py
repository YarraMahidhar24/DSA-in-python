l=[23,10,16,11,20]
for i in range(1,len(l)):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j=j-1
        l[j+1]=key
print(l)