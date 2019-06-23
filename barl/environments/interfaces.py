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

class StateLessEnvironment(metaclass=ABCMeta):
    """
    State Less

    Fixed Actions
    """
    @abstractmethod
    def sample_rewards(self, action=None, N=1):
        raise NotImplementedError





####################################################
# MAIN
####################################################


# EOF
