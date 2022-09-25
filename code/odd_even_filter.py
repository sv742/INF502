
def odd_even_filter(numbers):

    '''
        Input: numbers: a list of integers

        Output: filtered_numbers: a list containing two sublists of even and odd numbers (separately) from the given list
    
    '''

    #fist, create two lists for containing even and odd numbers respectively
    even_nums = list()
    odd_nums = list()

    #now create a final list that will contain the above two sublists
    filtered_list = list()

    #traverse the original list and filter the numbers
    #use mod 2 for checking even and odd numbers
    #place in respective lists

    for number in numbers:

        if number % 2 == 0:

            even_nums.append(number)

        else:

            odd_nums.append(number)

    #now, append the even and odd list to the main list
    filtered_list.append(even_nums)    
    filtered_list.append(odd_nums)

    #return the final list
    return filtered_list    

if __name__ == "__main__":

    print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(odd_even_filter([3, 9, 43, 7]))
    print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56]))
