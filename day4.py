# #task 1

num=int(input("enter a number"))
prime = True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
if prime:
    print("number is prime")
else:
    print("number is not prime")

# #task 2

# # num=int(input("enter a number"))
# # sum=0

# # for i in range(1,num) :
# #     if num%i==0:
# #         sum=sum+i
# # if sum==num:
# #     print("number is perfect")
# # else:
# #     print("not a perfect number")

# #task 3
# #143
# # num=(input("enter a number"))
# # num1=int(num)
# # arr=[]
# # sum=0
# # for i in num:
# #     arr.append(int(i))
# # for i in arr:
# #     def fact(i):
# #         if i<=1:
# #             return 1
# #         return i*fact(i-1)
# #     sum+=fact(i)

# # if num1==sum:
# #     print("strong number")
# # else:
# #     print("not a strong number")
    
    
# #task 4,1124
# # num=int((input("enter a number")))
# # sum=0
# # product=1
# # num1=num
# # while(num>0):
# #     rem=num%10
# #     sum+=rem
# #     product*=rem
# #     num=num//10
    
# # if product==sum:
# #     print("spy number")
# # else:
# #     print("not a spy number")

# #task 5
# 1634


# num1=input("enter a number")
# if num1.isdigit():
#     l=len(num1)
#     sum=0

#     for i in range(l):
#      sum+=int(num1[i])**l

#     if sum==int(num1):
#      print("armstrong number")
#     else:
#      print("not a armstrong number")
# else :
#     print("number adikkadaa")
