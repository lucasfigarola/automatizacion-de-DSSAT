import csv
from setup import *
from numpy import genfromtxt
from crop import *
from auxiliary_functions import *


def sequenceGenerator():

    contador = 0

    barbecho = Crop('Barbecho','')

    #--------- creacion de cultivos simples ------------
    soja = Crop('Soja','')
    maiz = Crop('Maiz','')
    trigo = Crop('Trigo','')
    girasol = Crop('Girasol','')
    colza = Crop('Colza','')
    arveja = Crop('Arveja','')
    soja2 = Crop('Soja2','')
    maiz2 = Crop('Maiz2','')

    simple_crops = []
    simple_crops.append(soja)
    simple_crops.append(maiz)
    simple_crops.append(trigo)
    #simple_crops.append(girasol)
    #simple_crops.append(colza)
    #simple_crops.append(arveja)
    #simple_crops.append(soja2)
    #simple_crops.append(maiz2)


    #--------- creacion de cultivos dobles ------------
    #cultivos = ['Soja','Maiz','Girasol','Trigo','Soja2','Maiz2','Colza','Arveja']
    cultivos = ['Soja','Maiz','Trigo','Soja2']
    matriz_de_restricciones = convertir_matriz()
    dicc_index = crear_dicc_index()
    double_crops = []

    for i in range(len(cultivos)):
        for j in range(len(cultivos)):
            secuencia = [str(cultivos[i]),str(cultivos[j])]
            if is_valid_double_crop(secuencia,dicc_index,matriz_de_restricciones):
                double_crops.append(Crop(cultivos[i],cultivos[j]))


    #--------- union de todos los cultivos simples y dobles ------------
    all_crops = simple_crops + double_crops

    path = os.path.join(my_path, 'sequence/sequence.txt')
    out = open(path, 'w')

    dicc_sequence = {}

    for i in range(len(all_crops)):
        secuencia = [all_crops[i],barbecho]
        if es_valida_la_combinacion(secuencia,dicc_index,matriz_de_restricciones):
            crop_sequence = get_list_crop(secuencia)
            if len(crop_sequence) not in dicc_sequence:
                dicc_sequence[len(crop_sequence)] = []
            if not_repeated(crop_sequence,dicc_sequence[len(crop_sequence)]):
                dicc_sequence[len(crop_sequence)].append(crop_sequence)
                out.write(str(crop_sequence) + '\n')
                contador += 1

    for i in range(len(all_crops)):
        for j in range(len(all_crops)):
            secuencia = [all_crops[i],barbecho,all_crops[j],barbecho]
            if es_valida_la_combinacion(secuencia,dicc_index,matriz_de_restricciones):
                crop_sequence = get_list_crop(secuencia)
                if len(crop_sequence) not in dicc_sequence:
                    dicc_sequence[len(crop_sequence)] = []
                if not_repeated(crop_sequence,dicc_sequence[len(crop_sequence)]):
                    dicc_sequence[len(crop_sequence)].append(crop_sequence)
                    out.write(str(crop_sequence) + '\n')
                    contador += 1

    for i in range(len(all_crops)):
        for j in range(len(all_crops)):
            for z in range(len(all_crops)):
                secuencia = [all_crops[i],barbecho,all_crops[j],barbecho,all_crops[z],barbecho]
                if es_valida_la_combinacion(secuencia,dicc_index,matriz_de_restricciones):
                    crop_sequence = get_list_crop(secuencia)
                    if len(crop_sequence) not in dicc_sequence:
                        dicc_sequence[len(crop_sequence)] = []
                    if not_repeated(crop_sequence,dicc_sequence[len(crop_sequence)]):
                        dicc_sequence[len(crop_sequence)].append(crop_sequence)
                        out.write(str(crop_sequence) + '\n')
                        contador += 1

    for i in range(len(all_crops)):
        for j in range(len(all_crops)):
            for z in range(len(all_crops)):
                for t in range(len(all_crops)):
                    secuencia = [all_crops[i],barbecho,all_crops[j],barbecho,all_crops[z],barbecho,all_crops[t],barbecho]
                    if es_valida_la_combinacion(secuencia,dicc_index,matriz_de_restricciones):
                        crop_sequence = get_list_crop(secuencia)
                        if len(crop_sequence) not in dicc_sequence:
                            dicc_sequence[len(crop_sequence)] = []
                        if not_repeated(crop_sequence,dicc_sequence[len(crop_sequence)]):
                            dicc_sequence[len(crop_sequence)].append(crop_sequence)
                            out.write(str(crop_sequence) + '\n')
                            contador += 1
    
    print(contador)
    #print(dicc_sequence[2])

    out.close()
    return dicc_sequence


def is_valid_double_crop(secuencia,dicc_index,matriz_de_restricciones):
    for i in range(len(secuencia)-1):
        crop_name1 = secuencia[i]
        crop_index1 = dicc_index[crop_name1]
        crop_name2 = secuencia[i+1]
        crop_index2 = dicc_index[crop_name2]
        if matriz_de_restricciones[crop_index1][crop_index2] == 0:
            return False
    return True


def es_valida_la_combinacion(secuencia,dicc_index,matriz_de_restricciones):
    if (repeated(secuencia)):
        return False
    for i in range(len(secuencia)-1):
        crop_name1 = secuencia[i].get_crop_end()
        crop_index1 = dicc_index[crop_name1]
        crop_name2 = secuencia[i+1].first_crop
        crop_index2 = dicc_index[crop_name2]
        if matriz_de_restricciones[crop_index1][crop_index2] == 0:
            return False
    return True


def repeated(secuencia):
    if len(secuencia) == 2:
        return False
    secuencia = delete_barbecho(secuencia)
    if secuencia.count(secuencia[0]) == len(secuencia):
        return True
    else:
        return False


def delete_barbecho(secuencia):
    secuencia_without_barbecho =[]
    for i in range(len(secuencia)):
        if secuencia[i].first_crop != 'Barbecho':
            secuencia_without_barbecho.append(secuencia[i])
    return secuencia_without_barbecho


def get_list_crop(secuencia):
    list_crop = []
    for i in range(len(secuencia)):
        list_crop = list_crop + secuencia[i].get_crop_list()
    return list_crop


def convertir_matriz():
    path = os.path.join(my_path, 'matrices/Matriz de restricciones - secuencias - Sheet1.csv')
    my_data = genfromtxt(path, delimiter=',')    
    return my_data


def crear_dicc_index():
    dicc_index = {}
    path = os.path.join(my_path, 'matrices/Matriz de restricciones - secuencias - Sheet1.csv')
    with open(path) as f:
        reader = csv.reader(f)
        for l in reader:
            dicc_index = crear_dicc_index_line(l)
            break
    return dicc_index


def crear_dicc_index_line(l):
    dicc_index = {}
    for i in range(1,len(l)):
        dicc_index[l[i]] = i
    return dicc_index


def read_list():
    path = os.path.join(my_path, 'sequence/sequence.txt')
    with open(path) as f:
        list_words = [i.strip().split(' ') for i in f]
    #print(list_words)


sequenceGenerator()
#convertir_matriz()
#crear_dicc_index()
#read_list()