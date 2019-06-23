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
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# >>>>>>  Local Imports   <<<<<<<


####################################################
# CODE
####################################################
sns.set(style="whitegrid")






####################################################
# MAIN
####################################################
if __name__ == "__main__":
    tips = sns.load_dataset("tips")
    # print(tips)
    # print(tips["day"])
    print( type(tips["day"]) )

    x = np.array([1,1,2,2])
    y = np.array([1,2,4,5])
    data = {"day":x,"total_bill":y}

    ax = sns.barplot(x="day", y="total_bill", data=data)

    plt.show()


# EOF
