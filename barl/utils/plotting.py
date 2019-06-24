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

def action_reward_barplot(arList, show=True):
    """
    plots a barplot
    """
    data = transform_arlist_to_data(arList)

    sns.barplot(x="actions", y="rewards", data=data)

    if show:
        plt.show()


def plot_reward_over_time_from_ar(arList, show=True):
    """
    plots reward over time
    """
    data = transform_arlist_to_data(arList)

    sns.lineplot( x=data["time"], y=data["rewards"] )

    if show:
        plt.show()



def plot_reward_over_time(trList, show=True):
    """
    plots reward over time
    """
    data = transform_trlist_to_data(trList)

    sns.lineplot( x=data["time"], y=data["rewards"] )

    if show:
        plt.show()

def plot_actions_over_time_from_ar(arList, show=True):
    """
    plots reward over time
    """
    data = transform_arlist_to_data(arList)

    sns.lineplot( x=data["time"], y=data["actions"] )

    if show:
        plt.show()









def transform_trlist_to_data(trList):
    """
    """
    timeSteps, rewards = unzip(trList)

    data = {"rewards":list(rewards), "time": timeSteps}

    return data

def transform_arlist_to_data(arList):
    """
    """
    actions, rewards = unzip(arList)

    timeSteps = range( len(actions) )

    data = {"actions": list(actions), "rewards":list(rewards), "time": timeSteps}

    return data

####################################################
# MAIN
####################################################


# EOF
