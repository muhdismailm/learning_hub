# def change_list(my_list):
#     my_list.append(40)
#     my_list.append(50)
#     print("Inside function:", my_list)
    
# list1 = [10, 20, 30]
# change_list(list1)
# print("Outside function:", list1)

# def change_string(my_string):
#     my_string += " World"
#     print("Inside function:", my_string)
    
# my_str = "Hello"
# change_string(my_str)
# print("Outside function:", my_str)

# def func(name,age):
#     print("Name:", name ,"and Age:", age)
    
# func(name="John",age= 25)
# names=["Alice", "Bob", "Charlie", "David"]

# def greet(nameS):
#     for name in nameS:
#         print("Hello, " + name + "!")

# greet(names)

def func(name1,message,name2):
    print("Hello", name1 + " and " + name2 + ", " + message)
    
func(message="How are you?", name1="Alice",name2="Bob")
