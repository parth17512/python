# users first name and last name and greet him and his name should be in capital (only first letter and last letter )
# take input from user and print its table 
# if user inputs flaot value than give the user a message to enter integer value.
# a = input("enter first name-")
# b = input("enter last name-")

# c=a.capitalize()
# d=b.capitalize()
# print(f"hi {c} {d}")
a=int(input("enter the number which you want to print table of-"))
b =1
while b<=10:
    print(f"{a} X {b} ={a*b}")
    b=b+1