"""
    This script runs the public opinion simulation with multiple networks with
    dynamic network structure and dynamic opinion.
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
import Agent
import Generator
import TimeIteration

#------------------------------------------------------------------------------
# INITIALIZATION
#------------------------------------------------------------------------------
# Initialize agents
population = Generator.Population()