row=int(input("enter the number of rows"))
row+=1
prime=True
print("*")
for i in range(2,row):
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
        else:
            prime=True
    if prime==True:
         print("*"*i+"*")
    else:
         print("*"*i)    