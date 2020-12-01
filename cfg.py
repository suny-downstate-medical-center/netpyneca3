from netpyne import specs, sim
from neuron import gui
from math import sqrt 

simdur = 300

# Simulation options
simConfig = specs.SimConfig()        # object of class SimConfig to store simulation configuration
simConfig.duration = simdur         # Duration of the simulation, in ms
simConfig.dt = 0.025                  # Internal integration timestep to use
simConfig.checkErrors = True
simConfig.verbose = False            # Show detailed messages 
simConfig.seeds={'conn': 1, 'stim': 1, 'loc': 1}

#simConfig.recordCells = [('PYR',0),('PYR',1),('PYR',2) ,('OLM',0),('OLM',1),('BAS',0),('BAS',1)]
#simConfig.recordCells = [('PYR',0)]
simConfig.recordTraces = {'V_soma':{'sec':'soma','loc':.5,'var':'v'}}  # Dict with traces to record
simConfig.recordStep = 0.1          # Step size in ms to save data (eg. V traces, LFP, etc)
simConfig.analysis['plotTraces'] = {'include': [('PYR',0)]}

simConfig.analysis['plotRaster'] = {'saveFig': True}                  # Plot a raster
#simConfig.plotRaster = True          # Plot a raster
#simConfig.orderRasterYnorm = 1       # Order cells in raster by yfrac (default is by pop and cell id)

#simConfig.recordLFP = True          # Plot a raster
#simConfig.recordLFP = e.g. [[50, 100, 50], [50, 200, 50]]
simConfig.recordLFP = [[30, y, 35] for y in range(150, 650, 150)]
simConfig.analysis['plotLFP'] = {'plots': ['timeSeries'], 'saveFig': True} 

   






