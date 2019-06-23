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
import numpy as np

# >>>>>>  Local Imports   <<<<<<<
from barl.estimators.baselines import EmpiricalMean
from barl.utils import numerical

####################################################
# CODE
####################################################

def test_empirical_mean_1():
    meanEst = EmpiricalMean([3])

    values = [1,2,3]
    idx = [0,0,1]
    out = np.array([1.5, 3, 0])

    meanEst.update(values, idx)

    assert np.array_equal( out, meanEst.get_estimate() ), "Empirical Mean 1"



def test_empirical_mean_2():
    meanEst = EmpiricalMean([3])

    values = 2
    idx = 0
    out = np.array([2, 0, 0])

    meanEst.update(values, idx)

    assert np.array_equal( out, meanEst.get_estimate() ), "Empirical Mean 2"



def test_empirical_mean_3():
    meanEst = EmpiricalMean([3])

    values = [[1,1,1],[2,2,2]]

    out = np.array([1.5, 1.5, 1.5])

    meanEst.update(values)

    assert np.array_equal( out, meanEst.get_estimate() ), "Empirical Mean 3"


def test_empirical_mean_4():
    meanEst = EmpiricalMean([3])

    values = [1,1,1]

    out = np.array([1,1,1])

    meanEst.update(values)

    assert np.array_equal( out, meanEst.get_estimate() ), "Empirical Mean 4"

####################################################
# MAIN
####################################################
if __name__ == "__main__":
    meanEst = EmpiricalMean([3])

    values = [[1,1,1],[2,2,2]]

    out = np.array([1.5, 1.5, 1.5])

    meanEst.update(values)

    print( meanEst.get_estimate() )



# EOF
