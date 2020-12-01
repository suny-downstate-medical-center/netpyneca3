from netpyne import specs, sim
from neuron import gui
from math import sqrt 

from cfg import simdur

#simdur = 300

netParams = specs.NetParams()  

netParams.sizeX = 100 # x-dimension (horizontal length) size in um
netParams.sizeY = 1000 # y-dimension (vertical height or cortical depth) size in um
netParams.sizeZ = 100 # z-dimension (horizontal length) size in um
netParams.propVelocity = 100.0 # propagation velocity (um/ms)
netParams.probLengthConst = 150.0 # length constant for conn probability (um)

# Network parameters
netParams.popParams['PYR'] = {'cellType': 'PYR', 'numCells': 800, 'yRange': [100,600], 'cellModel': 'HH'}
netParams.popParams['OLM'] = {'cellType': 'OLM', 'numCells': 200, 'yRange': [500,600], 'cellModel': 'HH'}
netParams.popParams['BAS'] = {'cellType': 'BAS', 'numCells': 200, 'yRange': [200,500], 'cellModel': 'HH'}
'''
netParams.importCellParams(
    label = 'PYR_rule',
    conds = {'cellType': 'PYR','cellModel': 'HH'},
    fileName = 'cellParams.py',
    cellName =  'PyrAdr',
    )


netParams.importCellParams(
    label = 'OLM_rule',
    conds =  {'cellType': 'OLM','cellModel': 'HH'},
    fileName = 'cellParams.py',
    cellName = 'Ow'
    )

netParams.importCellParams(
    label = 'BAS_rule',
    conds ={'cellType': 'BAS','cellModel': 'HH'},
    fileName = 'cellParams.py',
    cellName = 'Bwb',
    )


netParams.saveCellParamsRule('BAS_rule', 'BAScell.json')
netParams.saveCellParamsRule('PYR_rule', 'PYRcell.json')
netParams.saveCellParamsRule('OLM_rule', 'OLMcell.json')
'''

netParams.loadCellParamsRule('PYR_rule','PYRcell.json')
netParams.loadCellParamsRule('OLM_rule','OLMcell.json')
netParams.loadCellParamsRule('BAS_rule','BAScell.json')


#making Synapses
#AMPA
netParams.synMechParams['AMPAf'] =  {'mod': 'MyExp2SynBB',     'tau1': 0.05,  'tau2': 5.3, 'e': 0} # AMPA used in 3 places

#NMDA
netParams.synMechParams['NMDA'] = {'mod': 'MyExp2SynNMDABB', 'tau1': 0.05, 'tau2': 5.3, 'tau1NMDA': 15, 
'tau2NMDA': 150, 'r': 1, 'e': 0}

#GABA
netParams.synMechParams['GABAf'] = {'mod': 'MyExp2SynBB',     'tau1': 0.07, 'tau2': 9.1, 'e': -80}
netParams.synMechParams['GABAs'] = {'mod': 'MyExp2SynBB',     'tau1': 0.2,  'tau2': 20 , 'e': -80} # Adend2GABAs
netParams.synMechParams['GABAss'] ={'mod': 'MyExp2SynBB',     'tau1': 20,   'tau2': 40 , 'e': -80} # somaGABAss

#IClamps
netParams.stimSourceParams['PyrIClamp'] = {'type': 'IClamp', 'del': 0.2, 'dur': 1e9, 'amp': '50e-3'}
netParams.stimSourceParams['OlmIClamp'] = {'type': 'IClamp', 'del': 0.2, 'dur': 1e9, 'amp': '-25e-3'}
netParams.stimSourceParams['BasIClamp'] = {'type': 'IClamp', 'del': 0.2, 'dur': 0, 'amp': '0'}

# Background IClamp
netParams.stimTargetParams['bgPyrIClamp'] = {'conds': {'popLabel': 'PYR'}, # background -> pyr
  'sec' : 'soma', 'loc': 0.5,
  'source': 'PyrIClamp'}
netParams.stimTargetParams['bgOlmIClamp'] = {'conds': {'popLabel': 'OLM'}, # background -> pyr
  'sec' : 'soma', 'loc': 0.5,
  'source': 'OlmIClamp'}
netParams.stimTargetParams['bgBasIClamp'] = {'conds': {'popLabel': 'BAS'}, # background -> pyr
  'sec' : 'soma', 'loc': 0.5,
  'source': 'BasIClamp'}


