def list_mangler(list_in):

    '''
        Input: list_in: a list of integers
        
        Output: list_in_mod: the list with modified elements
    '''

    #create a new list to store modified elements
    list_in_mod = list()

    #we first traverse the list element by element
    #if the element is an even number, we double it
    #if the element is an odd number, we triple it

    for element in list_in:

        #using modulus operator for checking even odd
        #if remainder with 2 is 0, element is even
        if element % 2 == 0:

            element += element #double the element
        
        else:

            element += element + element #triple the element

        list_in_mod.append(element)

    #return the modified list
    return list_in_mod

if __name__ == "__main__":

    #call the function
    print(list_mangler([1, 2, 3, 4]))
    print(list_mangler([1, 3, 5, 7, 9]))
    print(list_mangler([2, 4, 6, 8, 10]))
    print(list_mangler([2, 3, 2, 3]))
