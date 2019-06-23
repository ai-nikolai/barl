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

    def learn(self):
        pass

    def take_action(self, N):
        return np.random.choice( self.numActions, [N] )



class StateLessEpsilonQLearning(StateLessFixedActionsAgent):
    """
    standard Q-learning algorithm
    """

    def __init__(self, numActions):
        super().__init__(numActions)
        self.Q = estimators.baselines.EmpiricalMean( [numActions] )

    def learn(self, actionRewardTupleList):
        """
        """
        assert actionRewardTupleList == list, "{} can only learn from List of [(Action, Reward)]"

        self.Q.update(  )

    def take_action(self, N, epsilon=0.05 ):
        """
        takes an action according to epsilon greedy policy
        """










####################################################
# MAIN
####################################################


# EOF
