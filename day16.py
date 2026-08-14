def digit(left,right):
    s=[]
    for i in range(left,right+1):
        temp=i
        flag=1
        while temp>0:
            num=temp % 10
            if num==0:
                flag=0
                break
            if i %num!=0:
                flag=0
                break
            temp//=10
        if flag==1:
            s.append(i)
    print(s)


left=int(input("enter left limit"))
right=int(input("enter right limit"))
digit(left,right)

