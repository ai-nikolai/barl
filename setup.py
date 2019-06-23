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
from setuptools import setup, find_packages

# >>>>>>  Package Imports <<<<<<<

# >>>>>>  Local Imports   <<<<<<<


####################################################
# CODE
####################################################





####################################################
# MAIN
####################################################
setup(

      #
      # SETUP
      #

      name          ='barl',
      version       ='1.0.0.0',
      description   ='Wluper Machine Learning Library',
      url           ='https://bitbucket.org/wluperdevteam/wluper-ml',
      author        ='nikolai rozanov',
      author_email  ='nikolai.rozanov@gmail.com',
      license       ='MIT',

      #
      # Actual packages, data and scripts
      #

      packages      = find_packages(),

      package_dir   = {'barl': 'barl'},

      install_requires=[
                        # "numpy",
                        # "torch",
                       ],

      python_requires='>=3.6'

      )

# EOF
