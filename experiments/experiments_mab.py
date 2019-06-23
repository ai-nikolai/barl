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





####################################################
# MAIN
####################################################
if __name__=="__main__":
    env = barl.environments.MultiArmedBandit(arms=4)

    agent1 = barl.agents.baselines.RandomActionsSampler(numActions=4)

    total, arlist = barl.simulations.run_state_less_agent_and_env( environment=env, agent=agent1, N=100)

    print(total)

    agent2 = barl.agents.baselines.StateLessEpsilonQLearning(numActions=4)

    agent2.learn(arlist)

    total2, arlist2 = barl.simulations.run_state_less_agent_and_env( environment=env, agent=agent2, N=100)

    print(total2)


    # barl.utils.plotting.action_reward_barplot(arlist)




# EOF
