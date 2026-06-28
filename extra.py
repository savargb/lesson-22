#Write a program to create a class Dog and perform the following tasks:
#Create a class variable species.
#Create an __init__() method with instance variables name and breed.
#Create two objects of the Dog class by passing values.
#Print the class variable by accessing it.
#Print the instance variables of both objects.

class Dog:
    species = "Mammal"

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Luna", "German Shepherd")

print(Dog.species)

print(dog1.name, dog1.breed)
print(dog2.name, dog2.breed)




        