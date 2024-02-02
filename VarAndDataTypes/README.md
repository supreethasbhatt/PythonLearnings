This is a section which talks about the different data types and the variables

Variables: named symbol that Hold values

x = 100
y="supreetha"

Naming restriction for variables:
1. letter or underscores
2. cannot contain special characters
3. variables are case sensitive

Naming conventions:
1. Use snake_case
2. most variables should be variables
3. constants should be capital( CAPITAL_SNAKE_CASE)
4. UpperCamelCase refer to class
5. Variables starting with 2 undescores are called dunders(double underscores) which are private and are left alone. Eg: __no_touchy__, __main__,__name__

Data types:
Every assignment should be a common data type.
1. bool - True/False : 0/1
2. int - 1,2,3
3. str - 'a','b','c'..
4. list - collection of data types of same values [1,2,3],['a','b','c'] <data structure>
5. dict - key value pairs - {'a':1,'b':2,'c':3,'d':a} <data structure>

Python is a dynamically typed language. Why?
>> highly flexible in reassigning the videos.

Statically typed --> C++

Value "None" --> just to represent null.  class <NoneType>

Escape sequences : back slash --> https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences

String Formatting:
~~~~~~~~~~~~~~~~~~~~
1. f-string : f"This is what number {number} looks like" - where numner is int
2. format method : "This is what number {} looks like".format(number)
3. deprecated : "This is what number %d looks like" %(number)

Strings and indexes:
~~~~~~~~~~~~~~~~~~~~
individual letter in the strings can be accessed by indices starting with 0.

Eg: 
x="supreetha"
x[0] = s
x[1] = u
x[-1] = a

Converting Data types:
~~~~~~~~~~~~~~~~~~~~~~~~
explicitly call the type of the fata type.
my_list = [1,2,3]
my_list_str = str(my_list)


Ask user input 
~~~~~~~~~~~~~~~
input

eg:
name input = input()