print(" Help me God \n") # \n makes a new line
print(" I want to find a cool job")
print (" I want be a \t data \n scientist") # \t print one sentence in with a space

# if class
x= 1

if x >10:
    print("x is big")
    print("x is smALL")
elif x==1:   # it is else if in python
    print("x is equal")
    
else:
    print(" x is small")

#Boolean in if 

y= True
x= False
if y==True:    # It prints the boolean if it is true to the condition
    print("x is big")
    print("LOOK AT THIS CODE")
elif x==1:
    print("x is equal")
else:
    print(" x is small")


if y:    # the same as the y== True, It prints the boolean if it is true to the condition
    print("x is big")
    print("LOOK AT THIS CODE")
elif x==1:
    print("x is equal")
else:
    print(" x is small")


#list

my_list=["apple", "banana","orange", "lemon"]
print(my_list[:-1])  # it kicks out the last order list
print(my_list[:-2])   # it kicks out the last 2 order lists
  

print(my_list[::-1]) #it prints backward to th list
print(my_list[0::3])
print(my_list[0::2])

print(f'my favorate foods are {my_list[1]},a silice of {my_list[0]}, and {my_list[3]} chips') #'f' formats the the print statment
age=11
print (f'my age is {age}, it is my birthdate')