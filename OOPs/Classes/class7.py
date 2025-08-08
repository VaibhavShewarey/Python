from abc import ABC,abstractmethod

class Dog(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def sound(self):
        pass
    def display_name(self):
        print(f"Dog's name:{self.name}")
        
        
class Labrador(Dog):
    def sound(self):
        print("Labrador Woof!")
        
class Beagle(Dog):
    def sound(self):
        print("Beagle Bark!")
        
dogs=[Labrador("Budd"),Beagle("Charlie")]
for dog in dogs:
    dog.display_name()
    dog.sound()