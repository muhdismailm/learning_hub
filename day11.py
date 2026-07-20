# list1=[1,3,5,4,7]
# list2=[4,7,3,8,9]
# list3=[]
# for i in list1:
#     for j in list2:
#         if i==j:
#             list3.append(i)

# print(list3)
list1=[2,6,4,5,5,5,7,8,2]
count1=1
for i in list1:
    if count1 < list1.count(i):
        list1.remove(i)
print(list1)
    
        
    


# list1=[4,6,2,3,6,8]
# list2=list1[::-1]
# print(list2)
    
# list1=[5,7,3,4,8,9]
# even=0
# odd=0
# for i in list1:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("number of evens=",even)
# print("number of odd =",odd)