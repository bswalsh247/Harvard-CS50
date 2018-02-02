import cs50
import sys

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument or have too many")
        exit(1)
    else:
        k = int(sys.argv[1])

        print("plaintext: ", end="")
        p = cs50.get_string()

        print("ciphertext: ", end="")

    if p != None:
        for c in p:
            if c.isalpha():
                if c.islower():
                    new_c = ((ord(c) - 97) + k) % 26 + 97
                    j = chr(new_c)
                    print(j, end="")
                else:
                    new_c = ((ord(c) - 65 ) + k) % 26 + 65
                    j = chr(new_c)
                    print(j, end="")
            else:
                print(c, end="")
        print()
        exit(0)


if __name__ == "__main__":
    main()