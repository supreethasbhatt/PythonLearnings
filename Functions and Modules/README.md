**What are functions**
1. a process for executing a task
2. reusable piece of code
3. it can accept input and output
4. DRY - Dont Repeat Yourself


**syntax**
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