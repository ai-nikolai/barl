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
import warnings
warnings.filterwarnings("ignore")

# >>>>>>  Package Imports <<<<<<<
import seaborn as sns
import matplotlib.pyplot as plt

# >>>>>>  Local Imports   <<<<<<<
from barl.utils.utils import unzip



####################################################
# CODE
####################################################
sns.set(style="whitegrid")

def action_reward_barplot(arlist):
    """
    plots a barplot
    """
    actions, rewards = unzip(arlist)

    data = {"actions": list(actions), "rewards":list(rewards)}

    sns.barplot(x="actions", y="rewards", data=data)

    plt.show()



####################################################
# MAIN
####################################################


# EOF
