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
from barl.utils import utils
from .interfaces import BaseStateLessAgent

####################################################
# CODE
####################################################

class RandomActionsSampler(BaseStateLessAgent):
    """
    simply random actions
    """
    def __init__(self,numActions):
        super().__init__(numActions)

    def learn(self, arList):
        pass

    def take_action(self):
        action =  np.random.choice( self.numActions, 1 )

        return np.squeeze(action)



class FixedActionsSampler(BaseStateLessAgent):
    """
    simply random actions
    """
    def __init__(self,numActions, fixedAction):
        super().__init__(numActions)
        self.fixedAction = fixedAction

    def learn(self, arList):
        pass

    def take_action(self, action=None):
        if type(action)==type(None):
            action = self.fixedAction

        return action







####################################################
# MAIN
####################################################


# EOF
