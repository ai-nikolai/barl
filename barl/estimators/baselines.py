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

from .interfaces import BaseEstimator
####################################################
# CODE
####################################################

class EmpiricalMean(BaseEstimator):
    """
    Estimating 1D Vectors
    """
    def __init__(self, size):
        assert len(size) < 2, "EmpiricalMean only does 1D estimates at the moment"
        self.__mean = np.zeros(size)
        self.__value = np.zeros(size)
        self.__count = np.zeros(size)
        self.__shape = self.__value.shape


    def update( self , newValueOrList, indexList=None):
        """
        updates the mean
        Can update from ListOf Values and List of Indexes

        """
        newValue = self.__deal_with_valueList( newValueOrList, indexList )
        oneHotIndexList = self.__deal_with_index( indexList )

        if newValue.shape == self.__shape:
            self.__update_single_value(newValue, oneHotIndexList)



        elif (newValue.ndim == self.__value.ndim+1) and (newValue.shape[1]==self.__value.shape[0]):
            self.__update_multiple_values(newValue, oneHotIndexList)

        self.__mean = np.divide(self.__value, self.__count, where=self.__count>0)



    def get_estimate(self):
        """
        returns the current estimate (of the mean)
        """
        return self.__mean





    def __update_single_value(self, newValue, oneHotIndexList=None):
        """
        updates a single value
        """
        if type(oneHotIndexList)==type(None):
            where = True
        else:
            where = oneHotIndexList

        self.__value = np.add( self.__value, newValue, where=where>0 )

        self.__count += where




    def __update_multiple_values(self, newValue, oneHotIndexList=None):
        """
        updates multiple values
        """
        if type(oneHotIndexList) == type(None):
            self.__count += newValue.shape[0]

        else:
            self.__count += np.sum( oneHotIndexList, axis=0 )

        self.__value += np.sum( newValue, axis=0 )




    def __deal_with_valueList(self, values, index=None):
        """
        creates valued one hot or does nothing
        """

        if type(index) == type(None):
            outValues = np.array(values)
        else:
            outValues = numerical.transform_to_valued_one_hot(listOfValues=values,listOfIndexes=index, numClasses=self.__value.shape[0])

        return outValues




    def __deal_with_index(self,index=None):
        """
        creates a one shot or returns None
        """
        if type(index) == type(None):
            return None
        else:
            outIndex = numerical.transform_to_one_hot(index, numClasses=self.__value.shape[0])
            return outIndex








####################################################
# MAIN
####################################################


# EOF
