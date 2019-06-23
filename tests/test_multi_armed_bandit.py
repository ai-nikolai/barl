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
    mab = environments.MultiArmedBandit()

    rewards = mab.sample_rewards(N=3)

    assert rewards.shape == (2,3), "MAB rewards have wrong shape"






####################################################
# MAIN
####################################################
if __name__ == "__main__":
    mab = simple_environments.MultiArmedBandit()

    rewards = mab.sample_rewards(N=3)

    print(rewards)

    print(rewards.shape)

    print(mab.get_true_means())

    print(mab.get_true_variances())


# EOF

#
