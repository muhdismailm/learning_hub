# num=int(input("enter a number"))
# if num<=1:
#     print("not prime")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")

#task 1

# num=int(input("enter a number"))
# sum=0
# for i in range(num+1):
#     sum=sum+i
# print("sum= ",sum)

#task 2

# print("_____Multiplication table___\n")
# num=int(input("Enter the number for multiplication table : "))

# for i in range(1,11):
#     multi=i*num
#     print(f"{i} * {num} ={multi}")
    
    
# task 3
# print("All even numbers between 1 to 50")
# i=0
# while i<=50:
#     print(i)
#     i+=2
    
# task 4

# num=(input("enter the number"))
# sum=0
# for i in num:
#     sum+=int(i)
# print(sum )

#Task 4.1

# num=int(input("Enter a Three digit number"))
# sum=0
# div=num//100
# sum=sum+div

# mod=num%100
# div=mod//10

# sum=sum+div
# mod=num%10
# sum=sum+mod
# print("sum of digits= ",sum)


#task 5

print("enter numbers")
sum=0
numbers=[]
while(1):
    for i in range(100):
        num=int(input())
        sum=sum+num
        numbers.append(num)
        
        if num==0:
            print("+".join(map(str, numbers)),"=",sum)
            break
        
        
