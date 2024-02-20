shopping_cart={"name":"cat_litter","qty":1,"price":33}
print(shopping_cart)


for values in shopping_cart.values():
    print(values)
    
for keys in shopping_cart.keys():
    print(keys)

for k,v in shopping_cart.items():
    print(f"key is {k} and value is {v}")
    
#dictionary tes:
shopping_cart_dict={"name":"cat_litter","qty":1,"price":33}
#copy
# 
copy_shop = shopping_cart_dict.copy()
print(f"copy_shop == shopping_cart_dict is : {copy_shop == shopping_cart_dict}")
print(f" copy_shop is shopping_cart_dict is : {copy_shop is shopping_cart_dict}")
#clear
clear_shop = shopping_cart_dict.clear()
#fromkeys
new_dict = {}.fromkeys("a","b")
print(new_dict)

new_dict_1 = {}.fromkeys(["email"],'unknown')
print(new_dict_1)

new_dict_2 = {}.fromkeys("a",[1,2,3,4,5])
print(new_dict_2)

new_dict_3 = {}.fromkeys("email",'unknown') #this will give 'e':'unknown','m':'unknown','a':'unknown'
print(new_dict_3)

#get
shopping_cart_dict={"name":"cat_litter","qty":1,"price":33}
print(shopping_cart.get("name"))


# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:
if food in bakery_stock:
    print('{} left'.format(bakery_stock[food]))
else:
    print("We don't make that")

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')


numbers = dict(a=1,b=2,c=3)

squared_nums = {key : value **2 for key,value in numbers.items() }
print(squared_nums)

print({ num : num **2 for num in [1,2,3,4]}) # setting the value as num ** 2

str1 = "supretha"
str2 = "bhatt"
print({str1[i] : str2[i] for i in range(0,len(str2))}) #map 2 lists 


#change every key and every value upper cased in the below dictionary:
name = {"first":"supreetha","middle":"s","last":"bhatt"}

new_name = {key[0].upper()+key[1:]:value[0].upper()+value[1:] for key,value in name.items()}
print(new_name)


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]: list2[i] for i in range(0,3)}
answer = dict(zip(list1,list2))  

'''
Create a dictionary called answer , that makes each first item in each list a key and
the second item a corresponding value.  That's a terrible explanation. 
I think it'll be easier if you just look at the end goal:

{'name': 'Jared', 'job': 'Musician', 'city': 'Bern'} 


'''
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]] 
answer = {i[0] : i[1] for i in person} # answer = dict(person) or answer = {k:v for k,v in person}
print(answer)

#assign the vowels the value 0
answer = {}.fromkeys(['a','e','i','o','u'],0) #or answer = {char:0 for char in 'aeiou'} 

