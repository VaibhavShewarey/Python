class Dog:
    def __init__(self,name):
        self.name=name
        
    def display_name(self):
        print("Dog's name: {self.name}")
        
class Labrador(Dog):
    def sound(self):
        print("Labrador woofs")
        
class GuideDog(Labrador):
    def guide(self):
        print(f"{self.name}Guides the way")
        
class Friendly:
    def greet(self):
        print("Friendly!")
        
class GoldenRetriever(Dog,Friendly):
    def sound(self):
        print("Golden Retriever Brake")
        
lab=Labrador("Bud")
lab.display_name()
lab.sound()

guide_dog=GuideDog("Max")
guide_dog.display_name()
guide_dog.guide()

retriever=GoldenRetriever("Reag")
retriever.display_name()
retriever.greet()
retriever.sound()