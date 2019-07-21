####################################################
#
# This Work is written by Nikolai Rozanov <nikolai>
#
# Contact:  nikolai.rozanov@gmail.com
#
# Copyright (C) 2018-Present Nikolai Rozanov
#
####################################################

# >>>>>>  Native Imports  <<<<<<<

# >>>>>>  Package Imports <<<<<<<
import numpy as np

# >>>>>>  Local Imports   <<<<<<<
from barl import environments



####################################################
# CODE
####################################################


def test_that_MAB_works():
    mab = environments.MultiArmedBandit(arms=2)

    rewards = mab.sample_rewards(N=3)

    assert rewards.shape == (2,3), "MAB rewards have wrong shape"


def test_that_MAB_samples_actions_correctly():
    mab = environments.MultiArmedBandit(arms=2)

    rewards = mab.sample_rewards(action=0)

    assert rewards.shape == () , "MAB action rewards have wrong shape"



####################################################
# MAIN
####################################################
if __name__ == "__main__":
    mab = environments.MultiArmedBandit()

    rewards = mab.sample_rewards(action=0)

    print(mab.arms[0]())

    # print(rewards)
    #
    # print(rewards.shape)
    #
    # print(mab.get_true_means())
    #
    # print(mab.get_true_variances())
    #
    # rewards = mab.sample_rewards(action=1)
    # print(rewards)
    #
    # print(rewards.shape)
    #
    # print(mab.get_true_means())
    #
    # print(mab.get_true_variances())




# EOF
