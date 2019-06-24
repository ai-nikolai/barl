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

# >>>>>>  Local Imports   <<<<<<<

####################################################
# CODE
####################################################

def average_simulation_runs(agent, environment, simulationFunction, T=20, N=10):
    """
    Averages the simulations:

    -simulation function needs to accept: agent, environment, **params
    -simulation function needs to return: totalReward, arList, NumOfSimulations
    """
    totalReward = 0
    timeSteps = range(T)
    accumulatedTRList = []

    for _ in range(N):

        totalR, arList, _ = simulationFunction(agent, environment, N=T)

        totalReward += totalR

        rewards = [x for _,x in arList]

        accumulatedTRList.extend( list( zip( timeSteps, rewards ) ) )


    totalReward /= N

    return totalReward, arList, T, accumulatedTRList






####################################################
# MAIN
####################################################


# EOF
