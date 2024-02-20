Limitations of list:
1. Used to store a particular peice of information. Eg: A list of names. 
2. eg:
    Shopping Cart
        Item
            name
            qty
            pricr
        Item
            name
            qty
            price
    to store this in a list, it would be as: cart =[["Cat_litter",1,$33],["pencil",3,30]]

    Storing this data in a list is thus difficult and hence we would have to use a new data type for it. This can be done using dictionaries.

**Create and access dictionaries**
1. It is a key value pair
2. Define by using the keyword "dict" or as shown in 3
    eg : 
    cat = dict(name = 'kitty')
    cat = dict(name = 'kitty','age'=2)
3. eg:
    shopping_cart={"Item1":{"name":"cat_litter","qty":1,"price":33}}

Accessing Data in dictionaries:
1. The same syntax as list is used.
2.  dictionary_name[key] --> if the key exists we get the corresponding value. If not, we get an error.

**Iterating dictionaries:**
1. Loops through values:
    ---> .values() ---> returns a list of the values.
    --->  for value in dict.values() 
            print(value)
2. Loop through keys
    ---> .keys() ---> returns a list of the keys.
    ---> for keys indict.keys():
            print(key)
3. Loop through key and value
    ---> .items() ---> it goves you a tuple of items in a list. o/p: [('name','cat_litter'),('qty',1)] 
    ---> for key,value in dict.items():
            print(key,value)
4. There is not guarantee of order in dictionary unlike of lists.
5. Test the presence of a key or value :
    done with "**in**" key word.
    eg: "name" in shopping_cart ----> returns true of it exists

**Dictionary Methods:**
1. clear : Empties the dictionary ---> dict.clear() : o/p --> {}
2. copy : Makes a copy of the dictionary in a new dictionary in memory. 
    eg : 
3. fromkeys : Called on empty doctionary. Pass in iterable collection and value. It assigns each value of the key with an unknown value.
    {}.fromkeys("a",[1,2,3,4,5]) ---> {'a': [1, 2, 3, 4, 5]}
    new_dict_3 = {}.fromkeys("email",'unknown') #this will give 'e':'unknown','m':'unknown','a':'unknown'
4. get() : retrives the key in an object and return NONE instead ofkey error if the key does not exist.
5. pop(value) : Removes an item from dict. Input: key. O/p: Returns the value but not key. An input is always needed here. 
    eg: new_dict.pop('email) --> gives the email
        new_dict.pop() --> error
6. popitem() : Removes a random item from the dictionary. It does not take any arguments. It resturns a random value in the form of tuple from the dictionary.
7. update : used to update the keys and values in the dictionary with another value.
    eg : first = dict(a=1,b=2,c=3)
        second.update(first)


Data Modelling with Dictionaries:
Model a playlist :
Plalist has:
1. Title, author, list of songs.
2. Each Song has: a title, artist/multiple artists, duration, order to the songs
    playlist = {
    "Title":"Calms",
    "Author":"Supeetha",
    "songs":[
        {"title":"flowers","artist":["miley"],"duration":3.5},
        {"title":"lover","artist":["taylor","justin"],"duration":5.5}
        
        ]
    }