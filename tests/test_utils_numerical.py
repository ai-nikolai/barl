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

# >>>>>>  Package Imports <<<<<<<
import numpy as np

# >>>>>>  Local Imports   <<<<<<<
from barl.utils import numerical

####################################################
# CODE
####################################################

def test_one_hot_works():
    #TODO, put it into conftest
    numClasses = 3

    testIdx = 2
    testVec = [0,0,1]

    testIdx2 = [0,2,2,1]
    testVec2 = [[1,0,0],[0,0,1],[0,0,1],[0,1,0]]

    out1 = numerical.transform_to_one_hot(testIdx, numClasses)
    assert np.array_equal(out1,testVec), "One Hot 1"

    out2 = numerical.transform_to_one_hot(testIdx2, numClasses)
    assert np.array_equal(out2,testVec2), "One Hot 2"


def test_valued_one_hot_works():
    #TODO, put it into conftest
    numClasses = 3

    value = 5
    testIdx = 2
    testVec = [0,0,5]

    values2 = [1,2,3,4]
    testIdx2 = [0,2,2,1]
    testVec2 = [[1,0,0],[0,0,2],[0,0,3],[0,4,0]]

    out1 = numerical.transform_to_valued_one_hot(value, testIdx, numClasses)
    assert np.array_equal(out1,testVec), "One Hot 1 V."

    out2 = numerical.transform_to_valued_one_hot(values2, testIdx2, numClasses)
    assert np.array_equal(out2,testVec2), "One Hot 2 V."

####################################################
# MAIN
####################################################

if __name__=="__main__":
    numClasses = 3

    testIdx = 2
    testVec = [0,0,1]

    testIdx2 = [0,2,2,1]
    testVec2 = [[1,0,0],[0,0,1],[0,0,1],[0,1,0]]

    out1 = numerical.transform_to_one_hot(testIdx, numClasses)
    out2 = numerical.transform_to_one_hot(testIdx2, numClasses)

    print(out1)
    print(out2)

# EOF
