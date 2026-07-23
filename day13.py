# li1=[1,4,2,3,5,"a",6]
# li2=[2,3,6,4,2,5,"a"]
# li3=[]
# for i in li1:
#     if i in li2:
#         li3.append(i)
# print(li3)


# li1=[1,4,6,3,4,5,5,6]
# li2=[]

# for i in li1:
#     if i not in li2:
#         li2.append(i)
# print(li2)

# li=[2,4,6,2,3,4,7]
# print(li[::-1])

# li=[2,5,6,7,3,8,10]
# even=0
# odd=0
# for i in li:
#     if i%2==0:
#         even+=1
#     elif i%2==1:
#         odd+=1
# print("even=",even)
# print("odd=",odd)

# li=[2,5,4,7,2,5,9]
# sum=0
# for i in li:
#     sum+=i
# print(sum)

# li=[-2,-6,-3,6,2,-4,6]
# positive=0
# negative=0
# for i in li:
#     if i>=0:
#         positive+=1
#     else:
#         negative+=1
# print("positive=",positive)
# print("negative=",negative)

# li=[2,6,4,8,2,0,4,7]
# count=0
# sum=0

# for i in li:
#     sum+=i
#     count+=1

# avg=sum/count

# print("average=",avg)

# li=[3,6,5,2,7,5,8,8]
# count=0
# num=int(input("enter the number"))
# for i in li:
#     if num==i:
#         count+=1

# print(f"count of {num}=",count)


# li=[2,5,4,6,3,7]
# sum=0
# li2=[]
# for i in li:
#     sum+=i

# avg=sum/(len(li))
# for i in li:
#     if i> avg:
#         li2.append(i)
    
# print(li2)

# li=[2,0,3,5,0,3,9,0,7]
# result=[]
# for i in li:
#     if i!=0:
#         result.append(i)

# while(len(result)<len(li)):
#     result.append(0)
    
# print(result)

# li=[2,0,3,5,0,3,9,0,7]
# for i in li:
#     if i==0:
#         li.remove(i)
#         li.append(0)
# print(li)

tu=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in range(0,len(tu)):
    li=list(tu[i][i])
    
print(li)