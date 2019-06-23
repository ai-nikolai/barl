####################################################
#
# This Work is written by Nikolai Rozanov <nikolai>
#
# Contact:  nikolai.rozanov@gmail.com
#
# Copyright (C) 2018-Present Nikolai Rozanov
#
####################################################

####################################################
# IMPORT STATEMENTS
####################################################

# >>>>>>  Native Imports  <<<<<<<
import timeit

# >>>>>>  Package Imports <<<<<<<
import numpy as np

# >>>>>>  Local Imports   <<<<<<<


####################################################
# CODE
####################################################

def generate_random_non_zero_matrix(size = [10,10]):
    """
    """
    return np.random.choice( 100 , size) + 1



def divide_matrices_vector_form(matrix1, matrix2):
    """
    generates random matrices and then div
    """
    matrix1 = matrix1/matrix2

    return matrix1


def divide_matrices_loop(matrix1, matrix2):
    """
    generates random matrices and then div
    """
    for idx in range(matrix1.shape[0]):
        for jdx in range(matrix1.shape[1]):
            matrix1[idx,jdx] /= matrix2[idx,jdx]

    return matrix1


####################################################
# MAIN
####################################################

if __name__ == "__main__":
    mat1 = generate_random_non_zero_matrix()
    mat2 = generate_random_non_zero_matrix()

    print( timeit.timeit('divide_matrices_vector_form(mat1,mat2)', globals=globals(), number=10000) )
    print( timeit.timeit('divide_matrices_loop(mat1,mat2)', globals=globals(), number=10000) )

# EOF
