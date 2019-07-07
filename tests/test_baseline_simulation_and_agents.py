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
import barl


####################################################
# CODE
####################################################

def test_averaged_simulation():
    N=3
    T=10

    env = barl.environments.MultiArmedBandit(arms=4, means=[0,1,1.5,2], variances=[0.1,0.1,0.1,0.1])

    agent2 = barl.agents.stateless_agents.StatelessEpsilonQLearning(numActions=4)
    agentB = barl.agents.baselines.FixedActionsSampler(numActions=4, fixedAction=3)

    total, arList, t1, trList = barl.simulations.average_simulation_runs(\
            environment = env,
            agent   = agent2,
            simulationFunction  = barl.simulations.run_and_train_state_less_agent_and_env,
            T   = T,
            N   = N )

    print(total)

    total2, arList2, t2, trList2 = barl.simulations.average_simulation_runs(\
            environment = env,
            agent   = agentB,
            simulationFunction  = barl.simulations.run_and_train_state_less_agent_and_env,
            T   = T,
            N   = N )

    print(total2)


    assert total <= total2, "Best Possible Needs to outperform Q-Learning"
    assert t1==T
    assert t2==T
    assert len( arList2 ) == T





####################################################
# MAIN
####################################################


# EOF
