class Student:
    def __init__(self, name: str, house: str) -> None:
        if not name:
            raise ValueError("Student name is empty")
        self.name = name
        self.house = house

    def __str__(self) -> str:
        return f"{self.name} is from {self.house}"

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("Invalid House")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    return Student(input("Name: "), input("House: "))


if __name__ == "__main__":
    main()
