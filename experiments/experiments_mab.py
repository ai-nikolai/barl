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
import numpy as np

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
    env = barl.environments.MultiArmedBandit(arms=8, means=[0,1,1.5,2,-1,3,4,3.9], variances=[0.1,0.1,0.1,0.1, 0.1,0.1,0.1,0.1])

    agent2 = barl.agents.StatelessEpsilonQLearning(numActions=4)

    total, arlist, _ = barl.simulations.run_and_train_state_less_agent_and_env( environment=env, agent=agent2, N=N)

    print(total)

    barl.utils.plotting.plot_reward_over_time_from_ar(arlist)



def averaged_q_learning_experiment(T=20, N=10):
    env = barl.environments.MultiArmedBandit(arms=8, variances=0.1*10)

    bestAction = np.argmax( env.get_true_means() )

    agentQ = barl.agents.StatelessEpsilonQLearning(numActions=8)
    agentB = barl.agents.FixedActionsSampler(numActions=8, fixedAction=bestAction)

    total, arList, _, trList = barl.simulations.average_simulation_runs(\
            environment = env,
            agent   = agentQ,
            simulationFunction  = barl.simulations.run_and_train_state_less_agent_and_env,
            T   = T,
            N   = N )

    print(total)

    total3, arList3, _, trList3 = barl.simulations.average_simulation_runs(\
            environment = env,
            agent   = agentB,
            simulationFunction  = barl.simulations.run_and_train_state_less_agent_and_env,
            T   = T,
            N   = N )

    print(total3)

    print( str(agentQ.Q) )

    barl.utils.plotting.plot_reward_over_time(trList, show=False)
    barl.utils.plotting.plot_reward_over_time(trList3, show=False)


    plt.show()

    # barl.utils.plotting.plot_actions_over_time_from_ar(arList2)
def averaged_q_learning_and_thompson_sampling_experiment(T=20,N=10):
    env = barl.environments.MultiArmedBandit(means=[0.1,8,8.1,8.2,5,0.2,0.2,0.3], variances=0.1*10)

    bestAction = np.argmax( env.get_true_means() )
    numActions = env.arms

    agentQ = barl.agents.StatelessEpsilonQLearning(numActions=numActions)
    agentT = barl.agents.StatelessThompsonSampling(numActions=numActions)
    agentB = barl.agents.FixedActionsSampler(numActions=numActions, fixedAction=bestAction)

    total, arList, _, trList = barl.simulations.average_simulation_runs(\
            environment = env,
            agent   = agentQ,
            simulationFunction  = barl.simulations.run_and_train_state_less_agent_and_env,
            T   = T,
            N   = N )

    print(total)

    total2, arList2, _, trList2 = barl.simulations.average_simulation_runs(\
            environment = env,
            agent   = agentT,
            simulationFunction  = barl.simulations.run_and_train_state_less_agent_and_env,
            T   = T,
            N   = N )

    print(total2)

    total3, arList3, _, trList3 = barl.simulations.average_simulation_runs(\
            environment = env,
            agent   = agentB,
            simulationFunction  = barl.simulations.run_and_train_state_less_agent_and_env,
            T   = T,
            N   = N )

    print(total3)

    print( str(agentQ.Q) )
    print( str(agentT.Q) )

    barl.utils.plotting.plot_reward_over_time(trList, show=False, name="Q Learning" )
    barl.utils.plotting.plot_reward_over_time(trList2, show=False, name="Thompson Sampling")
    barl.utils.plotting.plot_reward_over_time(trList3, show=False, name="Best Possible")


    plt.show()

    # barl.utils.plotting.plot_actions_over_time_from_ar(arList2)

####################################################
# MAIN
####################################################
if __name__=="__main__":

    averaged_q_learning_and_thompson_sampling_experiment(100,1000)



# EOF
