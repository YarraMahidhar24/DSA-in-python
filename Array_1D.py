# 1d array>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
size=int(input("Enter the size fo the array"))
arr=[]
for i in range(size):
    item=input()
    arr.append(int(item))
for j in range(size):
    print(arr[j],end=" ")
print()
# Removing element in arr
d=int(input("Enter the element that need to be deleted"))
if d in arr:
    arr.remove(d)
    for k in range(size-1):
        print(arr[k],end=" ")
else:
    print(f"{d} is Not in array")
