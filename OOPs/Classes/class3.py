class Dog:
    species="Canine"
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
dog1=Dog("Bud",3)
dog2=Dog("reag",3)

print(dog1.species)
print(dog1.name)
print(dog2.name)

dog1.name="Max"
print(dog1.name)

Dog.species="Feline"
print(dog1.species)
print(dog2.species)