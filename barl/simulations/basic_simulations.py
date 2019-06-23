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
from barl.agents.interfaces import BaseStateLessAgent
from barl.environments.interfaces import StateLessEnvironment


####################################################
# CODE
####################################################

def run_state_less_agent_and_env(agent, environment, N=10):
    """
    Runs the simulation of agent and environment for N steps
    """
    assert issubclass( type(agent), BaseStateLessAgent ) , "Wrong Agent"
    assert issubclass( type(environment), StateLessEnvironment ) , "Wrong Environment"

    ARList = []
    totalReward = 0

    for t in range(N):

        action = agent.take_action()
        print(action)
        reward = environment.sample_rewards(action=action)
        print(reward)
        
        ARList.append( (action, reward) )
        totalReward += reward

    return totalReward, ARList









####################################################
# MAIN
####################################################


# EOF
