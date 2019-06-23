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


####################################################
# CODE
####################################################

def one_hot(listOfIndexes, numClasses):
    """
    returns [[0,0,1,...],...]
    """
    idxes = np.array( listOfIndexes )

    return np.eye( numClasses )[ idxes.reshape(-1) ]


def transform_to_one_hot(listOfIndexes, numClasses):
    """
    transforms a listOfIndexes into oneHot
    """
    return np.squeeze( one_hot(listOfIndexes, numClasses) )



def transform_to_valued_one_hot(listOfValues, listOfIndexes, numClasses):
    """
    transforms list of values and indexes to valued one-hot
    """
    vals = np.array(listOfValues)

    oneHots = one_hot(listOfIndexes, numClasses)

    vOneHots = oneHots * vals.reshape(-1,1)

    return np.squeeze( vOneHots )





####################################################
# MAIN
####################################################


# EOF
