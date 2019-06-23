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

class BaseStateLessAgent(metaclass=ABCMeta):
    """
    State Less

    Fixed Actions
    """
    def __init__(self, numActions):
        self.numActions = numActions

    @abstractmethod
    def learn(self):
        raise NotImplementedError

    @abstractmethod
    def take_action(self, N):
        raise NotImplementedError





####################################################
# MAIN
####################################################


# EOF
