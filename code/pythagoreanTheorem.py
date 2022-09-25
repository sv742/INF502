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
