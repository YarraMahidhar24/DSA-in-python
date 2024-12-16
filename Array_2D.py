row=int(input("Enter the no of rows"))
col=int(input("Enter the no of cols"))
arr2d=[[0 for co in range(col)] for ro in range(row)]
for ro in range(row):
    for co in range(col):
        item=int(input()) # we can keep it as any type
        arr2d[ro][co]=item
print(arr2d)
# arr3=[list(map(int,input().split())) for i in range(row)] # knowing rows we can do it
# print(arr3)
