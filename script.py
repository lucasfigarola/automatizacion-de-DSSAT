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


def script_sequences(name_input):
    name_input_original = name_input
    name_input = name_input + 'aux'
    copy_input(name_input_original,name_input)
    modify_batch(name_input)
    copy_batch()

    crop_ids = create_dicc_ids(name_input)
    coefficients = get_all_coefficients()

    first_year = get_FirstYear(name_input)
    dicc_sequence = sequenceGenerator()
    num_line = 2
    for i in range(2,13):
        sequences = dicc_sequence[i]
        for j in range(len(sequences)):
            crops = sequences[j]
            print(crops)
            total_function(name_input,crops,crop_ids,coefficients)
        add_line(name_input, num_line)
        num_line += 1
        add_line(name_input, num_line)
        num_line += 1

    restore_batch()


def run_generator_sequences(input_name):

    input_name_original = input_name
    input_name = input_name + 'aux'
    copy_input(input_name_original,input_name)
    modify_batch(input_name)
    copy_batch()

    cultivo_ids = create_dicc_ids(input_name)
    coefficients = get_all_coefficients()

    first_year = get_FirstYear(input_name)

    cultivos = ['Soja','Barbecho']
    total_function(input_name,cultivos,cultivo_ids,coefficients)

    cultivos = ['Maiz','Barbecho']
    #total_function(input_name,cultivos,cultivo_ids,coefficients)

    cultivos = ['Trigo','Barbecho']
    #total_function(input_name,cultivos,cultivo_ids,coefficients)


    numero_linea = 2
    add_line(input_name, numero_linea)
    numero_linea += 1

    cultivos = ['Trigo','Soja2','Barbecho']
    total_function(input_name,cultivos,cultivo_ids,coefficients)

    add_line(input_name, numero_linea)
    numero_linea += 1

    cultivos = ['Maiz','Barbecho','Soja','Barbecho']
    #total_function(input_name,cultivos,cultivo_ids,coefficients)

    cultivos = ['Soja','Barbecho','Trigo','Barbecho']
    #total_function(input_name,cultivos,cultivo_ids,coefficients)

    cultivos = ['Maiz','Barbecho','Trigo','Barbecho']
    #total_function(input_name,cultivos,cultivo_ids,coefficients)


    add_line(input_name, numero_linea)
    numero_linea += 1
    add_line(input_name, numero_linea)
    numero_linea += 1

    #cultivos = ['Maiz','Barbecho','Trigo','Barbecho','Soja','Barbecho']
    #total_function(input_name,cultivos,cultivo_ids,coefficients)

    cultivos = ['Trigo','Soja2','Barbecho','Trigo','Soja2','Barbecho']
    total_function(input_name,cultivos,cultivo_ids,coefficients)

    restore_batch()


def total_function(input_name,crops,crop_ids,coefficients):
    #input_name_original = crear_backup_input(input_name)  # crear backup del input    
    run_for_different_tech_levels(input_name,crops,crop_ids,coefficients)
    #graficar_todos_los_resultados()


def run_for_different_tech_levels(input_name,crops,crop_ids,coefficients):
    name_input_original = input_name + 'original'
    copy_input(input_name,name_input_original)
    update_input(input_name,crops,crop_ids)
    varying_technological_level(input_name,crops,crop_ids,coefficients)
    copy_input(name_input_original,input_name)


def crear_backup_input(nombre_input):
    input_name_original = nombre_input + 'Original'
    copy_input(nombre_input,input_name_original)
    return input_name_original


#script_sequences('UBAR2002')
#generar_grafico()
run_generator_sequences('UBAR2004')