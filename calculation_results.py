from calculations_graphic_aux import *
import csv

def calculate_values_for_graphics(name_input,cultivos,coefficients,nivel_tecnologico,first_year):
    #----------- calcula los valores de Rendimiento, Rentabilidad y Emergy para graficar  ----------

    #----------- obtengo todos los costos para un nivel tecnologico -------------
    costos = get_all_costos(nivel_tecnologico)

    cant_years_to_evalue = 4

    for i in range(cant_years_to_evalue):
        cant_years = 6*(i+1)
        #---------------- calcular los valores para graficar de rendimiento y rentabilidad (aux) ------------
        calculate_values_for_graphics_performance(cultivos,coefficients,nivel_tecnologico,first_year,cant_years)



def calculate_values_for_graphics_performance(cultivos,coefficients,nivel_tecnologico,first_year,cant_years):
    #----------- obtengo todos los valores del rendimiento multiplicado por el coeficiente -------------
    performance = get_all_performance(coefficients,nivel_tecnologico)
    #----------- calculo los valores de rendimiento por año y promedio -------------
    calculate_values_for_graphics_performance_by_year(cultivos,performance,nivel_tecnologico,first_year,cant_years)
    calculate_values_for_graphics_performance_by_promedio(cultivos,performance,nivel_tecnologico,first_year,cant_years)


#------------ obtengo todos los rendimientos -----------------
def get_all_performance(coefficients,nivel_tecnologico):
    f = open('C:/DSSAT47/Sequence/output.txt','r')
    lines = f.readlines()
    performance = []
    value = 0
    for l in lines:
        if there_is_performance_on_the_line(l):
            coefficient = get_coefficient_of_the_line(l,coefficients,nivel_tecnologico)
            value = int(l.split()[6])
            value = coefficient * value
            performance.append(float(value))
    f.close()
    return performance