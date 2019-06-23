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
    """
    def __init__(self, size):
        self.mean = np.zeros(size)
        self.count = 0
        self.value = self.mean
        self.shape = self.mean.shape


    def update(self,newValue):
        """
        updates the mean
        """
        if newValue.shape == self.shape:
            self.value += newValue









####################################################
# MAIN
####################################################


# EOF
