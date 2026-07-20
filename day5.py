 # #task 1
# row=int(input("enter the number of rows"))

# for i in range(1,row+1):
#         print(" "*(row-i)+"* "*i)

#task

row= int(input("enter number of row"))
i=1
while(i<row+1):
    print(" "*(row-i)+"* "*i)
    i+=1
if i==row+1:
    j=1
    i=i-1
    while(i>=0):
        print(" "*j+"* "*(i-1))
        i-=1
        j+=1