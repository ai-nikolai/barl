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
import matplotlib.pyplot as plt

# >>>>>>  Local Imports   <<<<<<<
import barl

####################################################
# CODE
####################################################

def random_action_q_learning_experiment():
    env = barl.environments.MultiArmedBandit(arms=4)

    agent1 = barl.agents.RandomActionsSampler(numActions=4)

    total, arlist, _ = barl.simulations.run_state_less_agent_and_env( environment=env, agent=agent1, N=100)

    print(total)

    agent2 = barl.agents.StatelessEpsilonQLearning(numActions=4)

    agent2.learn(arlist)

    total2, arlist2, _ = barl.simulations.run_state_less_agent_and_env( environment=env, agent=agent2, N=100)

    print(total2)

    barl.utils.plotting.action_reward_barplot(arlist)



def q_learning_experiment(N=10):
    env = barl.environments.MultiArmedBandit(arms=4, means=[0,1,1.5,2], variances=[0.1,0.1,0.1,0.1])

    agent2 = barl.agents.StatelessEpsilonQLearning(numActions=4)

    total, arlist, _ = barl.simulations.run_and_train_state_less_agent_and_env( environment=env, agent=agent2, N=N)

    print(total)

    barl.utils.plotting.plot_reward_over_time_from_ar(arlist)



def averaged_q_learning_experiment(T=20,N=10):
    env = barl.environments.MultiArmedBandit(arms=4, means=[0,1,1.5,2], variances=[0.1,0.1,0.1,0.1])

    agent2 = barl.agents.StatelessEpsilonQLearning(numActions=4)
    agentB = barl.agents.FixedActionsSampler(numActions=4, fixedAction=3)

    total, arList, _, trList = barl.simulations.average_simulation_runs(\
            environment = env,
            agent   = agent2,
            simulationFunction  = barl.simulations.run_and_train_state_less_agent_and_env,
            T   = T,
            N   = N )

    print(total)

    total2, arList2, _, trList2 = barl.simulations.average_simulation_runs(\
            environment = env,
            agent   = agentB,
            simulationFunction  = barl.simulations.run_and_train_state_less_agent_and_env,
            T   = T,
            N   = N )

    print(total2)

    print( str(agent2.Q) )

    barl.utils.plotting.plot_reward_over_time(trList, show=False)
    barl.utils.plotting.plot_reward_over_time(trList2, show=False)


    plt.show()

    barl.utils.plotting.plot_actions_over_time_from_ar(arList)

####################################################
# MAIN
####################################################
if __name__=="__main__":

    averaged_q_learning_experiment(200,10)



# EOF
