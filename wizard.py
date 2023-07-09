class Wizard:
    def __init__(self, name) -> None:
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizard):
    def __init__(self, name: str, house: str) -> None:
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name: str, subject: str) -> None:
        super().__init__(name)
        self.subject = subject


harry = Student("Harry", "Gryffindor")
print(f"{harry.name} is from {harry.house}")
professor = Professor("Severus", "Defense against dark spells")
