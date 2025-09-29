'''
 * Name : Ramakrishnan Mahesh                   
 * Date : 11.07.2025                            
 * Program : To build a command line interface with python

'''

# It is important to use the python script for the efficient automation
# Python can be used to build the command line tool interface with the example given here

#####################################################################################################################
## In order to know the blocks of the directory, use the lsblk command in the command line window
## output of the lsblk command is as follows
## If you use any other commands like lsblk sdc or lsblk sda and all, you will get to see a error message as follows
## lsblk : xxx not a block device
#####################################################################################################################

'''
    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda   8:0    0 388.4M  1 disk 
sdb   8:16   0   186M  1 disk 
sdc   8:32   0     8G  0 disk [SWAP]
sdd   8:48   0     1T  0 disk /snap
                              /mnt/wslg/distro
'''

## First import the necessary modules
import os
import json
import subprocess
import shlex
import sys

def run_command(command):
    cmd = shlex.split(command)
    output = subprocess.check_output(cmd);
    return output

def run_lsblk(device):
    command = f'lsblk -J -o NAME SIZE TYPE MOUNTPOINT'
    output = run_command(command)
    devices = json.loads(output)['blockdevices']
    for parent in devices:
        if(parent['name'] == device):
            return parent
        for child in parent.get('children',[]):
            if (child['name'] == device):
                return child


def main(device):
    print(f"          '{run_lsblk(device)}'")

if __name__=='__main__':
    print(sys.argv)
    main(sys.argv[-1])