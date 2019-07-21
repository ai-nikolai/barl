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

from .interfaces import BaseStateLessAgent


####################################################
# CODE
####################################################


class StatelessEpsilonQLearning(BaseStateLessAgent):
    """
    standard Q-learning algorithm
    """

    def __init__(self, numActions, epsilon=0.05, estimator=None):
        super().__init__(numActions)
        self.epsilon = epsilon
        self.Q = estimators.EmpiricalMean( [numActions] )


    def learn(self, actionRewardTupleList):
        """
        Learns from a list of ActionReward Tuples
        """

        actions, rewards = utils.unzip( actionRewardTupleList )
        print(actions, rewards)
        self.Q.update( newValueOrList=rewards, indexList=actions )



    def take_action(self, epsilon=None ):
        """
        takes an action according to epsilon greedy policy
        """
        if type(epsilon)==type(None):
            epsilon = self.epsilon

        tempRand = np.squeeze( np.random.uniform(0,1,1) )

        if tempRand<epsilon:
            action = np.random.choice(self.numActions)

        else:

            action = np.argmax(self.Q.get_estimate())

        return np.squeeze(action)












####################################################
# MAIN
####################################################






# EOF
