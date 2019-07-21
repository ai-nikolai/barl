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

from .interfaces import BaseBayesianEstimator
####################################################
# CODE
####################################################


class NormalMean(BaseBayesianEstimator):
    """
    Estimating 1D Vectors
    """
    def __init__(self, size, initialVariance=3.0, samplingVariance=0.1):
        assert len(size) < 2, "EmpiricalMean only does 1D estimates at the moment"

        self.__means  = np.zeros(size)
        self.__variances = np.ones(size) * initialVariance
        self.__sampling_variances = np.ones(size) * samplingVariance

        self.__shape = self.__means.shape
        self.__ndim = self.__means.ndim

    def __str__(self):
        """
        Represents the empricial mean as a string
        """
        outStr = "Means: " + str(self.__means) + '\n' + "Variances: " + str(self.__variances)
        return outStr

    def update( self , newValueOrList, indexList=None):
        """
        updates the mean
        Can update from ListOf Values and List of Indexes

        """
        newValue = self.__deal_with_valueList( newValueOrList, indexList )
        oneHotIndexList = self.__deal_with_index( indexList )

        if newValue.shape == self.__shape:
            self.__update_single_value(newValue, oneHotIndexList)

        elif (newValue.ndim == self.__ndim+1) and (newValue.shape[1]==self.__shape[0]):
            self.__update_multiple_values(newValue, oneHotIndexList)




    def get_estimate(self, returnVariances=False):
        """
        returns the current estimate (of the mean)
        """
        if returnVariances:
            return self.__means, self.__variances

        else:
            return self.__means



    def sample(self):
        """
        returns the current estimate (of the mean)
        """
        # sampling the means
        samplingMeans = np.random.multivariate_normal( mean=self.__means, cov=np.diag(self.__variances) )

        # sampling the estimate
        sample = np.random.multivariate_normal( mean=samplingMeans, cov=np.diag(self.__sampling_variances) )

        return sample




    def __update_single_value(self, newValue, oneHotIndexList=None):
        """
        updates a single value
        """
        if type(oneHotIndexList)==type(None):
            where = np.ones(self.__shape)
        else:
            where = oneHotIndexList

        sampleMean = newValue

        self.__update_means(sampleMean, where)
        self.__update_variances(sampleMean, where)





    def __update_multiple_values(self, newValue, oneHotIndexList=None):
        """
        updates multiple values
        """
        if type(oneHotIndexList) == type(None):
            where =  np.ones(self.__shape) * newValue.shape[0]

        else:
            where = np.sum( oneHotIndexList, axis=0 )

        values = np.sum( newValue, axis=0 )
        sampleMean = np.divide(values, where, where=where>0)

        self.__update_means(sampleMean, where)
        self.__update_variances(sampleMean, where)




    def __deal_with_valueList(self, values, index=None):
        """
        creates valued one hot or does nothing
        """

        if type(index) == type(None):
            outValues = np.array(values)
        else:
            outValues = numerical.transform_to_valued_one_hot( listOfValues=values, listOfIndexes=index, numClasses=self.__shape[0] )

        return outValues




    def __deal_with_index(self,index=None):
        """
        creates a one shot or returns None
        """
        if type(index) == type(None):
            return None
        else:
            outIndex = numerical.transform_to_one_hot(index, numClasses=self.__shape[0])
            return outIndex



    def __update_means(self, sampleMean, countVector):
        """
        updates means according to Conjugate Prior update rule.

        https://people.eecs.berkeley.edu/~jordan/courses/260-spring10/lectures/lecture5.pdf

        (sg0^2 * x_bar + sg^2 * mu0) / (sg^2/n + sg0^2)

        sg == sampling variances
        sg0 == mean variances
        """

        mask = countVector>0

        sg2n = np.divide( self.__sampling_variances, countVector, where = mask)

        denominator = sg2n[mask] + self.__variances[mask]
        numerator = self.__variances[mask] * sampleMean[mask] + self.__sampling_variances[mask] * self.__means[mask]

        self.__means[mask] = numerator / denominator

    def __update_variances(self, sampleMean, countVector):
        """
        updates means according to Conjugate Prior update rule.

        https://people.eecs.berkeley.edu/~jordan/courses/260-spring10/lectures/lecture5.pdf

        1 / (1/sg0^2 + n/sg^2)

        sg == sampling variances
        sg0 == mean variances

        Note: sampleMean is not used
        """

        mask = countVector>0

        sg2n = np.divide( countVector, self.__sampling_variances, where = mask )
        sg0  = np.divide(1, self.__variances)

        denominator = sg2n[mask] + sg0[mask]

        self.__variances[mask] = 1 / denominator




####################################################
# MAIN
####################################################


# EOF
