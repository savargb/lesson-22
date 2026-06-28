class Parrot:

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

Blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

print("Clu is a {}".format(Blu.species))
print("Woo is a {}".format(woo.species))

print("{} is {}".format(Blu.name, Blu.age))
print("{} is {}".format(woo.name, woo.age))
        