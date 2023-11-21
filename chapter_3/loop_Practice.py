# append() , contiune

grocery_shops=["apple", "banana", "cherry", "orange", "kale", "potatoes"]
urgent_groc=[]

for item in grocery_shops:
    if item[0] in ['a', 'c','p']:
         urgent_groc.append(item)
    else:
         continue

print(urgent_groc)

print("-------------------------------")

names= ["ali","belule", "merry", "feri"]

fav_names=[]

for favirate in names:
    if favirate[0] in ['a', 'b','f']:
       fav_names.append(favirate)
    else:
        continue

print(fav_names)  


       

