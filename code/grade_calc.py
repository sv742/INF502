

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
