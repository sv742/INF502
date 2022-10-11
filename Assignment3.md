# Assignment 3: Python Basics
## Problems

**Problem 1: Wallets**

Write a Python program that request a user to provide numbers representing the value in cash for different wallets. Your program should store these values in a list. The user should be able to add as many values as they want. One example of a filled wallets list (in this example, with 5 wallets) would be:

For example:
```python
print(wallets)

Output: [1023, 984, 192, 1842, 12]
```

After the user adds the values for the wallets, your application should provide the following information:

The fattest wallet has $value in it.
The skinniest wallet has $value in it.
All together, these wallets have $value in them.
All together, the total value of these wallets is worth $value dimes.
Please try to think about different functions to complete your work.

## Solution:

```python
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
```

[Code Link](https://github.com/sv742/INF502/blob/main/code/pythagoreanTheorem.py)

**Problem 2: Periodic Table**

The Periodic Table of the Elements was developed to organize information about the elements that make up the Universe. Write a terminal application that lets you enter information about each element in the periodic table. Make sure you include the following information:

symbol, name, atomic number, row, and column
You must save the elements in a dictionary where the symbol is the key and the other attributes are nested inside symbol. The nested keys are name, number, row, column.

To populate your dictionary with data, provide a menu of options to the users:

Search the element by symbol (see all the details).
Search by a property (name, number, row, column) and see the values for that property for all the elements in the table.
Enter a new element manually (type the information for each property)
Change the properties of an element (by symbol)
Export periodic table as a JSON file
Load periodic table from JSON file
Exit the program
Make sure you do the appropriate communication with the user to get the necessary information to complete each step.

## Solution:

```python
import json 

def add_to_table(table):

    sym = input("Enter Symbol: ")

    if sym in table.keys():

        print("Element with given symbol already exists!")
    
    else:

        name = input("Name of element: ")
        at_num = int(input("Atomic Number of Element: "))
        row = int(input("Row in table: "))
        col = int(input("Column in table: "))

        table[sym] = [name, at_num, row, col]
    
    return table

def search_by_symbol(table):

    sym = input("Enter Symbol: ")
    
    if sym not in table.keys():
        
        print("No such symbol found!")
        return
    
    print("Name: ", table[sym][0])
    print("Atomic Number: ", table[sym][1])
    print("Row: ", table[sym][2])
    print("Column: ", table[sym][3])

    return table[sym]

def change_property(table):

    sym = input("Enter Symbol: ")
    
    if sym not in table.keys():
        
        print("No such symbol found!")
        return

    name = input("Name of element: ")
    at_num = int(input("Atomic Number of Element: "))
    row = int(input("Row in table: "))
    col = int(input("Column in table: "))

    table[sym] = [name, at_num, row, col]



def search_by_property(table):

    print('1. Name')
    print('2. Atomic Number')
    print('3. Row')
    print('4. Column')

    choice = int(input("Enter Choice: "))

    if choice == 1:

        name = input("Enter Name: ")

        for i in table.values():

            if name in i:
                print("Found: ", i)
                print()

        print("Other elements with same name:")

        for i in table.values():

            print(i[0])

    elif choice == 2:
    
        num = input("Atomic Number: ")

        for i in table.values():

            if num in i:
                print("Found: ", i)
                print()

        print("Other elements with same atomic number:")

        for i in table.values():

            print(i[1])

    elif choice == 3:

        row = input("Enter row: ")

        for i in table.values():

            if row in i:
                print("Found: ", i)
                print()

        print("Other elements with same row:")

        for i in table.values():

            print(i[2])


    elif choice == 4:
        
        col = input("Enter column: ")

        for i in table.values():

            if col in i:
                print("Found: ", i)
                print()

        print("Other elements with same columns:")
        
        for i in table.values():

            print(i[3])

def export_to_JSON(table):

    fn = input("Enter a name for JSON file: ")

    with open(fn, "w") as outfile:
        json.dump(table, outfile)

def load_from_JSON():

    fc = input("Enter JSON filename: ")
    fc = open(fc)
    fc = fc.read()

    table = json.loads(fc)

    #fc.close()

    return table

def main():

    table = dict()

    while True:

        print("1. Search element by symbol")
        print("2. Search element by property")
        print("3. Enter element manually")
        print("4. Change element properties by symbol")
        print("5. Export to JSON file")
        print("6. Load from JSON file")
        print("7. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:

            search_by_symbol(table)

        elif choice == 2:

            search_by_property(table)

        elif choice == 3:

            table = add_to_table(table)

        elif choice == 4:

            table = change_property(table)
        
        elif choice == 5:

            export_to_JSON(table)
        
        elif choice == 6:

            table = load_from_JSON()

        elif choice == 7:
            
            break


if __name__ == "__main__":

    main()
```

[Code Link](https://github.com/sv742/INF502/blob/main/code/list_mangler.py)
