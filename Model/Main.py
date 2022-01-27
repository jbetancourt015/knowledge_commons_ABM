"""
    This script runs the public opinion simulation with multiple networks with
    dynamic network structure and dynamic opinion.
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
import Agent
import Generator
import TimeSeries
import Output

#------------------------------------------------------------------------------
# SIMULATION
#------------------------------------------------------------------------------
def simulate():
    '''
    This function initializes and runs the simulation.
    '''
    # Initialize agents
    population = Generator.Population()
    print('Initialization complete')
    # Initialize timeSeries object
    timeSeries = TimeSeries.TimeSeries()
    # Extract agents and groups
    agents = population.agents
    groups = population.groups
    # Run simulation
    Generator.run_simulation(agents, groups, timeSeries)
    print('Simulation complete')