class Dog:
    species="Canine"
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

dog1=Dog("Buddy",3)
dog2=Dog("Rock",4)

print(dog1.name,dog1.age,dog1.species)
print(dog2.name,dog2.age,dog2.species)
print(Dog.species)
