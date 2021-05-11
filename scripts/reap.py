import pandas as pd
import numpy as np
import sys

indir = sys.argv[1]
out = sys.argv[2]

inpth = 'datasets/'+indir+'/indices_used.txt'
 
with open('datasets/inputs_test.txt','r') as f:
    inputs = f.readlines()
 
with open(inpth,'r') as h:
    indices = h.readlines()
 
numbers = [0,1,3,6]
#_indices = [0,1,2,3,4]
stats = ['sim_seconds','sim_insts','system.cpu.dcache.overall_miss_rate::total','system.cpu.dcache.overall_misses::total','system.cpu.dcache.replacements']
f = []
count = 0
for idx in indices:
    idx=int(idx)
    if(count%500==0):
    	print('-----'+str(count)+'-----')
    c = inputs[idx]
    data = []
    split_line = c[1:-2].split(', ')
    for d in range(len(split_line)):
        if d in numbers:
                d = int(split_line[d])
        else:
                d = split_line[d].split("'")[1]
        data.append(d)
    try: 	
    	pth='exp_'+indir+'/m5out_'+str(count)+'/stats.txt'
    	with open(pth) as g:
        	s = g.readlines()
    	for stat in stats:
        	for l in s:
            		if stat in l:
                		data.append(l.split()[1])
				break
    	f.append(data)
    except IOError:
	print('No output dir for run '+str(idx)+', skipping reap for this directory\n')
	print('No file named exp_'+indir+'/m5out_'+str(count)+'/stats.txt\n')
    count+=1
df = pd.DataFrame(f, columns = ['l1d_size','l1d_assoc','l2cache','l2assoc','mem_type','l1d_hwp_type','cacheline_size','sim_seconds','sim_insts','dcache_overall_miss_rate','dcache_overall_misses','dcache_replacements'])
outpth = 'datasets/csv/'+out+'.csv'
df.to_csv(outpth,index=False)
 
