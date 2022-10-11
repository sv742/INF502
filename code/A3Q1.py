def add_wallet(wallets):

    value = int(input("Enter Wallet Value: "))

    wallets.append(value)

    return wallets

def add_value_to_wallet(wallets):

    wallet = int(input("Enter wallet number: "))
    value = int(input("Enter Wallet Value: "))
    
    if wallet > len(wallets):

        print("Not enough wallets!")
        return wallets
    
    wallets[wallet - 1] += value
    return wallets

def main():

    wallets = []

    while True:

        print("1. Add Wallet")
        print("2. Add Value to Wallet")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            wallets = add_wallet(wallets)

        elif choice == 2:

            wallets = add_value_to_wallet(wallets)
        
        else:

            break


        print("\nThe fattest wallet has ", max(wallets), " in it.")
        print("The skinniest wallet has ", min(wallets), " in it.")
        print("All together, these wallets have ", sum(wallets), " in them.")
        print("All together, the total value of these wallets is worth ", sum(wallets) * 10, " dimes.\n")


if __name__ == "__main__":

    main()
