import sys
import os
import random

def anydup(thelist):
  	seen = set()
  	for x in thelist:
		if x in seen: return True
		seen.add(x)
  	return False

exp=sys.argv[1]
nruns=sys.argv[2]

with open('datasets/inputs_test.txt') as f:
	lines = f.readlines()

indices = random.sample(range(0,len(lines)), int(nruns))

for i in range(int(nruns)):

	index = indices[i]
	lines[index]=None

#print("length of indices: {0}\n").format(len(indices))
#print("any duplicates? {0}").format(anydup(indices))


	cmd='sbatch --export=exp='+exp+',i='+str(i)+',p='+str(index)+' ~/ac-gem5-workflow/scripts/script.slurm'
	os.system(cmd)

opth = 'datasets/'+exp
ri=opth+'/remaining_inputs.txt'
iu=opth+'/indices_used.txt'
ocmd='mkdir '+opth
os.system(ocmd)
#with open(opth, 'w') as g:
#	for line in lines:
#        	g.write("%s\n" % line)

with open(ri, 'w') as filehandle:
        for line in lines:
                filehandle.write('%s\n' % line)

with open(iu, 'w') as h:
	for idx in indices:
		h.write("%d\n" % idx)
