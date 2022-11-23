list=[]
n=int(input("enternumber of element"))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
for i in range(len(list)):
    for j in range(len(list)):
        if list[i]<list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)
print("smallest  no:",list[0])
print("second smallest  no:",list[1])

