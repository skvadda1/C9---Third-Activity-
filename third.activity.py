class Parrot:
    species = "bird"

    def __init__(self,name,age):
        self_name = name
        self_age = age

blu = Parrot("Blu" , 10)
woo = Parrot("Woo" , 15)

print("Blu is a {}".format(blu.species))
print("Woo is also a species".format(woo.species))
