#Dictinary is usefull it saves time when searching and find a value , it get it by
# going striaght , and it has keys that allows for easy access

my_dict={
    'key': 'value',
    1: 'spaghetti',
    2:'pasta',
    3: 'pizza',
    'cats':'No thanks',
    10.5: 4
}

print(my_dict)
print("=========================")
print(my_dict[2])
print(my_dict['cats'])

#Adding a new value

my_dict['new key']= ' Alphones'
print(my_dict)

#overriding
my_dict[2]= 'cheese'
my_dict[2]= 'endless breadsticks' # the key is unique , it ll print only latest value
print(my_dict)

#delting 

del my_dict[2]
print(my_dict)

#get
x=my_dict.get(3)
print(x)

print("----------------------------------")
print(my_dict)

# #for loop
# for key, value in my_dict.items(): # key , value , items() are inbuilts 
#     print(f'The key is {key}')
#     print(f'And this is the: {value}')

for k, v in my_dict.items(): # key , value , items() are inbuilts 
    print(f'The key is {k}')
    print(f'And this is the: {v}')

print("======================================")
# loop the keys only
for key in my_dict.keys():
    print(key)

print("======================================")
#loop the value
for value in my_dict.values():
    print(value)

#dic can have a varity of objects, lists, and dics inside
my_dict={
    'soccer': ['machester', 'chelisi','shasu'],
    'formula': {'driver': 'andretti'},
    'football':{'nfl': ['seahawks','packers', 'Patriots'],
    'college': ['celmson', 'UNLA', 'NU'],
    1:5 }
}
print(my_dict['soccer'][0]) # prints the key and value

print(my_dict['football']['college']) 

print(my_dict['football']['college'][1])# this wont print since 1 is a key too
#isinstance is boolean that identifies the data type

print(isinstance(my_dict['football']['college'][1], int))# it is  false since 'collage is a list type 
print(isinstance(my_dict['football']['college'], list))# it is true
print(isinstance('I m a proud mama', str))