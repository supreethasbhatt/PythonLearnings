**Lambdas**
1. nameless functions which are executed in place
2. eg : square2 = lambda *num*:*num* * *num*
3. PAss a function into another function which would not be usd again. 


**MAP**
1. accepts 2 arguments
2. Requires an iterable
3. eg : double = map(lambda x: x*2,nums)
4. These objects can be iterated only once.

**FILTER**
1. filters a particular item based on condition
2. Used with lambda functions
3. eg : even = list(filter(lambda x : x%2==0, input))

**ANY AND ALL**
1. ALL - Return true if all elements in the iterable are truthy.
    eg : people=["supreetha","s","bhatt]
            all([peop[0] == 's' for peop in people]) --> retruns false since one of the values are false.
2. ANY - Return true if any elements in the iterable are truthy.
    eg: people=["supreetha","s","bhatt]
            all([peop[0] == 's' for peop in people]) --> retruns true since one of the values are false.


**Sorted**
1. Works with other iterable other than list.
2. syntax --> sorted(variable,key = lambda user:user['usrname'])

**zip**

**len**
- the built in function used to find the object length,
- len('hi') --> returs 2
- can be used to pass objects also

**abs**
- takes the numberic value without the negative value
- any negative value is turned to +ve
- abs(-3) --> 3
- cannot be used with strings

**fabs**
- import math
- converts everything to float first
-  math.fabs(-4) ---> 4.0

**sum**
- starts at left and goes to the end , takesan optional start.
- starts with 0
- sum(iterable[,start])


**reversed**
- another form of reverse
- used for tuple, dict, list unlike reverse which is used only on list
- list(reversed.dunder())


**round**
- returns the rounded digit to the specified number , if not gives the integer.

**zip**
- list(zip([1,2,3],[4,5,6]))----> [(1,4),(2,5),(3,6)]
- dict(zip([1,2,3],[4,5,6])) --> {1:4,2:5,3:6}