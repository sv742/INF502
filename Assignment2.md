# Assignment 2: Python Basics
## Problems

**1. Write a function with the following signature:** `pythagoreanTheorem(length_a, length_b)`.

The function returns the length of the hypotenuse assuming that `length_a` and `length_b` are the lengths of the two legs of a right triangle (the legs that form the triangle's right angle). Hint: the `math` module might have useful functions to use.

For example:
```python
print(pythagoreanTheorem(2, 2))
2.8284271247461903
```

## Solution:

```python
import math

def pythagoreanTheorem(length_a, length_b):

    '''
        Input: length_a: length of side adjacent to the base
               length_b: length of the base of the triangle
        
        Output: hyp: length of the hypotenuse in relative units
               
    
    '''

    #we know that hypotenuse is equal to the square root of sum of squares of base and adjacent sides
    #matehmetically, h = squareroot(length_a^2 + length_b^2)

    #squaring length_a
    length_a_sq = math.pow(length_a, 2)

    #squaring length_b
    length_b_sq = pow(length_b, 2)

    #square rooting
    hyp = math.sqrt(length_a_sq + length_b_sq)

    return hyp


if __name__ == "__main__":

    print(pythagoreanTheorem(2,2))
    print(pythagoreanTheorem(3,2))
    print(pythagoreanTheorem(3,3))
    print(pythagoreanTheorem(3,4))

```

## Output:

```

2.8284271247461903
3.605551275463989
4.242640687119285
5.0

```

[Code Link](https://github.com/sv742/INF502/blob/main/code/pythagoreanTheorem.py)

**2. Write a function with the following signature:** `list_mangler(list_in)`.

The function assumes that `list_in` is a list of integers, and returns a new list containing transformed elements of `list_in`. If the element is even, it's doubled. If the element is odd, it's tripled.

For example:

```python
print(list_mangler([1, 2, 3, 4]))
[3, 4, 9, 8]
```

## Solution:

```python
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

```

## Output:
```
[3, 4, 9, 8]
[3, 9, 15, 21, 27]
[4, 8, 12, 16, 20]
[4, 9, 4, 9]

```
[Code Link](https://github.com/sv742/INF502/blob/main/code/list_mangler.py)

**3. Write a function with the following signature:** `grade_calc(grades_in, to_drop)`.

The function accepts a list `grades_in` containing integer grades, drops the `to_drop` lowest grades (so, for `to_drop` equal to 2, the function should drop the 2 lowest grades), calculates the average of the grades left, and returns the letter grade this average corresponds to according to the letter grade scale for this course.

For example:

```
print(grade_calc([100, 90, 80, 95], 2)) # drops the 2 lowest grades (80 and 90)
'A'
```
## Solution:

```python


def grade_calc(grades_in, to_drop):

    '''
        Input: grades_in: a list containing integer grades
               to_drop: number of lowest grades to drop

        Output: letter_grade: the grade according to calculated average

    '''

    #first check if the list has enough grades to drop
    if len(grades_in) < to_drop:

        print("Not enough grades to drop!")
        return 

    #first sort the list from lowest to highest grades
    #it will make it easy to drop the lowest k
    grades_in.sort()

    #now loop for to_drop times, and drop the top most element
    #Each time the lowest element will occupy the lowest space in the sorted list
    grades_in.pop(0) #removes the element at the 0th place. 

    #now let's calculate the average of the remaining courses
    #use sum by count
    avg = sum(grades_in) / len(grades_in)

    letter_grade = ''

    #set the letter grade based on average

    if avg >= 90:

        letter_grade = 'A'
    
    elif avg >= 80:

        letter_grade = 'B'

    elif avg >= 70:

        letter_grade = 'C'
    
    elif avg >= 60:

        letter_grade = 'D'

    else:

        letter_grade = 'F'

    return letter_grade

if __name__ == "__main__":

    print(grade_calc([100, 90, 80, 95], 2))
    print(grade_calc([80, 70, 80, 95], 2))
    print(grade_calc([100, 20, 80, 95], 1))
    print(grade_calc([60, 40, 80, 95], 3))

```

## Output: 

```python

>grade_calc([100, 90, 80, 95], 2)
A

>grade_calc([80, 70, 80, 95], 2)
B

>grade_calc([100, 20, 80, 95], 1)
A

>grade_calc([60, 40, 80, 95], 3)
C

```

[Code Link](https://github.com/sv742/INF502/blob/main/code/grade_calc.py)

**4. Write a function with the following signature:** `odd_even_filter(numbers)`.

The function accepts an input list of integers and returns a list with two sublists. The first sublist contains all even numbers in the input list and the second sublist contains all odd numbers.

For example:
```
print(odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9]))
[[2, 4, 6, 8], [1, 3, 5, 7, 9]]
print(odd_even_filter([3, 9, 43, 7]))
[[], [3, 9, 43, 7]]
print(odd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56]))
[[98, 50, 90, 2, 56], [71, 39, 79, 5, 89]]
```

## Solution:

```python


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

    print(odd_even_filter([5, 2, 1, 6, 8, 3, 6, 8, 7]))
    print(odd_even_filter([1, 2, 4 ,5, 7, 6, 12, 63, 12, 5]))
    print(odd_even_filter([92, 12, 45, 12, 64, 74, 12, 2, 3]))
    print(odd_even_filter([1, 1, 1, 1, 2, 2, 2, 2]))
    print(odd_even_filter([1, 1, 1, 1]))


```

## Output:


```
[[2, 6, 8, 6, 8], [5, 1, 3, 7]]
[[2, 4, 6, 12, 12], [1, 5, 7, 63, 5]]
[[92, 12, 12, 64, 74, 12, 2], [45, 3]]
[[2, 2, 2, 2], [1, 1, 1, 1]]
[[], [1, 1, 1, 1]]

```

[Code Link](https://github.com/sv742/INF502/blob/main/code/odd_even_filter.py)
