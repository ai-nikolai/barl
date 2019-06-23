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
from barl.agents import estimators
from barl.agents.interfaces import StateLessFixedActionsAgent

####################################################
# CODE
####################################################

class RandomActionsSampler(StateLessFixedActionsAgent):
    """
    simply random actions
    """
    def __init__(self,numActions):
        super().__init__(numActions)

    def take_action(self, N):
        return np.random.choice( self.numActions, [N] )


class StateLessQLearning(StateLessFixedActionsAgent):
    """
    standard Q-learning algorithm
    """

    def __init__(self, numActions):
        super().__init__(numActions)
        self.Q =








####################################################
# MAIN
####################################################


# EOF
