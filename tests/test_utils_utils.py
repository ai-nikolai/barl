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
from barl.utils import utils

####################################################
# CODE
####################################################


def test_unzip():
    x = [1,2,3]
    y = [4,5,6]

    z = zip(x,y)

    v,w = utils.unzip(z)

    assert v==x, "Unzip 1"
    assert w==y, "Unzip 2"





####################################################
# MAIN
####################################################

if __name__=="__main__":
    print("hi")



# EOF
