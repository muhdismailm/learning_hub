# li=[1,2,5,3,11,13,14,17,19]
# s=[]
# pairs=[]

# for i in li:
#     if i <=1:
#         continue
#     else:
#         for j in range(2,i):
#            if i%j==0:
#                break
#            else:
#                s.append(i)
#                break
# for i in range(len(s)-1):
#     if abs(s[i+1]-s[i])==2:
#         pairs.append((s[i],s[i+1]))
# print(pairs)


# num=int(input("Enter an even number greater than 4 "))
# s=[]
# pair=[]
# if num%2!=0:
#     print("enter even number greater than 4")
# else:
#     if num<4:
#         print("enter number greater than 4")
#     else:
#         for i in range(2,num+1):
#             prime=True
#             for j in range(2,i):
#                 if i%j==0:
#                     prime=False
#                     break  
#             if prime:
#                 s.append(i)
# for i in range(len(s)-1):
#     for j in range(len(s)-1):
#         if s[i]+s[j]==num:
#             pair.append((s[i],s[j]))
# print(pair)
        


# l2=[]
# digit=0
# for i in range(1,20):
#     j=i
#     sum=0
#     while(j>0):
#         digit=j%10
#         sum=sum+digit
#         j=j//10
#     if i%sum==0:
#         l2.append(i)
# print(l2)
            
li=[1,2,3,4,5,6,7,8,9]
pair=[]

for i in range(len(li)):
    for j in range(i,len(li)):
        for k in range(len(li)):
            if (li[i])**2+(li[j])**2==li[k]**2:
                pair.append((li[i],li[j],li[k]))
print(pair)


# ------function----
d={}
li=[1,2,3,11,6,9,1234,23,28,153]

def check_prime(num):
    is_prime=True
    for j in range(2,num):
        if num%j==0:
            is_prime=False
    if num<2:
        is_prime=False  
    if is_prime:
        d.setdefault("prime",[]).append(num)
    else:
        d.setdefault("composite",[]).append(num)

def check_even(num):
    if num%2==0:
        d.setdefault("even",[]).append(num)
    else:
        d.setdefault("odd",[]).append(num)

def check_perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum=sum+i
    if sum==num:
        d.setdefault("perfect",[]).append(num)
            
def check_armstrong(num):
    sum=0
    number=num
    l=len(str(num))
    
    while(num>0):
        digit=num%10
        sum=sum+digit**l
        num=num//10
    if sum==number:
        d.setdefault("armstrong",[]).append(number)
        
def check_neon(num):
    original=num
    sum=0
    product=num**2
    while product>0:
        digit=product%10
        sum=sum+digit
        product//=10
    if sum==original:
        d.setdefault("Neon",[]).append(original)
        
    
for i in li:
    check_even(i)
    check_prime(i) 
    check_perfect(i)  
    check_armstrong(i)
    check_neon(i)       
print(d)
    
    