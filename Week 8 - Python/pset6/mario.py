import cs50

def main():
    while True:
        print("Height: ", end="")
        height = cs50.get_int()
        if height > 0 and height < 23:
            break

    for row in range(1, height + 1):
        for space in range(height - row):
            print(" ", end="")
        for space in range(row + 1):
            print("#", end="")
        print()

if __name__ == "__main__":
    main()

