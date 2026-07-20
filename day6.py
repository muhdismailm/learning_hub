

# for i in range(1,7):
#     if i%2!=0:
#         print("*"*2*i)
#     else:
#         print("*"*i)



#task  2 butterfly
row=int(input("enter the number of rows"))
row2=row-1
row+=1
for i in range(row):
    print("*"*i+" "*((row*2))+"*"*i)
    row-=1

j=4
for row2 in range(row2,0,-1):
    print("*"*(row2)+" "*j+"*"*row2)
    j+=2
    

