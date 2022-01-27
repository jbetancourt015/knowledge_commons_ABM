"""
    This script has the information for the time iteration of the model.
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

class Simulation(object):
    def __init__(self):
        '''
        This function initializes the simulation object
        '''
        self.time = 0
    
    def iterate(self, agents, groups, record):
        '''
        This function advances the simulation one time step.
        '''
        # Update membership record
        record.get_membership(agents)
        # Update group payoffs
        for group in groups:
            group.update_payoffs()
        self.time += 1