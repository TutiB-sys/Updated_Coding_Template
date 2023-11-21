# grocery_list=["apple", "banana", "orange", "spinach", "kale", "curry", "potatoes"]

# for item in grocery_list:
#     print(item)

# grocery_list=["apple", "banana", "orange", "spinach", "kale", "curry", "potatoes"]

# for elephant in grocery_list:  # elephant or any name is served as temperary varable
#     print(elephant)

# #==========================================================

# grocery_shops=["apple", "banana", "orange", "spinach", "kale", "curry", "potatoes"]

# for item in grocery_shops:
#     if item[0]=='s':
#         print(item)
#     else:
#         print('Does not start with the letter s')

# letter_to_check='s'

# for item in grocery_shops:
#     if item[0]==letter_to_check:
#         print(item)
#     else:
#         print('Does not start with the letter s')
       
# for item in grocery_shops:
#     if item[0]=='a':
#         print(item)

# for item in grocery_shops:
#     if item[0]=='b':
#         print(item)

# grocery_shops=["apple", "banana", "orange", "spinach", "kale", "curry", "potatoes"]

# letter_to_check='s'

# for item in grocery_shops:
#     if item[0]==letter_to_check:
#         print(item)
#     else:
#         print('Does not start with the letter s')

# using input function

# grocery_shops=["apple", "banana", "cherry", "orange", "kale", "potatoes"]

# letter_to_check = input(" What do you want to check?")

# for item in grocery_shops:
#     if item[0]==letter_to_check:
#         print(item)
#     else:
#         print("Nothing with that letter here")
#         break

#counter, it shows the index number of each item lists
# grocery_shops=["apple", "banana", "cherry", "orange", "kale", "potatoes"]

# letter_to_check = input(" What do you want to check?")
# counter=0

# for item in grocery_shops:
#     if item[0]==letter_to_check:
#         print(item)
#     else:
#         print("Nothing with that letter here")
#     counter +=1
#     print(counter)

#RANGE

for i in range(5):
    print(i)
grocery_shops=["apple", "banana", "cherry", "orange", "kale", "potatoes"]

for i in range(5):
    print(grocery_shops[i])

for i in range(6):
    print(grocery_shops[i])

print("======================================")
# using len() is more effective

grocery_length= len(grocery_shops)

for i in range(grocery_length):
    print(grocery_shops[i])

print("-------------------------------------")

for i in range (len(grocery_shops)):
    print(grocery_shops[i])
print("-----------------------------------")
# range(start, stop, step)

for i in range(0,20,2):# it only prints even numbers from 0 t0 20
    print([i])
print("-----------------------------------")
for i in range(0,10,1):
    print([i])
print("-----------------------------------")

for i  in range(0,17**2,17):
    print([i])

print("-----------------------------------")


# append() , contiune

urgent_groceries=[]

for item in grocery_shops:
    if item[0] in ['a', 'b','c']:
        urgent_groceries.append(item)
    else:
        continue
print(urgent_groceries) 
print("-----------------------------------")   

# shortcut 

my_groceries= [item for item in grocery_shops if item[0] in ('a','b','c')]

print(urgent_groceries)
print("-----------------------------------")
print(my_groceries)
print("-----------------------------------")
#comprehensive python eg

my_math=[ x for x in range(20) if x%2==0]
print(my_math)