## Synapse Connections Params
print("pyr->bas, AMPA,NMDA ")
netParams.connParams['PyrBasEx'] = {'synMech': ['AMPAf','NMDA'], 
  'delay': 2, 'weight': [0.3*1.2e-3,1.15*1.2e-3], 'convergence': 100, 
  'preConds': {'cellType': 'PYR'}, 'postConds': {'cellType': 'BAS'},
  'sec':'soma', 'loc': 0.5,'threshold':10, 'preLoc':.5, 'preSec': 'soma'}

print("pyr -> olm, AMPA,NMDA " )             
netParams.connParams['PyrOlmEx']=  {'synMech': ['AMPAf','NMDA'], 
  'delay': 2, 'weight': [0.3*1.2e-3, 0.7e-3], 'convergence':  10,
  'preConds': {'cellType': 'PYR'}, 'postConds': {'cellType': 'OLM'},
  'sec':'soma', 'loc': 0.5,'threshold':10, 'preLoc':.5, 'preSec': 'soma' }

print("pyr->pyr, AMPA,NMDA" )             
netParams.connParams['PyrPyrEx'] = {'synMech': ['AMPAf', 'NMDA'],
   'delay':    2, 'weight': [0.5*0.04e-3, 0.004e-3], 'convergence':25, 
   'preConds': {'cellType': 'PYR'}, 'postConds': {'cellType': 'PYR'},
   'sec':'Bdend', 'loc':1.0,'threshold':10, 'preLoc':.5, 'preSec': 'soma'}

print("BAS -> BAS , GABA")
netParams.connParams['BasBasGf'] = {'synMech': 'GABAf', 
  'delay':   2,'weight': 3.*1.5*1.0e-3, 'convergence': 60,  
  'preConds': {'cellType': 'BAS'}, 'postConds': {'cellType': 'BAS'},
  'sec':'soma', 'loc': 0.5,'threshold':10, 'preLoc':.5, 'preSec': 'soma'}

print("bas > pyr, gaba")
netParams.connParams['BasPyrGf'] = {'synMech': 'GABAf', 
  'delay':   2,'weight': 2.*2.*0.18e-3, 'convergence': 50, 
  'preConds': {'cellType': 'BAS'}, 'postConds': {'cellType': 'PYR'},
  'sec':'soma', 'loc': 0.5,'threshold':10, 'preLoc':.5, 'preSec': 'soma'}

print("OLM -> PYR , GABA")
netParams.connParams['OlmPyrGf'] = {'synMech': 'GABAs',
  'delay':2,'weight': 4.0*3.*6.0e-3, 'convergence': 20, 
  'preConds': {'cellType': 'OLM'}, 'postConds': {'cellType': 'PYR'},
  'sec':'Adend2','loc':.5,'threshold':10, 'preLoc':.5, 'preSec': 'soma'}


## Stimulation sources parameters
#netParams.stimSourceParams['NMDAe'] = {'type': 'NetStim', 'interval': 100, 'noise': 0, 'start': 0,'number':10*simdur}
#netParams.stimSourceParams['AMPAe'] =  {'type': 'NetStim', 'interval': 1, 'noise': 0,  'start': 0,'number':1e3*simdur}
#netParams.stimSourceParams['GABAe'] = {'type': 'NetStim', 'interval': 1, 'noise': 0,  'start': 0, 'number':1e3*simdur}
#netParams.stimSourceParams['GABAss'] ={'type': 'NetStim', 'interval': 150, 'noise': 0,  'start': 0, 'number':(1e3 / 150.0) * simdur}
netParams.stimSourceParams['NMDAe'] = {'type': 'NetStim', 'interval': 100, 'noise': .5, 'start': 0,'number':10*simdur}
netParams.stimSourceParams['AMPAe'] =  {'type': 'NetStim', 'interval': 1, 'noise': .5,  'start': 0,'number':1e3*simdur}
netParams.stimSourceParams['GABAe'] = {'type': 'NetStim', 'interval': 1, 'noise': .5,  'start': 0, 'number':1e3*simdur}
netParams.stimSourceParams['GABAss'] ={'type': 'NetStim', 'interval': 150, 'noise': .5,  'start': 0, 'number':(1e3 / 150.0) * simdur}

