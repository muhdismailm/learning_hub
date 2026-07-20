# # # # string=input("enter a string")
# # # # if len(string)<2:
# # # #     print("empty string")
# # # # elif len(string)==2:
# # # #     print(string+string)
# # # # elif len(string)>=3:
# # # #     last=len(string)
# # # #     print(string[0:2]+string[last-2:last])


# # # string=input("enter a string\n")
# # # string1="ing"
# # # string2="ly"
# # # if len(string)<3:
# # #     print(string)
# # # elif len(string)>=3:
# # #     if string[-3:]!=string1:
# # #         print(string+string1)
# # #     elif string[-3:]==string1:
# # #         print(string+string2)
        
        
# # string="The occurrences of each word in a given sentence"
# # arr=string.split()
# # count=0
# # temp=""
# # for i in arr:
# #     if len(i)>count:
# #         count=len(i)
# #         temp=i
# # print("longest word =",temp)
# # print("number of letters=",count)
    

# string=input("enter a string")
# string2=string.replace(string[0],"$")
# string3=string[0]
# print(string3+string2[1:])

# string="hello"
# if len(string)>2:
#     string2=string[-2:]
#     print(4*string2)
# else:
#     print("invalid")

# string=input("enter a string")
# if len(string)%4==0:
#     string1=string[::-1]
#     print(string1)
# else:
#     print(string)

# string=input("enter a string")
# for i in string:
#     if i.isdigit():
#         print("False")
#         break
# else:
#     print("True")

# string="hello"
# string2=""
# for i in string:
#     if string.count(i)==1:
#         string2+=i
# print(string2)
# string="heloo"
# string2=""
# for i in string:
#     if string.count(i)>=2:
#         string2+=i
#         break
# print(string2)
    
string=input("enter a string")
num=0
string1=input("enter the character")
for i in string:
    if string1==i:
        num+=1
print("output=",num)

        