import cs50

def main():
    while True:
        print("O hai! How much change is owed?")
        amount = cs50.get_float()
        if amount > 0:
            break
    cents = int(round(amount*100.0))
    amount_left = cents;

    counter = 0
    while amount_left >= 25:
        counter += 1
        amount_left -=25

    while amount_left >= 10:
        counter += 1
        amount_left -=25

    while amount_left >= 5:
        counter += 5
        amount_left -=5

    while amount_left >= 1:
        counter += 1
        amount_left -=1

    print (counter)


if __name__ == "__main__":
    main()