# NetStims
print('bkg -> pyr')
netParams.stimTargetParams['bgPyrAMPAs'] = {'conds': {'popLabel': 'PYR'}, # background -> pyr
  'weight': 0.05e-3,                     # synaptic weight n
  'delay': '.2',      # transmission delay (ms) 
  'synMech':'AMPAf', 
  'sec':'soma', 'loc': 0.5,                       
  'source': 'AMPAe'}
netParams.stimTargetParams['bgPyrAMPA3'] = {'conds': {'popLabel': 'PYR'}, # background -> pyr
  'weight': 0.05e-3,                     # synaptic weight n
  'delay': '2. * 0.1',      # transmission delay (ms) 
  'synMech':'AMPAf', 
  'sec':'Adend3', 'loc': 0.5,                             
  'source': 'AMPAe'}
netParams.stimTargetParams['bgPYRGABAs'] = {'conds': {'popLabel': 'PYR'}, # background -> pyr
  'weight': 0.012e-3,                     # synaptic weight n
  'delay': '2. * 0.1',      # transmission delay (ms) 
  'synMech':'GABAf',
  'sec' : 'soma', 'loc': 0.5,                               
  'source': 'GABAe'}
netParams.stimTargetParams['bgPyrGABA3'] = {'conds': {'popLabel': 'PYR'}, # background -> pyr
  'weight': 0.012e-3,                     # synaptic weight n
  'delay': '2. * 0.1',      # transmission delay (ms) 
  'synMech':'GABAf',
  'sec':'Adend3', 'loc': 0.5,                            
  'source': 'GABAe'}
netParams.stimTargetParams['bgPyrNMDA3'] = {'conds': {'popLabel': 'PYR'}, # background -> pyr
  'weight': 6.5e-3,                     # synaptic weight n
  'delay': '2. * 0.1',      # transmission delay (ms) 
  'synMech':'NMDA', 
  'sec':'Adend3', 'loc': 0.5,                    
  'source': 'NMDAe'}

print('bkg -> olm')
netParams.stimTargetParams['bgOlmAMPA'] = {'conds': {'popLabel': 'OLM'}, # background -> olm
  'weight': 0.0625e-3,                     # synaptic weight n
  'delay': '2. * 0.1',      # transmission delay (ms) 
  'synMech':'AMPAf',  
  'sec':'soma', 'loc': 0.5,                             
  'source': 'AMPAe'}
netParams.stimTargetParams['bgOlmGABA'] = {'conds': {'popLabel': 'OLM'}, # background -> olm
  'weight': 0.2e-3,                     # synaptic weight n
  'delay': '2. * 0.1',      # transmission delay (ms) 
  'synMech':'GABAf',
  'sec':'soma', 'loc': 0.5,                                
  'source': 'GABAe'}


print('bkg -> BAS')
netParams.stimTargetParams['bgBasAMPA'] = {'conds': {'popLabel': 'BAS'}, # background -> bas
   'weight': 0.02e-3,                     # synaptic weight n
   'delay': '2. * 0.1',      # transmission delay (ms) 
   'synMech':'AMPAf',
   'sec':'soma', 'loc': 0.5 ,                           
   'source': 'AMPAe'}
netParams.stimTargetParams['bgBasGABA'] = {'conds': {'popLabel': 'BAS'}, # background -> bas
   'weight': 0.2e-3,                     # synaptic weight n
   'delay': '2. * 0.1',      # transmission delay (ms) 
   'synMech':'GABAf',
   'sec':'soma', 'loc': 0.5,                         
   'source': 'GABAe'}

print('sept -> X')
netParams.stimTargetParams['sepOlmGABA'] = {'conds': {'popLabel': 'OLM'}, # MedialSpetal -> olm
  'weight': 1.6e-3 ,                     # synaptic weight n
  'delay': '2. * 0.1',      # transmission delay (ms) 
  'synMech':'GABAss',
  'sec':'soma', 'loc': 0.5,                             
  'source': 'GABAss'}
netParams.stimTargetParams['sepBasGABA'] = {'conds': {'popLabel': 'BAS'}, # MedialSeptal -> bas
  'weight': 1.6e-3 ,                     # synaptic weight n
  'delay': '2. * 0.1',      # transmission delay (ms) 
  'synMech':'GABAss', 
  'sec':'soma', 'loc': 0.5,              
  'source': 'GABAss'}




