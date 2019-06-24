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
      version       ='0.0.0.1',
      description   ='Bayesian Approximate Reinforcement Learning (BARL)',
      url           ='https://github.com/ai-nikolai/barl',
      author        ='nikolai rozanov',
      author_email  ='nikolai.rozanov@gmail.com',
      license       ='MIT',

      #
      # Actual packages, data and scripts
      #

      packages      = find_packages(),

      package_dir   = {'barl': 'barl'},

      install_requires=[
                        "numpy",
                        "matplotlib",
                        "seaborn>=0.9",
                       ],

      python_requires='>=3.6'

      )

# EOF
