# equality checks
# print(5==5)  # turns out true
#===================================
# or & and 


# x=0
# y=1

# if x:
#     print("howdy")
# elif y:
#     print("Hello from here") 
# if a varable is assigned any value like a number or string, 
# it ll be printed out eventhough there is no true or false statment
# it is known as truthy and falsy
# the value should not be 0 or empty list or set
print("===================")
x=0
y= " The elephant ate penuts"

if x:
    print("howdy")
elif y==True:
    print("Hello from here") # nothing will be printed since it is a falsy or truthy statement


x= ["apple"]
y= " The elephant ate penuts"

if x:
    print("howdy") # it prints this since the x is now has value
elif y==True:
    print("Hello from here")


print("===================")

x=5
y=6

if x!=5 or y==5:
    print('panang curry')
elif x!=5 or y==6:
    print("habesha food")
elif x==6 or y==5:
    print("yee haw")

