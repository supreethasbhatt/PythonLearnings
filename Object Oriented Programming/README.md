**What is OOP?**
1. Using code to recreate things in the world.
2. This is done using classes and objects


**Classes**
1. blueprints/recepies
2. IT can contain methods(functions) and attributes(name,or keys of dicts)
3. **instance** --> Objects that are constructed from a class blueprin that contain their classes's methods and properties

**private attributes**
1. the attributes which do not need to exposed to the outside world.
2. _cards --> synatx to make the list of cards private

Syntax:
---------
class User:
    pass

user1 = User()
-------------

**init method**
1. python automatically looks at this
2. This method is automatically called everytime when an object is instantiated 
3. self indicates the specific keyword that initiates an object

Syntax:
---------
class User:
    
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self. sex = sex

    def usr_info(self):
        return f"{self.name}"


user1 = User("supreetha",29,"f")
print(user1.name)
print(user1.age)
print(user1.sex)
print(user1.usr_info())
-------------

**Dunder MEthods/Name Mangling**
1. used with special cases only when we are overwriting that already exists in python. 
2. eg : __init__

3. _name ----> private attribute, not be used outside the class. 
4. __name ---> name mangling ---> to acceess --> _Classname__attribute. ---> This is generally used with inheritence.

**Class Attributes**
1. The attributes defined by the class are shared nby all the instances within the class

Sntax:
class User:
    
    active_user = 0                                                             -------> class attribute
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self. sex = sex
        User.active_user = active_user +1
        
    def logout():
        User.active_user -=1
        return f"{self.first} has logged out"

    def usr_info(self):
        return f"{self.name}"


user1 = User("supreetha",29,"f")
print(user1.name)
print(user1.age)
print(user1.sex)
print(user1.usr_info())
print(User.active_user)                                            -------> Ref to ClassName.class attribute

**Class MEthods**
1. @classmethod decorator
2. Associated with the class itself and not instance.
3. instead of self, slf/cls is passed as parameter
4. called using Class_name.@classmethod


**__repr__** :
1. representation method
2. Represents the class instance as a string.


**Inheritance**
1. Pull code from a part of another code.
2. Syntax:
    class PArent:
        code
    class child(Pasrent):
        code
3. **super** --> used to inherit attributes from the parent class. 
    eg:
        class Animal:

                def __init__(self,name,species):
                    self.name = name
                    slf.species = species

                def __repr__(self):
                    print f{se;f.name} is a {self.species}"

        class Cat(Animal):

                def __init__(self,name,species,breed,toy):
                    super().__init__(name,species)
                    self.breead = breed
                    self.toy = toy

**@properties, @method.setter**
1. Used to call class methods like without parenthesis

 