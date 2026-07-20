# x=121 
# rev=0
# while x>0:
#     digit =x%10
#     rev=rev*10+digit
#     x=x//10
#     print(x)
# if x==rev:
#     print("True")
# else:
#     print("False")


list1=[2,4,3]
list2=[5,6,4]
list3=[]
#out= 930->039
num1=""
num2=""
rev=""
for i in list1:
    num1=str(i)+num1
for i in list2:
    num2=str(i)+num2
sum=int(num1)+int(num2)
rev=str(sum)
for i in rev:
    list3.append(int(i))
    
print(list3)