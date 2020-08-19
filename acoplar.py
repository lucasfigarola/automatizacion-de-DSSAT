from setup import *
import subprocess
import os
import re

#----------- corre DSSAT ----------
def dssat_run():
    output = open("C:/DSSAT47/Sequence/output.txt","w")
    subprocess.check_call(["C:/DSSAT47/DSCSM047.EXE","","Q","C:/DSSAT47/DSSBatch.v47"], shell=True, stdout=output)
    #subprocess.check_call(["C:/DSSAT47/DSCSM047.EXE","","Q","C:/DSSAT47/DSSBatch.v47","C:/DSSAT47/DSCSM047.CTR"], stdout=output)

#----------- modifica el archivo batch ----------
def modifier_batch(new_name_sqx):
    f= open("C:/DSSAT47/DSSBatch.v47","r")
    lines = f.readlines()
    checker = False
    #--------- obtener el nombre y carpeta del viejo txt ----------------
    for i, l in enumerate(lines):
        info = l.split()
        if checker and len(l.strip()) != 0:
            lines[i] = l[:20] + new_name_sqx + l[20+len(new_name_sqx):]
        if 'Experiment' in l:    
            lines[i] = l[:17] + new_name_sqx + '\n' #+ l[17+len(new_name_sqx):]
        if '@FILEX' in l:
            checker = True
    out = open("C:/DSSAT47/DSSBatch.v47", "w")
    out.writelines(lines)
    out.close()
        

def modify_batch(name_input):
    name = name_input + '.SQX'
    modifier_batch(name) 

#----------- crea una copia del input ----------
def copy_input(name_input,new_name_input):
    #new_name_input = name_input + 'Original'
    f= open('C:/DSSAT47/Sequence/' + name_input + '.SQX','r')
    lines = f.readlines()
    out = open('C:/DSSAT47/Sequence/' + new_name_input + '.SQX', 'w')
    out.writelines(lines)
    out.close()    
    #return new_name_input

def copy_batch():
    f= open('C:/DSSAT47/DSSBatch.v47','r')
    lines = f.readlines()
    path = os.path.join(my_path, "backup/DSSBatch.v47")
    out = open(path, 'w')
    out.writelines(lines)
    out.close()    

def restore_batch():
    path = os.path.join(my_path, "backup/DSSBatch.v47")
    f= open(path,'r')
    lines = f.readlines()
    out = open('C:/DSSAT47/DSSBatch.v47', 'w')
    out.writelines(lines)
    out.close()   

def change_name(old_crop_name,new_crop_name):
    f= open("C:/DSSAT47/Sequence/UBAR2001.SQX","r")
    lines = f.readlines()
    checker = None 
    for i, l in enumerate(lines):
        info = l.split()
        if old_crop_name in l and checker:
            lines[i] = l[:9] + new_crop_name + '   ' + l[16:] 
            checker = None
        if '*TREATMENTS' in l: 
            checker = True
    out = open('C:/DSSAT47/Sequence/UBAR20010.SQX', 'w')
    out.writelines(lines)
    out.close()
    
#name1 = 'ITHY7502.SQX'
#name2 = 'Sequence'

#modify_batch(name1,name2)    
#dssat_run()