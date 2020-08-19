from auxiliary_functions import *

#-------------- conseguir la cantidad de fertilizante de un cultivo ---------------
def get_fertilizer_value(name_input,cultivos):
    f= open('C:/DSSAT47/Sequence/' + name_input + '.SQX','r')
    lines = f.readlines()
    cultivos_sin_duplicados = delete_barbecho_and_without_duplicates(cultivos)
    fertilizer_value = 0
    fertilizantes = {}
    checker = False
    j = 0
    for i, l in enumerate(lines):
        info = l.split()
        #print(info)
        if j == len(cultivos_sin_duplicados):
            break
        if checker and info[11] in cultivos_sin_duplicados:
            fertilizer_value = int(info[5]) 
            fertilizantes[info[11]] = fertilizer_value
            j += 1             
        if 'FAMN' in l: 
            checker = True
    f.close()
    return fertilizantes


def calcular_nivel_tecnologico_bajo(niveles_tecnologicos_medios):
    niveles_tecnologicos_bajos = {}
    for key in niveles_tecnologicos_medios:
        nivel_tecnologico_medio = niveles_tecnologicos_medios[key]
        niveles_tecnologicos_bajos[key] = nivel_tecnologico_medio - (nivel_tecnologico_medio * 30) / 100
    return niveles_tecnologicos_bajos


def calcular_nivel_tecnologico_alto(niveles_tecnologicos_medios):
    niveles_tecnologicos_altos = {}
    for key in niveles_tecnologicos_medios:
        nivel_tecnologico_medio = niveles_tecnologicos_medios[key]
        niveles_tecnologicos_altos[key] = nivel_tecnologico_medio + (nivel_tecnologico_medio * 30) / 100
    return niveles_tecnologicos_altos


def calcular_valor_fertilizante_incremental(niveles_tecnologicos_medios,porcentaje_fijo):
    valor_fertilizante_incremental = {}
    for key in niveles_tecnologicos_medios:
        nivel_tecnologico_medio = niveles_tecnologicos_medios[key]
        valor_fertilizante_incremental[key] = (nivel_tecnologico_medio * porcentaje_fijo) / 100
    return valor_fertilizante_incremental


def actualizar_valores_fertilizantes(actuales_valores_fertilizantes,valores_fertilizantes_incrementales):
    nuevos_valores_fertilizantes = {}
    for key in actuales_valores_fertilizantes:
        nuevos_valores_fertilizantes[key] = actuales_valores_fertilizantes[key] + valores_fertilizantes_incrementales[key]
    return nuevos_valores_fertilizantes