"""
    This script has the information for the Agent class.
-------------------------------------------------------------------------------
created on:
    Wed 26 Jan 2022
-------------------------------------------------------------------------------
last change:
    Wed 26 Jan 2022
-------------------------------------------------------------------------------
notes:
-------------------------------------------------------------------------------
contributors:
    Jose:
        name:       Jose Betancourt
        email:      jose.betancourtvalencia@yale.edu
-------------------------------------------------------------------------------
"""
import Params
import numpy as np

class Group(object):
    def __init__(self):
        '''
        This function initializes the group.
        '''
        self.members = []
        self.payoff = 0