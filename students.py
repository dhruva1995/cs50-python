import csv

students = []

with open("students.csv") as file:
    for row in csv.DictReader(file):
        students.append(row)

for student in students:
    name, place = student["name"], student["place"]
    print(f"{name} is from {place}")
