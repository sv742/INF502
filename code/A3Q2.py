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
