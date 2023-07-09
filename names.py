# name = input("What is your name? ")

# with open("names.txt", "a") as file:
#     file.write(name + "\n")

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print("Hello,", name)
