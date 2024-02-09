**What**?

Collection of grouping of items. 
Kind of Data structure. 
Similar to arrays in Java,C,C++

**How**?
instead of storing values in separate variables- 
item1=banana
item2=apple
store -
items = ['banana','apple','mango']
lists = ['a',1,2,'hello',4]

Lists have a lot of built in methods.

**Built In functions of list:
**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. **len** : length - returns the number of items in the list.
    >> print(len(list_name))
2. **list** : used to make a list. 
    >> number_lis = list(range(1,4))

Accessing values in a List:
~~~~~~~~~~~~~~~~~~~~~~~~~~
1. Lists always start with 0 index
2. print a particular data in a list, use []. It can be accessed using positive and negative integers.
    >> eg: colours = ["purple", "teal"]
            colours[0] = purple
            colours[1] = teal
            colours[-1] = teal
            colours[-2]= purple
3. using the **in** operator. it returns true if the element exists in the list if not it returns false. 
    >> eg: friends = ["ash","cash"]
            "ash" in friends ---> returns true
            "hello" in friends ---> returns false

Iterating over lists:
~~~~~~~~~~~~~~~~~~~~~
1. Print each item in the list can be done using "for" or "while". With while loop you would have to first get the length of the numbers handy. This can be done using the len function.
   >> number = [1,2,3,4]
      for num in number:
         print(num)

          or
      
      i=0
      while i < len(number):
         print(numbers[i])
         i = i+1
    

