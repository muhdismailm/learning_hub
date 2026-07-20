# list1=["car","auto","bike"]
# list1.append("Boat")
# list1.insert(2,"van")
# print(list1)
# list1.pop(0)
# print(list1)
# list1.remove("auto")
# print(list1)
# num=len(list1)
# print(num)
# print("for loop")
# for i in list1:
#     print(i)

# list2=["4","5"]
# result=0
# for i in list2:
#     result+=int(i)
# print(result)

# print(list2.append("x"))
# print(list2)

# list1=[3,6,2,7,9,-10]
# list1.sort()
# great=-float("inf")
# small=float("inf")
# for i in list1:
#     if i>great:
#         great=i
#     if i<small:
#         small=i
# print("greatest =",great)
# print("smallest =",small)
# print("2nd largest",list1[1])
# print("difference=",great-small)


# list1.sort()
# print(list1)
# print("smallest=",list1[0])
# print("greatest=",list1[-1])
# print("difference=",list1[-1]-list1[0])

# print("max=",max(list1))
# print("min=",min(list1))
# print(list1.index(min(list1)))
# print(list1.index(max(list1)))
# print("difference=",max(list1)-min(list1))

list1 = [30, 82, 48, 90, 12, 45, 67]
largest = -float("inf")
second_largest = -float("inf")
for i in list1:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest:
        second_largest = i
print("Largest =", largest)
print("Second Largest =", second_largest)