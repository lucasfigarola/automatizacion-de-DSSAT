from setup import *
from acoplar import *
from auxiliary_functions import *
from fertilizer_calculation import *
from run_simulations import *
from graphic_standard import *
from sequence_generator import *
import re
import os
import glob

max_line_treatments = 12

def script_sequences(name_input):
    create_batch()
    name_input_original = name_input
    name_input = name_input + 'aux'
    copy_input(name_input_original,name_input)
    modify_batch(name_input)

    line_treatments = num_line_TREATMENTS(name_input_original)
    crop_ids = create_dicc_ids(name_input)
    coefficients = get_all_coefficients()
    dicc_sequence = sequenceGenerator()
    num_line = 2
    for i in range(2,max_line_treatments):
        sequences = dicc_sequence[i]
        for j in range(len(sequences)):
            crops = sequences[j]
            print(crops)
            total_function(name_input,crops,crop_ids,coefficients)
        add_line(name_input,num_line,line_treatments)
        num_line += 1


def run_generator_sequences(input_name):
    create_batch()
    input_name_original = input_name
    input_name = input_name + 'aux'
    copy_input(input_name_original,input_name)
    modify_batch(input_name)

    line_treatments = num_line_TREATMENTS(input_name_original)
    crop_ids = create_dicc_ids(input_name)
    coefficients = get_all_coefficients()

    crops = ['Soja','Barbecho']
    total_function(input_name,crops,crop_ids,coefficients)

    crops = ['Maiz','Barbecho']
    total_function(input_name,crops,crop_ids,coefficients)

    crops = ['Trigo','Barbecho']
    #total_function(input_name,crops,crop_ids,coefficients)


    num_line = 2
    add_line(input_name,num_line,line_treatments)
    num_line += 1

    crops = ['Trigo','Soja2','Barbecho']
    total_function(input_name,crops,crop_ids,coefficients)

    add_line(input_name,num_line,line_treatments)
    num_line += 1

    crops = ['Maiz','Barbecho','Soja','Barbecho']
    total_function(input_name,crops,crop_ids,coefficients)

    crops = ['Soja','Barbecho','Trigo','Barbecho']
    #total_function(input_name,crops,crop_ids,coefficients)

    crops = ['Maiz','Barbecho','Trigo','Barbecho']
    #total_function(input_name,crops,crop_ids,coefficients)

    add_line(input_name,num_line,line_treatments)
    num_line += 1
    add_line(input_name,num_line,line_treatments)
    num_line += 1

    crops = ['Maiz','Barbecho','Trigo','Barbecho','Soja','Barbecho']
    total_function(input_name,crops,crop_ids,coefficients)

    crops = ['Trigo','Soja2','Barbecho','Trigo','Soja2','Barbecho']
    #total_function(input_name,crops,crop_ids,coefficients)



def total_function(input_name,crops,crop_ids,coefficients):   
    run_for_different_tech_levels(input_name,crops,crop_ids,coefficients)


def run_for_different_tech_levels(input_name,crops,crop_ids,coefficients):
    name_input_original = input_name + 'original'
    copy_input(input_name,name_input_original)
    update_input(input_name,crops,crop_ids)
    varying_technological_level(input_name,crops,crop_ids,coefficients)
    copy_input(name_input_original,input_name)


def crear_backup_input(name_input):
    input_name_original = name_input + 'Original'
    copy_input(name_input,input_name_original)
    return input_name_original


script_sequences('UBAR2004')
#run_generator_sequences('UBAR2004')