from acoplar import *
from auxiliary_functions import *
from graphic_standard import *
from fertilizer_calculation import *
from calculation_results import *
import re


def varying_technological_level(input_name,cultivos,cultivo_ids,coefficients):
    numero_de_niveles = 1 # cantidad incremental de niveles tecnologicos
    porcentaje_fijo = 30/numero_de_niveles
    niveles_tecnologicos_medios = get_fertilizer_value(input_name,cultivos)
    niveles_tecnologicos_bajos = calcular_nivel_tecnologico_bajo(niveles_tecnologicos_medios)  #calculo el valor de fertilizante inicial (minimo)
    niveles_tecnologicos_altos = calcular_nivel_tecnologico_alto(niveles_tecnologicos_medios)  #calculo el valor de fertilizante maximo
    valores_fertilizantes_incrementales = calcular_valor_fertilizante_incremental(niveles_tecnologicos_medios,porcentaje_fijo)  #calculo el valor de fertilizante que se ira sumando

    run_varying_ferlitizer(input_name,cultivos,coefficients,niveles_tecnologicos_bajos,niveles_tecnologicos_altos,valores_fertilizantes_incrementales)


def run_varying_ferlitizer(nombre_input,cultivos,coefficients,niveles_tecnologicos_bajos,niveles_tecnologicos_altos,valores_fertilizantes_incrementales):
    f= open('C:/DSSAT47/Sequence/' + nombre_input + '.SQX','r')
    lines = f.readlines()
    actuales_valores_fertilizantes = niveles_tecnologicos_bajos
    checker = False
    cant_nivel_tecnologico = 3
    nivel_tecnologico = 0
    first_year = get_FirstYear(nombre_input)
    for nivel_tecnologico in range(cant_nivel_tecnologico):
        print('Valores de fertilizante: ', actuales_valores_fertilizantes)
        for i, l in enumerate(lines):
            info = l.split() 
            if checker and info[11] in cultivos:
                actual_cultivo = info[11]
                actual_valor_fertilizante = actuales_valores_fertilizantes[actual_cultivo]
                if actual_valor_fertilizante < 10:
                    lines[i] = l[:31]+ str(int(actual_valor_fertilizante)) +l[32:]                
                if 10 <= actual_valor_fertilizante and actual_valor_fertilizante < 100:
                    lines[i] = l[:30]+ str(int(actual_valor_fertilizante)) +l[32:]
                if actual_valor_fertilizante >= 100:      
                    lines[i] = l[:29]+ str(int(actual_valor_fertilizante)) +l[32:]
                checker = False
            if 'FAMN' in l: 
                checker = True
        out = open('C:/DSSAT47/Sequence/' + nombre_input + '.SQX', 'w')
        out.writelines(lines)
        out.close()
        copy_SQX(nombre_input,cultivos,nivel_tecnologico)
        dssat_run()
        copy_out(cultivos,nivel_tecnologico)
        calculate_values_for_graphics(nombre_input,cultivos,coefficients,nivel_tecnologico,first_year)
        actuales_valores_fertilizantes = actualizar_valores_fertilizantes(actuales_valores_fertilizantes,valores_fertilizantes_incrementales)
    graficar_resultados(cultivos)


def graficar_resultados(cultivos):
    sequence = get_sequence_name(cultivos)
    create_graphics(sequence)

def create_graphics(sequence):
    cant_years_to_evalue = 4

    for i in range(cant_years_to_evalue):
        cant_years = 6*(i+1)
        create_graphic_rendimiento_original(sequence,cant_years)
        create_graphic_rendimiento_promedio(sequence,cant_years)



#-------------- crear grafico original ---------------
def create_graphic_rendimiento_original(sequence,cant_years):
    create_graphic_standard('Rendimiento','RendimientoOriginal',sequence,cant_years)


#-------------- crear grafico promedio ---------------
def create_graphic_rendimiento_promedio(sequence,cant_years):
    create_graphic_standard('Rendimiento','RendimientoPromedio',sequence,cant_years)