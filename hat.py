from random import choice


class Hat:
    houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]

    @classmethod
    def sort(cls, name):
        print(f"{name} is in {choice(cls.houses)}")


Hat.sort("Ron")
