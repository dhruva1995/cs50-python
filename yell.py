def main():
    yell(*"This is Dhruva".split(" "))


def yell(*words):
    uppercased = (word.upper() for word in words)
    print(*uppercased)


if __name__ == "__main__":
    main()
