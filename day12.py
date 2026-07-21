# tu=(1,2,3,4,5)
# li=list(tu)
# print(li)
# li.append(50)
# print(li)
# tu=tuple(li)
# print(tu)

#take1

# tu=('Python', 'list', 'exercises', 'practice', 'solution')
# list1=list(tu)
# list2=[]
# tup=""
# size=int(input("enter the size"))
# for i in list1:
#     if len(i)==size:
#         list2.append(i)
# tu2=()
# tu2=tuple(list2)
# print(tu2)
        
        
#task2

# l1=[1, 1, 3, 4, 4, 5, 6, 7]
# l2=[0, 1, 2, 3, 4, 4, 5, 7, 8]

# l3=l1+l2
# sum=0
# for i in l3:
#     sum+=i
# avg=sum/len(l3)

# print(avg)


#task3

# tu=(1, 2, 4,3, 6, 8, 10, 12, 14, 16, 17)
# li=list(tu)
# li.sort()
# li2=list(tu)
# print(li)
# print(li2)
# if li==li2:
#     print(True)
# else:
#     print(False)
            

# tu=(10, 20, 30, 40, 20, 50, 60, 40)
# li=list(tu)
# li2=[]
# count=1
# product=1
# for i in li:
#     if i not in li2:
#         li2.append(i)

# for i in li2:
#     product*=i
# print(product)


# tuple1 = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# li=list(tuple1)
# s=""
# for i in li:
#     s+=i

# print(s)
# print(type(s))

# tu=((10, 10,10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# result=[]
# sum=0
# for i in tu:
#     for j in i:
#         sum+=j
#     avg=sum/len(i)
#     result.append(avg)

# print(result)

# tu=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# li=list(tu)
# result=[]

# for i in li:
#     tuple1=i[:-1]+(100,)
#     result.append(tuple1)
# print(result)

li=[10, "b", "a",56]
        
sum=0
digit=0
for i in li:
    if type(i)==int:
        while(i>0):
            digit=i%10
            sum+=digit
            i//=10
print(sum)