**What is module**
1. used to keep the python files small
2. reuse across multiple files by importing

**Buil-in Module**
1. something already presented by module.
2. eh: random
3. import random
    random.choice([list])
    random.randint([list])
    random.shuffle([list])
4. aliasing can be used as well, 
    eg: import random as r
5. from random import randint.
    -- from can be used to import a particualr function from the moodule
6. syntax:
    import random
    import random as r
    from random import randint
    from random import randint as ra, shuffle as sh

**Custom Modules**
1. write your own cide which can be imported.
2. eg:
    file1.py
    def fn():
        return "do some stuff"
    def other_func():
        return "do other stuf"

    file2.py
    import file1

    fn()


**