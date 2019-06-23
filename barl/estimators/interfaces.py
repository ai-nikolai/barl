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
from abc import ABCMeta, abstractmethod

# >>>>>>  Package Imports <<<<<<<
import numpy as np

# >>>>>>  Local Imports   <<<<<<<


####################################################
# CODE
####################################################

class BaseEstimator(metaclass=ABCMeta):
    """
    Base Interface for Estimators
    """
    @abstractmethod
    def update(self):
        raise NotImplementedError

    @abstractmethod
    def get_estimate(self):
        raise NotImplementedError






####################################################
# MAIN
####################################################


# EOF
