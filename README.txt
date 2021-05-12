The following scripts were tested and successfully ran on ac-fe1 on the
usrc-nd02 partition. The aim of this infrastructure is to be able to run
X amount of Gem5 simulations in parallel and store the corresponding output
data from each run. After all simulations have been completed, a collection
script will consolidate all Gem5 inputs used with the corresponding output
from each Gem5 run and store in a CSV. An example of such a CSV is provided in
the data folder.



# scripts/
This directory contains 4 different scripts: spinup.py, script.slurm, gem5.py,
and reap.py

#	../spinup.py
	This python script is responsible for spawning each individual slurm
	job, using sbatch.
	Usage: python ./scripts/spinup.py <experiment name> <# runs>
#	../script.slurm
	This slurm script is called by spinup.py and is responsible for passing
        the required parameters for each job. It calls a script that runs gem5
        with those parameters.
#	../gem5.py
	This python script is where the bulk of the work is actually happening
	in the workflow. Given one of the system parameter combinations from
	inputs.txt, it will run Gem5 in full system mode with the correct flags,
	depending on what was passed in by the slurm script.
#	../reap.py
	This python script is meant to be run after all desired Gem5 runs are
	complete and will consolidate all relevant simulation inputs/stats
	into a CSV.
	Usage: python ./scripts/reap.py <experiment dir path> <csv name>

# data/
This directory contains 2 different files: fs_data_9000_plus.csv and inputs.txt

#	../fs_data_9000.csv
	A csv that contains all relevant data gathered from 9000 random Gem5
	runs using slurm
#	../inputs.txt
	A text file that contains all 18,750 possible combinations of input
	parameters for the input ranges I have determined.
