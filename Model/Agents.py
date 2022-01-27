"""
    This script has the information for the Agent class.
-------------------------------------------------------------------------------
created on:
    Sun 16 Jan 2022
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

class Agent(object):
    def __init__(self, ident, x, y, z):
        '''
        This function initializes the agent.
        '''
        self.ident = ident
        self.x = x
        self.y = y
        self.z = z
        self.group = None