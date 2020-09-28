from calculations_graphic_aux import *
import csv

def calculate_values_for_graphics(name_input,crops,coefficients,nivel_tecnologico,first_year):
    #----------- calcula los valores de Rendimiento, Rentabilidad y Emergy para graficar  ----------
    crops_without_barbecho = remove_barbecho_from_sequence(crops)
    cant_years_to_evalue = 4

    for i in range(cant_years_to_evalue):
        cant_years = 6*(i+1)
        #---------------- calcular los valores para graficar de rendimiento y rentabilidad (aux) ------------
        calculate_values_for_graphics_performance(name_input,crops_without_barbecho,coefficients,nivel_tecnologico,first_year,cant_years)



def calculate_values_for_graphics_performance(name_input,crops,coefficients,nivel_tecnologico,first_year,cant_years):
    #----------- obtengo todos los valores del rendimiento multiplicado por el coeficiente -------------
    performance = get_all_performance(name_input,crops,coefficients,nivel_tecnologico)
    #----------- calculo los valores de rendimiento por año y promedio -------------
    calculate_values_for_graphics_performance_by_year(crops,performance,nivel_tecnologico,first_year,cant_years)
    calculate_values_for_graphics_performance_by_promedio(crops,performance,nivel_tecnologico,first_year,cant_years)


#------------ obtengo todos los rendimientos -----------------
def get_all_performance(name_input,crops,coefficients,technological_level):
    name_input_cut = get_the_last_8_characters_SQX(name_input)
    path = os.path.join(my_path, 'results_files/temporary_files/' + name_input_cut + '.OSU')
    f = open(path,'r')
    lines = f.readlines()
    performance = []
    current_yield = 0
    value = 0
    for l in lines:
        info = l.split()
        if there_is_performance_on_the_line(l,name_input_cut,crops):
            current_crop = info[8]
            coefficient = get_coefficient_of_crop(coefficients,current_crop,technological_level)
            value = int(info[21])
            value = coefficient * value
            current_yield = current_yield + value
        if there_is_barbecho_on_the_line(l):
            performance.append(float(current_yield))
            current_yield = 0
    performance.append(float(current_yield)) # agrego el ultimo rendimiento
    f.close()
    return performance