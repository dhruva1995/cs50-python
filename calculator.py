def main():
    x = int(input("What's x? "))
    print(f"x squared is {square(x)}")


def square(num: int) -> int:
    return num * num


if __name__ == "__main__":
    main()
