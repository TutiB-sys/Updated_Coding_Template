my_input=input('what is my input')
print(my_input)

x=0

while x<=10:
    print(x)
    x+=1
   #OR

while True:
    print(x)
    x +=1
    if x>50:
        break

     #OR
flag=True

while flag:
    print(x)
    x+=1
    if x>100:
        flag=False


while True:
    my_name = input("what is your name?\n")
    if my_name.lower() == 'quit' :
        break
    elif my_name.lower()[0] in 'abcdefg':        # string acts like list, it check with the indexes
        print('please proceed to first table One')
    elif my_name.lower()[0] in 'hijklmnop':
        print('please proceed to the second table')
    elif my_name.lower()[0] in 'qrstuvwxyz':
        print('please proceed to the last table')

for letter in ' ya he weee ki hahe':
        print(letter)
    
