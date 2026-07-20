# string=input("enter a string")
# string1=string[::-1]
# if string==string1:
#     print("palindrome")
# else:
#     print("not palindrome")
    
# s = input("Enter a string: ")

# reverse = ""

# for i in s:
#     reverse = i+reverse

# if s == reverse:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# print("numbers")
# for i in range(1,101):
#     if i%(5*3)==0:
#         print("pizzbuss")
#     elif i%3==0:
#         print("pizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)

# string=input("enter a string")
# vowel_count=0
# consonant_count=0
# vowels=["a","e","i","o","u"]

# for i in string:
#     for j in range(0,5):
#         if i==vowels[j]:
#             vowel_count+=1
#             break
#     else:
#         consonant_count+=1
# print("vowels=",vowel_count)
# print("consonat=",consonant_count)


# string="pythhhoooon"
# count=0
# letter=""

# for i in string:
#     if count<string.count(i):
#         count=string.count(i)
#         letter=i
# print("letter =",letter)
# print("count=",count)

list=[1,2,3,4,6]
for i in range(len(list)):
    if i%2==0:
        print(list[i])