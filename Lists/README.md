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

**Built In functions of list:**

**~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~**
1. **len** : length - returns the number of items in the list.
    >> print(len(list_name))
2. **list** : used to make a list. 
    >> number_lis = list(range(1,4))

**Accessing values in a List:**

**~~~~~~~~~~~~~~~~~~~~~~~~~~~~**
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

**Iterating over lists:**

**~~~~~~~~~~~~~~~~~~~~~**
1. Print each item in the list can be done using "for" or "while". With while loop you would have to first get the length of the numbers handy. This can be done using the len function.
   >> number = [1,2,3,4]
      for num in number:
         print(num)

          or
      
    >> i=0
      while i < len(number):
         print(numbers[i])
         i = i+1
    

**List Methods:**

**~~~~~~~~~~~~~~~**

**Adding items to List**

1. List methods are accessed using the dot operator after the list.
2. **append**: adds the value to the end of the list. It can be used to add only 1 item at a time and not multiple items at a time.
    >> eg: num =[1,2,3,4,5]
            num.append(6)
            num = [1,2,3,4,5,6]

            num.append(6,7) --> will not work
            num.append([6,7]) --> will work, but as : num = [[1,2,3,4,5],[6,7]]
            
3. **extend**: All the values passed are added to the list. 
    >> eg: num = [1,2,3,4]
            num.extend([5,6,7,8])
            num =[1,2,3,4,5,6,7,8]

4. **insert** : used to insert at a random position in a list. 
    >> eg : num = [1,2,3,4]
            num.insert(2,"hi") ------> list.insert(pos,value). Pos can be negative to indicating it would start inserting numbers from the end of the list. (-1 indicates last position. -2 indicates last but one position)
            num = [1,2,3,"hi",4]

**Deleting Items from a list**

1. **clear** : Lest common used. Removes all the items in the list and empties it. 
    >> eg: items = ["socks","pant","shoe"]
            items.clear() ---> empties the entire list. Returns an empty list.

2. **pop** : Removes one element from the list. If yoused without position, removes the last element from the list. You can also capture the item being popped out. 
    >> eg: items: [1,2,3,4,5]
            items.pop() ----> removes 5
            items = [1,2,3,4]
            items.pop(1) --> removes the 2rd element from then list i.e 2
            items = [1,3,4]
            last_items = items.pop() -----> value 4 would be stored in last_items

3. **remove** : Provide the item that has to be removed. It removes the first instance of the item specified. If the item does not exist, it would throw an error.
    >> eg: names = ['sup','hello','what','bye','sup']
            names.remove('sup') ---> returned list would be ['hello','what','bye','sup']
            names.remov('tata') ---> It would throw an error saying the item is not in the list.

**Leftovers** 

1. **index** : Find the index of a value specified.
    >> eg: nums.index(5) --> returns the position where the first occurence of 5 is found.
            nums.index(5,1) --> find the position of the number 5 after the 1st index (2nd lement in the index)
            nums.index(5,1,4) --> Find the position of 5 between the 2 specified indexes i.e. 1st (2nd element) and 4th (5th element)
2. **Count** : Returns the number of times "x" occurs in the list.
    >> eg: nums = [1,2,4,2,5,2,6,7,8]
            nums.count(2) ---> this returns 3
            nums.count(9) ---> this returns 0

3. **reverse** : It reverses the elements of the list in place. 
    >> eg: nums = [1,2,3,4]
            reversed = nums.reverse()
            ----> reversed would have : [4,3,2,1]

4. **sort** : sorts the values in ascending order. 
    >> eg: another_list = [4,2,3,1]
            another_list.sort() --> returns the o/p --> [1,2,3,4]

5. **join** : sting method. Not list method. It adds the specified "String" to every item in the list. 
    >> eg: num = [1,2,3,4] --> value inside the list should bea string for this to work.
            '.hello'.join(num) ---> this would not work.

            num = ['hello','how','doing']
            '.bye'.join(num) ---> outputs : 'hello.byehow.byedoing'

**Slicing in Lists**

**~~~~~~~~~~~~~~~~~**
1. Make new lists using the old lists. 
2. The slicing is specified using square brackets. 
3. syntax:
        >> some_list[start:end:step]
        >> eg: num = [1,2,3,4,5]
                num[1:] ----> [2,3,4,5]
                num[3:] ----> [5]
                num[:3] ----> [1,2,3,4]
                num[-1:] ----> [5]
                num[-3] ----> [3,4,5]
                num[0:2] ---> [1,2]
                num[1::-1] ---> [2,1]
                num[:1:-1] --> [5,4,3,2]
                reverse a string ---> list[::-1]

**List Comprehension:**

**~~~~~~~~~~~~~~~~~~~**
1. syntax :
    [__ for __ in __ ]:
    eg :
    num = [1,2,3]
    [x*10 for x in nums]:
    >> tricky: [bool(val) for val in [0,[],'']] ----> gives : [false,false,false]
2. List comprehension with conditional logic using keyword like if, else:
    >> eg: num = [1,2,3,4,5,6]
            evns = [num for num in numbers if num % 2 == 0]

Nestd lists:
1. They are multi-dimensional lists
2. USed in games like tic tak toe, complex data tructures: Tic Tac Toe
3. eg: num = [[1,2,3],[4,5,6],[7,8,9]]
        num[0][1] ---> gives 2
4. Printing values in nested lists use 2 loops. 
    num = [[1,2,3],[4,5,6],[7,8,9]]
    for x in num:
        for val in x:
            print(val)

5. Nested List Comprehension:
    num = [[1,2,3],[4,5,6],[7,8,9]]
    [[print(val) for val in x] for x in num]

    eg :
    board = [[num for val in range(1,4)]for val in range(1,4)]
        --> outer: [1,2,3,]
        1st: [1] replaces it with [[1,2,3],2,3,4]