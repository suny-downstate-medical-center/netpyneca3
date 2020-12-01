NetPyNe Model of CA3 Layer Repo

1. Type or `./compile` or the equivalent `nrnivmodl mod`. This should create a directory called either i686 or x86_64, depending on your computer's architecture. 

## Overview of file structure:

* /init.py: Main executable; calls functions from other modules. Sets what parameter file to use.

* /netParams.py: Network parameters

* /cfg.py: Simulation configuration

* /PYRcell.json: Cell parameters
* /OLMcell.json: Cell parameters
* /BAScell.json: Cell parameters


init.py will plot:

	 - Cell 1 of the pyramidal cell population

	 - Raster plot 

	 - LFP plots at 5 different locations across the apical dendrite and an average


Nov 30 2020


