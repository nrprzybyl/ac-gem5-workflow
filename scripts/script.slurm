#!/bin/bash

#SBATCH --job-name="gem5 test"
#SBATCH --output="out/test.%j.%N.out"
#SBATCH --partition=usrc-nd02
#SBATCH --ntasks=1
#SBATCH --export=ALL
#SBATCH -t 00:15:00

module load gnu8/8.3.0
#export PYTHONPATH=/home/nprzybylski/env/lib/python2.7/site-packages/
export PYTHONPATH=~/env/lib/python2.7/site-packages/

python ~/ac-gem5-workflow/scripts/gem5.py ${i} ${exp} ${p}
