"""
    This script has the information for the initialization of the model.
-------------------------------------------------------------------------------
created on:
    Sun 16 Jan 2022
-------------------------------------------------------------------------------
last change:
    Sun 16 Jan 2022
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
import Agents
import numpy as np

#------------------------------------------------------------------------------
# GENERATION
#------------------------------------------------------------------------------
class Population(object):
    def __init__(self, agents=None):
        '''
        This function initializes the population object.

        '''
        self.agents = agents
    
    def initialize(self):
        '''
        This function initializes the model population.

        '''
        # Create agent population
        agents = []
        Na = Params.N_agents
        for i in range(Na):
            opinion = np.random.rand()
            agent = Agents.Agent(ident=i, opinion=opinion)
            agents.append(agent)
        self.agents = agents
        # Create network interactions
        Ng = Params.N_networks
        n_mean = Params.mean_neighbors
        n_max = Params.max_neighbors
        for i in range(Na):
            neighbors = []
            for n in range(Ng):
                choice_set = np.delete(np.arange(Na), i)
                neighbors_g = np.random.choice(choice_set, min(np.random.poisson(n_mean), n_max))
                neighbors.append(neighbors_g)
            agents[i].create_neighbors(neighbors)
                