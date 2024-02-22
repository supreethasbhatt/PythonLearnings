**Common type of errors**
1. syntax errors --> missing colons
2. NameError --> when the variable is not defined
3. TypeError --> Mismatch of data types
4. IndexError --> list
5. KeyError --> No key present
6. AttributeError --> Variable does not have attribute



**Raising own errors**
1. This can be used to throe errors using the **Raise** key word. 
2. This is helpful when creating your own kind of exception and error message
3. raise ValueError("blah")

**Handle Errors**
1. When there is an error encountered, the entire issue is stopped. Thus to overcome this, errors have to be handld
2.  try:
        code
    except:
        print("problm")
    print("after try")
3. Except : Nameerror, typeError etc.
4. try:
        code
    except:
        runs only when an error is encountered
    else:
        runs only when the try code turns out to be true.
    finally:
        Runs no matter what.

**pdb**
1. used to debug python debugger
2. ITs a module whihc has to be imported. 
3. import pdb. pdb.set_trace() on the line where you feel the issue exists