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

class EmpiricalMean(object):
    """
    Estimating 1D Vectors
    """
    def __init__(self, size):
        assert len(size) < 2, "EmpiricalMean only does 1D estimates at the moment"
        self.__value = np.zeros(size)
        self.__count = np.zeros(size)

        self.__shape = self.__value.shape



    def update( self , newValue, oneHotIndexList=None):
        """
        updates the mean
        """

        #if they are the same size
        if newValue.shape == self.__shape:
            where = oneHotIndexList if oneHotIndexList else True
            self.__value = np.add( self.__value, newValue, where=where )

        #if newValue is multiple values at once
        elif (newValue.ndim == self.value.ndim+1) and (newValue.shape[0]==self.value.shape[0]):

            if oneHotIndexList:
                self.count += np.sum( oneHotIndexList, axis=1 )

            else:
                self.count += newValue.shape[1]

            self.value += np.sum( newValue, axis=1 )

        self.mean = np.divide(self.value, self.count, where=self.count)



    def get_estimate(self):
        """
        returns the current estimate (of the mean)
        """
        return self.mean








####################################################
# MAIN
####################################################


# EOF
