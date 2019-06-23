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
import os
import sys
from functools import partial


# >>>>>>  Package Imports <<<<<<<
import numpy as np

# >>>>>>  Local Imports   <<<<<<<
from .interfaces import StateLessEnvironment


####################################################
# CODE
####################################################

class MultiArmedBandit(StateLessEnvironment):
    """
    MultiArmedbandit - MAB
    """
    #Allowed Distributions
    distributionMapping = {
        "Normal" : np.random.normal,
    }


    def __init__(self, arms=2, means=None, variances=None, distribution="Normal"):
        if not means:
            means = MultiArmedBandit.get_means( arms )

        if not variances:
            variances = MultiArmedBandit.get_variances( arms )

        self.__arms = arms
        self.__means = means
        self.__variances = variances
        self.__distribution = distribution

        self.__set_arms()


    def sample_rewards(self, action=None, N=1):
        """
        samples rewards: np.array ( size[arms,N] )
        """
        if type(action)==type(None):

            outList = []

            for arm in self.arms:

                outList.append( arm(N) )

            rewards = np.array( outList )

        else:

            rewards = self.arms[ int(action) ](N)

        return np.squeeze( rewards )



    def get_true_variances(self):
        """
        """
        return self.__variances

    def get_true_means(self):
        """
        """
        return self.__means


    def __set_arms(self):
        """
        sets the arm properties
        """

        self.arms = []

        distro = MultiArmedBandit.distributionMapping[self.__distribution]

        for mean, variance in zip(self.__means,self.__variances):

            temp = partial(distro, mean, variance)

            self.arms.append(temp)


    @staticmethod
    def get_variances(arms = 2):
        """
        returns [v1,v2, ...v_arms] sampled from ~Unif(0,1)
        """
        return np.random.beta(a=1,b=1,size=[arms])


    @staticmethod
    def get_means(arms = 2):
        """
        returns [m1,m2, ...m_arms] sampled from ~Normal(0,1)
        """
        return np.random.normal(loc=0.0, scale=1.0, size=[arms])




####################################################
# MAIN
####################################################


# EOF
