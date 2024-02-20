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


    