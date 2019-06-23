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

    agent = barl.agents.baselines.RandomActionsSampler(numActions=4)

    total, arlist = barl.simulations.run_state_less_agent_and_env( environment=env, agent=agent, N=100)

    print(total)

    barl.utils.plotting.action_reward_barplot(arlist)




# EOF
