**What are functions**
1. a process for executing a task
2. reusable piece of code
3. it can accept input and output
4. DRY - Dont Repeat Yourself


**Syntax**
1. def name_of_function():
        code xxx

    name_of_function()

2. retruning vales;
    - exits the function
    - use tuple to return more than one values

3. Parameters:
    - inputs given to the function. Can be more than 1
    - def function_name(param)

4. default parameters:
    - used to pass default values to the paramaeters when no argument is passed on to the function.
    - def func_name(param=default_Value)
    - these default parameters can be any values - list, dicts, tuples, sets or ven other funtions!
    - only the order has to be matched.

5. Keyword Arguments:
    - ued to specify the parameters and values
    - eg : 
    def function_name(y,x):
        code
    function_name(x=1,y=2)

6. Scope:
    - global scope
    - function scope

7. Documenting:
    - def fnction_name():
        """ enter the message """
        code
    
     print(fnction_name().__doc__) ----> This will add the function definition


**MISC and IMP**
1. * ---> *args --> gathers the  arguments into tuples and passes it to the function. This avoids specifying how many parameters have to be passed. 
    eg : def fun_name(*args):
            code
        func_name(1,2,3)
        func_name(2)

2. ** ---> **kwargs --> gather remaining keyword args as a dictionary.
    eg: def fav_colours(**kwargs):
            code
        fav_colour(sup="sup",rub="red")

3. parameter ordering should be like below when there are multiple parameters involved:
    a. parameter
    b. *args
    c. default parameters
    d. **kwargs

    eg: def display_info(a,b,*args,instructor = 'sup', **kwargs)

**Tuples Unpacking**
1. *args --> unpacks the values
2. works with tuples and liste
3. USed when calling the function.
4. eg:
    def function_1(*args):
        code
    
    num=[1,2,3,4]
    nums=(1,2,3,4)
    function_1(*num) ---->if *num is not passed, the argument passed would be considered as ([1,2,3,4],) and would throw rror
    function_1(*num)

**Dictionary Unpacking**
1. **kwargs --> Unpack dictionary into key word arguments
2. used when calling functions containing dictionaries
3. eg:
    def function_1(**kwargs):
        code
    
    num={"first":"colt","last":"Sup"}
    function_1(**num) ---->if *num is not passed, the argument passed would be considered as disctionary and would throw rror
