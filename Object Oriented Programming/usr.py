class User:
    
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self. sex = sex

    def usr_info(self):
        return f"{self.name}"
    
    def like(self,thing):
        return f"{self.name} likes {thing}"


user1 = User("supreetha",29,"f")
print(user1.name)
print(user1.age)
print(user1.sex)
print(user1.usr_info())
print(user1.like("ice cream"))