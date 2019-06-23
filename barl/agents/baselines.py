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
from barl import estimators
from barl.utils import utils

from .interfaces import BaseFixedActionAgent

####################################################
# CODE
####################################################

class RandomActionsSampler(BaseFixedActionAgent):
    """
    simply random actions
    """
    def __init__(self,numActions):
        super().__init__(numActions)

    def learn(self):
        pass

    def take_action(self, N):
        return np.random.choice( self.numActions, [N] )



class StateLessEpsilonQLearning(BaseFixedActionAgent):
    """
    standard Q-learning algorithm
    """

    def __init__(self, numActions):
        super().__init__(numActions)
        self.Q = estimators.baselines.EmpiricalMean( [numActions] )

    def learn(self, actionRewardTupleList):
        """
        Learns from a list of ActionReward Tuples
        """

        actions, rewards = utils.unzip( actionRewardTupleList )
        self.Q.update( newValueOrList=rewards, indexList=actions )

    def take_action(self, N, epsilon=0.05 ):
        """
        takes an action according to epsilon greedy policy
        """
        tempRand = np.random.uniform(1)

        if tempRand<epsilon:

            return np.random.choice(self.numActions)

        else:

            return np.argmin(self.Q.get_estimate())










####################################################
# MAIN
####################################################


# EOF
