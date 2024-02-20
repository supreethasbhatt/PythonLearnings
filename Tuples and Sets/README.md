# Tuples:
**Describe**
1. Tuples: ORdered collection or grouping of items. Eg : (1,2,3,4,5)
    - Tuples are immutable, meaning it cannot be updated. 
    - Faster than lists
    - makes code safer from bugs
    - Can be used as valid keys in dictionaries.
    eg: Month of year

**Create -**
- created using ()
- immutable
- faster than lists
- eg: location: {
    (35.123,42.245) : 'Tokyo',
    (56.1034,89.123) : 'Inida'
}


**Access-**
- accessed using the index. 
- eg: tuple_(1,2,34) 
        tuple[1] = 2

**Tuples Built in MEthods**
1. count : Number of times a value is in the tuple
    eg - x.count(3) ===> returns the number of times 3 is present in the tuple
2. index :tell us the index of the given value in the tuple


**Looping:**
1. for x in tuple_name:
    do somthing
2. while can also be used

# Sets:
**Describe** 
1. collection of data with no duplicate values. 
2. Elements are not ordred
3. You cannot access the values using index
4. Used when keeping track of collection of items.

**Syntax**
Eg -
    s = set({1,2,3})
    t = {3,4,5}
    h = {1,2,3,'a','b'}

**SET Methods**
1. add - add data into the set. 
    eg - s.add(4)
2. remov - removes a value from the set. 
    eg - s.remove(3) ---> removes the value from the set
    - if the value is not there, it throws keyerror
3. discrad() - discards the item.
    - does not throw key error if the item does not exist
4. clear - clears the entire set

**Set Math**
1. | --> union
2. & --> common between both (intersect)

**Set Comprehension**
1. {x**2 for x in num} ---> returns a set with doubled values
2. {x:x** 2 for x in num} ---> Creates a dictionarry with x as value and x**2 as value