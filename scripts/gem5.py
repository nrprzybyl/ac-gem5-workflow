# python script that will run gem5

import random
import os
import sys

#os.system('module load gnu8/8.3.0')
#os.system('export PYTHONPATH=/home/nprzybylski/env/lib/python2.7/site-packages/')

p = int(sys.argv[3])
exp = sys.argv[2]
i = sys.argv[1]

with open('datasets/inputs_test.txt') as f:
	lines = f.readlines()

c = lines[p]

numbers = [0, 1, 3, 6]
data = []

split_line = c[1:-2].split(', ')
for d in range(len(split_line)):
	if d in numbers:
            	d = int(split_line[d])
        else:
            	d = split_line[d].split("'")[1]
	data.append(d)

#pth='/home/nprzybylski/gem5'
pth='~/gem5'

print(data)

# l1d_sizes, l1d_assoc, l2cache, l2_assoc, mem_types, l1d_hwp_types, cacheline_sizes

if(data[5] == 'None'):
	if(data[2] == 'OFF'):
		cmd=''+pth+'/build/X86/gem5.fast --outdir=exp_'+exp+'/m5out_'+str(i)+' -r '+pth+'/configs/example/fs.py --disk-image='+pth+'/fs_images/disks/linux-x86.img --kernel='+pth+'/fs_images/binaries/x86_64-vmlinux-2.6.22.9 --script='+pth+'/test --cpu-type=TimingSimpleCPU --caches --l1d_size='+str(data[0])+'kB --l1d_assoc='+str(data[1])+' --mem-type='+str(data[4])+' --cacheline_size='+str(data[6])

	else:
		cmd=''+pth+'/build/X86/gem5.fast --outdir=exp_'+exp+'/m5out_'+str(i)+' -r '+pth+'/configs/example/fs.py --disk-image='+pth+'/fs_images/disks/linux-x86.img --kernel='+pth+'/fs_images/binaries/x86_64-vmlinux-2.6.22.9 --script='+pth+'/test --cpu-type=TimingSimpleCPU --caches --l1d_size='+str(data[0])+'kB --l1d_assoc='+str(data[1])+' --l2cache --l2_assoc='+str(data[3])+' --mem-type='+str(data[4])+' --cacheline_size='+str(data[6])
else:
	if(data[2] == 'OFF'):
		cmd=''+pth+'/build/X86/gem5.fast --outdir=exp_'+exp+'/m5out_'+str(i)+' -r '+pth+'/configs/example/fs.py --disk-image='+pth+'/fs_images/disks/linux-x86.img --kernel='+pth+'/fs_images/binaries/x86_64-vmlinux-2.6.22.9 --script='+pth+'/test --cpu-type=TimingSimpleCPU --caches --l1d_size='+str(data[0])+'kB --l1d_assoc='+str(data[1])+' --mem-type='+str(data[4])+' --l1d-hwp-type='+str(data[5])+' --cacheline_size='+str(data[6])
	else:
		cmd=''+pth+'/build/X86/gem5.fast --outdir=exp_'+exp+'/m5out_'+str(i)+' -r '+pth+'/configs/example/fs.py --disk-image='+pth+'/fs_images/disks/linux-x86.img --kernel='+pth+'/fs_images/binaries/x86_64-vmlinux-2.6.22.9 --script='+pth+'/test --cpu-type=TimingSimpleCPU --caches --l1d_size='+str(data[0])+'kB --l1d_assoc='+str(data[1])+' --l2cache --l2_assoc='+str(data[3])+' --mem-type='+str(data[4])+' --l1d-hwp-type='+str(data[5])+' --cacheline_size='+str(data[6])

os.system(cmd)
