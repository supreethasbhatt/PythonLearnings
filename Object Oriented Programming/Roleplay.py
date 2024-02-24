class Character:
    
    def __init__(self,name,hp,level):
        self.name = name
        self.hp = hp
        self.level = level
    
    
class NPC(Character):

    def __init__(self,name,hp,level):
        
        super().__init__(name,hp,level)
        
    def __repr__(self):
        return f"{self.name} is at {self.level} haveing {self.hp} points"
        
    def speak(self):
        return f"{self.name} says: 'I heard monsters running around last night!'"

villager = NPC("Bob", 100, 12)
print(villager.name)
print(villager.hp)
print(villager.level)
print(villager)         #returns the class as string.
print(villager.speak())
