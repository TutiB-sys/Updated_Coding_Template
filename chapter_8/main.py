#cars=["audi","ferrari","ford focus", "toyota sienna hybrid"]

# cars.append("BMw")
# cars.append("Honda")
# cars.append("chrysler")

#function is used to reuse the statment multiple times 

# def car_adder():  # with no paratesis 
#     cars.append("car")

# car_adder()      # No agrgument in the parateses since we do not feed the function the paramater
# # car_adder()
# # car_adder()
# print(cars)

# def car_adder1(car_to_add):
#     cars.append(car_to_add)


# car_adder1("BMW")
# car_adder1("Honda")
# car_adder1("Chrysler")
# 
#print(cars)


# def car_adder(car_to_add):
#     if car_to_add[0].lower() in 'abcdefg':
#         print("This car starts with A-G")
#         cars.append(car_to_add)
#     else:
#         print("This car starts with H-Z and we don't allow it in this club")
#     for car in cars:
#         if len(car)<=5:
#             cars.remove(car)
#             print(f"{car} IS NOT ADDED BECAUSE IE TOO FEW CHARATER ")

# car_adder("BMW")
# car_adder("Honda")
# car_adder("Aeep")

# print(cars)

# cars=["audi","ferrari","ford focus", "toyota sienna hybrid"]
# groceries=["grapes", "oranges", "cheese"]

# def item_adder(things_to_add, target_list):
#     if things_to_add[0].lower() in 'abcdefg':
#         print(f"{things_to_add} starts with A-G")
#         target_list.append(things_to_add)
#     else:
#         print(f"{things_to_add} starts with H-Z and we are not allowing to add to our lists")
   
  

# item_adder("BMW", cars)
# item_adder("Honda", cars)
# item_adder("apples", groceries)
# item_adder("eggs", groceries)
# item_adder("zappers", groceries)

# print(cars)
# print(groceries)

# Return allows to use the funtion's  bodies for operating more tasks  

def addtwo(num):
    return num+2

print(addtwo(3))

print("======================================")

def addthree(num):
    return num+3

print(addthree(addtwo(5)))

print("======================================")

def namePrinter(first, middle, last):
    return f"The name's {last}, {first} {middle} {last}"

print(namePrinter("Ruth", "Tekekeste", "Kidane"))

print("======================================")


def namePrinter(first, last, middle):
    return f"The name's {last}, {first} {middle} {last}" # the order matters it ll creat logical errors

print(namePrinter("Ruth", "Tekekeste", "Kidane"))

print("======================================")
def namePrinter(first, last, middle = ''):   # if we do not print the middle name 
    return f"The name's {last}, {first} {middle} {last}."

print(namePrinter("Ruth", "kidane"))

print("======================================")

def giveMeMyGroceries(grocery_to_add):
    grocery_list=[" apple", "oragnge", "onion"]
    grocery_list.append(grocery_to_add)
    return grocery_list

print(giveMeMyGroceries("pasta"))

def giveMeMySports(name_to_add):
    sports_dic= {'soccer': ["Machester city", "shasu","demak"],
                 'basketball': 'Golden Gate',
                 'biycle': 'Red sea'}
    sports_dic['wresling']= name_to_add
    return sports_dic
# print(giveMeMySports('Dan Gable'))
print(giveMeMySports([ 'Dan Gable', 'The Rock',' The undertaking'])) # we can add one string or lists 