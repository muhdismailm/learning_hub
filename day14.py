# #set

# # s1={1,2,3,4,8,4,4,2,1,5}
# # print(s1)
# # s1.add(10)
# # print(s1)
# # s1.remove(2)
# # print(s1)
# # s1.discard(10)
# # print(s1)

# #dictionary

# dict={
#     "Name":"ismail",
#     "dob":"12/4/2002",
#     "date":8
    
# }

# print(dict)


# s="hello world"
# vo="aeiou"
# vowel=0
# conso=0
# for i in s:
#     if i in vo:
#         vowel+=1
#     else:
#         conso+=1
        
# dict={
#     "vowels": vowel,
#     "consonants": conso
# }
# print(dict)

# dict1 = {"a": 10, "b": 20, "c": 30, "d": 40}
# dict2 = {"b": 50, "c": 60, "e": 70}
# set1=set()

# for i in dict1:
#     if i in dict2:
#         set1.add(i)

# print(set1)
        
        
# n=5
# dict1={x:x**2 for x in range(n)}

# print(dict1)

# n=int(input("enter a range"))
# dict1={}
# for i in range(1,n+1):
#     dict1[i]=i**2

# print(dict1)


# words = ['apple', 'ant', 'banana', 'ball', 'cat', 'car']

# d={}
# for word in words:
#     first=word[0]
    
#     if first in d:
#         d[first].append(word)
#     else:
#         d[first]=[word]
        
# print(d)

# l1=["suzuki","kia","ford","toyota"]

# l2=["alto","seltos","raptor","innova"]

# d={}

# for i in range(len(l1)):
#     d[l1[i]]=l2[i]
    
# print(d)


d1={'a':100,'b':200,'c':500}
d2 = {'a':300,'b':200,'d':400}
d3={}
for x in d1:
    if x in d2:
        sum=d1[x]+d2[x]
        d3[x]=sum
    else:
        d3[x]=d1[x]
for y in d2:
    if y not in d1:
        d3[y]=d2[y]
        
print(d3)