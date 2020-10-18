from setup import *
from auxiliary_functions import *
import csv

#------------ calculo los rendimientos por año -----------------
def calculate_values_for_graphics_performance_by_year(cultivos,performance,nivel_tecnologico,first_year,cant_years):
    calculate_values_for_graphics_by_year(cultivos,performance,nivel_tecnologico,first_year,cant_years,'Rendimiento')
    

#------------ calculo los rendimientos por promedio -----------------
def calculate_values_for_graphics_performance_by_promedio(cultivos,performance,nivel_tecnologico,first_year,cant_years):
    calculate_values_for_graphics_by_promedio(cultivos,performance,nivel_tecnologico,first_year,cant_years,'Rendimiento')
    

def calculate_values_for_graphics_by_year(cultivos,values,nivel_tecnologico,first_year,cant_years,name):
    sequence = get_sequence_name(cultivos)
    print(cultivos)
    print(sequence)
    name_nivel_tecnologico = get_name_nivel_tecnologico(nivel_tecnologico)
    path = os.path.join(my_path, 'results/' + name + 'Original' + '_' + str(cant_years) + '_' + sequence + '_' + name_nivel_tecnologico + '.txt' )
    f = open(path,'w')
    result=[]
    for i in range(cant_years):
        result.append(first_year+i)
    for index in range(cant_years):
        f.write(str(result[index]) + " " + str(values[index]) + "\n")
        if index == len(values)-1: 
            break           
    f.close()    


def calculate_values_for_graphics_by_promedio(cultivos,values,nivel_tecnologico,first_year,cant_years,name):
    sequence = get_sequence_name(cultivos)
    name_nivel_tecnologico = get_name_nivel_tecnologico(nivel_tecnologico)
    path = os.path.join(my_path, 'results/' + name + 'Promedio' + '_' + str(cant_years) + '_' + sequence + '_' + name_nivel_tecnologico + '.txt')
    f = open(path,'w')
    #----------- calculo los promedios --------------
    promedios = promedio(values)
    years=[]    
    cant_year_prom = int(cant_years/2)
    for i in range(cant_year_prom):
        years.append(first_year+2*i)
    for index in range(cant_year_prom):
        f.write(str(years[index]) + "-" + str(years[index]+1) + " " + str(promedios[index]) + "\n")
        if index == len(promedios)-1: 
            break           
    f.close()  
