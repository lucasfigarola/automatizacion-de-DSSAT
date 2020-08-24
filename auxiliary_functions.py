from setup import *
import csv

def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)


def promedio(iterable):
    result=[]
    for x, y in grouped(iterable,2):
        result.append((x+y)/2)
    return result    


#----------- crea un nueva copia del input  ----------
def copy_txt(name_input,cultivos,num_nivel_tecnologico):
    f= open("C:/DSSAT47/Sequence/" + name_input + ".SQX","r")
    lines = f.readlines()
    sequence = get_sequence_name(cultivos)
    name_nivel_tecnologico = get_name_nivel_tecnologico(num_nivel_tecnologico)
    out = open('C:/DSSAT47/Sequence/' + name_input + '_' + sequence + '_' + name_nivel_tecnologico + '.SQX', 'w')
    out.writelines(lines)
    out.close()


#----------- crea un nueva copia del output  ----------
def copy_out(cultivos,num_nivel_tecnologico):
    f= open("C:/DSSAT47/Sequence/output.txt","r")
    lines = f.readlines()
    sequence = get_sequence_name(cultivos)
    name_nivel_tecnologico = get_name_nivel_tecnologico(num_nivel_tecnologico)
    out = open('C:/DSSAT47/Sequence/output' + '_' + sequence + '_' + name_nivel_tecnologico + '.txt', 'w')
    out.writelines(lines)
    out.close()    


def there_is_performance_on_the_line(line):
    b = 'MZ' in line or 'SB' in line or 'WH' in line
    return b    


#------------ obtengo los coeficientes de todos los cultivos para un nivel tecnologico -----------------
def get_all_coefficients():
    coefficients = {}
    path = os.path.join(my_path, "matrices/Matriz Rentabilidad - Coef Correccion de Rendimiento.csv")
    with open(path) as f:
        reader = csv.reader(f)
        cant_nivel_tecnologico = 3  # cantidad de niveles tecnologicos
        for l in reader:
            if 'Maiz' in l:
                coefficients['Maiz'] = []
                for i in range(cant_nivel_tecnologico):
                    coefficient = l[i+1]
                    coefficients['Maiz'].append(coefficient)
            if 'Soja' in l:
                coefficients['Soja'] = []
                for i in range(cant_nivel_tecnologico):
                    coefficient = l[i+1]
                    coefficients['Soja'].append(coefficient)
            if 'Soja2' in l:
                coefficients['Soja2'] = []
                for i in range(cant_nivel_tecnologico):
                    coefficient = l[i+1]
                    coefficients['Soja2'].append(coefficient)
            if 'Girasol' in l:
                coefficients['Girasol'] = []
                for i in range(cant_nivel_tecnologico):
                    coefficient = l[i+1]
                    coefficients['Girasol'].append(coefficient)
            if 'Trigo' in l:
                coefficients['Trigo'] = []
                for i in range(cant_nivel_tecnologico):
                    coefficient = l[i+1]
                    coefficients['Trigo'].append(coefficient)
    return coefficients 


#------------ obtengo el coeficiente del cultivo que esta en la linea -----------------
def get_coefficient_of_the_line(line,coefficients,nivel_tecnologico):
    coefficient = 0
    if 'MZ' in line:
        coefficient =  coefficients['Maiz']
    if 'SB' in line:
        coefficient =  coefficients['Soja']
    if 'WH' in line:
        coefficient =  coefficients['Trigo']
    return float(coefficient[nivel_tecnologico])  


#-------------- conseguir el i-esimo cultivo del input ---------------
def get_cultivo(name_input,num_cultivo):
    f= open('C:/DSSAT47/Sequence/' + name_input + '.SQX','r')
    lines = f.readlines()
    checker = None 
    crop = 'None'
    for i, l in enumerate(lines):
        info = l.split()  
        if checker and info[1] == str(num_cultivo):  
            crop = info[4]                      
            checker = None
            break
        if '*TREATMENTS' in l: 
            checker = True
    f.close()
    return crop


#-------------- conseguir el primer año del input ---------------
def get_FirstYear(inputName):
    f= open("C:/DSSAT47/Sequence/" + inputName + ".SQX","r")
    lines = f.readlines()
    result = 0
    b = 0     
    for l in lines:
        if len(l.strip()) != 0:
            if b == 2:
                firstYear = l.split()[5]    
                firstYear = firstYear[:2]                 
                result = int(firstYear)          
                b = 0
            if b == 1:
                b +=1            
            if 'SIMULATION CONTROLS' in l:
                b += 1     
    f.close()
    return result


#-------------obtener el primer año y la cantidad de años totales --------------
def get_NYEARS(inputName):
    f= open("C:/DSSAT47/Sequence/" + inputName + ".SQX","r")
    lines = f.readlines()
    result = 0
    b = 0     
    for l in lines:
        if len(l.strip()) != 0:
            if b == 2:
                NYEARS = int(l.split()[2])
                result = NYEARS              
                b = 0
            if b == 1:
                b +=1            
            if 'SIMULATION CONTROLS' in l:
                b += 1     
    f.close()
    return result

#-------------- conseguir el primer cultivo del input ---------------
def get_first_cultivo(name_input):
    crop = get_cultivo(name_input,1)
    return crop

#-------------- conseguir el segundo cultivo del input ---------------
def get_second_cultivo(name_input):
    crop = get_cultivo(name_input,3)
    return crop


#----------- Modifica una linea de TREATMENTS de un cultivo ----------
def change_line(name_input,num_line,crop_name,id_crop):    
    f= open('C:/DSSAT47/Sequence/' + name_input + '.SQX','r')
    lines = f.readlines()
    checker = None 
    difference = 0
    for i, l in enumerate(lines):
        info = l.split()
        if checker and info[1] == str(num_line):                        
            #if len(crop_name) < len(info[4]):                
                #difference = len(info[4]) - len(crop_name)
                #print(difference) 
                #m = crop_name.ljust(4+difference)   
                #lines[i] = l[:9] + crop_name + l[13:36] + str(id_crop) + l[37:48] + str(id_crop) + l[49:72] + str(id_crop) + l[73:]
            lines[i] = l[:9] + crop_name + l[13:36] + str(id_crop) + l[37:48] + str(id_crop) + l[49:72] + str(id_crop) + l[73:]
            checker = None
        if '*TREATMENTS' in l: 
            checker = True
    out = open('C:/DSSAT47/Sequence/' + name_input + '.SQX', 'w')
    out.writelines(lines)
    out.close()


#----------- Modifica el MH de una linea de TREATMENTS ----------
def change_MH(name_input,num_line,mh):
    f= open('C:/DSSAT47/Sequence/' + name_input + '.SQX','r')
    lines = f.readlines()
    checker = None 
    for i, l in enumerate(lines):
        info = l.split()
        if checker and info[1] == str(num_line):           
            lines[i] = l[:69] + str(mh) + l[70:]
            checker = None
        if '*TREATMENTS' in l: 
            checker = True
    out = open('C:/DSSAT47/Sequence/' + name_input + '.SQX', 'w')
    out.writelines(lines)
    out.close() 
    f.close()  


def change_cantYears(name_input,cantYears):
    f= open('C:/DSSAT47/Sequence/' + name_input + '.SQX','r')
    lines = f.readlines()
    b = 0     
    for i, l in enumerate(lines):
        if len(l.strip()) != 0:
            if b == 2:
                if cantYears < 10:
                    lines[i] = l[:18] + ' ' + str(cantYears) + l[20:]             
                if 10 <= cantYears and cantYears < 100:
                    lines[i] = l[:18] + str(cantYears) + l[20:]  
                if cantYears >= 100:      
                    lines[i] = l[:17] + str(cantYears) + l[20:]            
                b = 0
            if b == 1:
                b +=1            
            if 'SIMULATION CONTROLS' in l:
                b += 1    
    out = open('C:/DSSAT47/Sequence/' + name_input + '.SQX', 'w')
    out.writelines(lines)
    out.close() 
    f.close()  



def get_name_nivel_tecnologico(nivel_tecnologico):
    if nivel_tecnologico == 0:
        return 'Bajo'
    if nivel_tecnologico == 1:
        return 'Medio'
    if nivel_tecnologico == 2:
        return 'Alto'


def create_dicc_ids(name_input):
    f= open('C:/DSSAT47/Sequence/' + name_input + '.SQX','r')
    lines = f.readlines()
    checker = None
    dicc_ids = {}
    for i, l in enumerate(lines):
        info = l.split()
        if checker == True and len(l.strip()) == 0:
            break
        if checker == True:
            dicc_ids[info[15]] = info[0]
        if '@P PDATE EDATE  PPOP' in l: # Llegue a la matriz CULTIVARS
            checker = True
        if 'FA IB0001' in l: 
            dicc_ids['Barbecho'] = info[0]
    f.close()
    return dicc_ids


def update_input(name_input,cultivos,cultivo_ids):
    f= open('C:/DSSAT47/Sequence/' + name_input + '.SQX','r')
    lines = f.readlines()
    checker = None 
    j = 0
    for i, l in enumerate(lines):
        if j == len(cultivos):
            checker = None
        if checker:    
            crop_name = cultivos[j]
            if crop_name == 'Barbecho':          
                next_crop = get_next_crop(cultivos,j)  
                lines[i] = create_line_barbecho(l,crop_name,next_crop,cultivo_ids)
            else:
                lines[i] = create_line_cultivo(l,crop_name,cultivo_ids)
            j += 1            
        if '@N R O C TNAME' in l: # Llegue a la matriz TREATMENTS
            checker = True
    out = open('C:/DSSAT47/Sequence/' + name_input + '.SQX', 'w')
    out.writelines(lines)
    out.close()


def create_line_barbecho(l,crop_name,next_crop,cultivo_ids): 
    mh = cultivo_ids[next_crop]
    line = l[:9] + crop_name + l[17:36] + str(cultivo_ids[crop_name]) + l[37:48] + str(0) + l[49:54] + str(0) + l[55:69] + str(mh) + l[70:72] + str(cultivo_ids[crop_name]) + l[73:]
    return line


def create_line_cultivo(l,crop_name,cultivo_ids):
    info = l.split()
    #print(crop_name)
    #print(info)
    if len(crop_name) > len(info[4]): 
        difference = len(crop_name) - len(info[4]) 
        line = l[:9] + crop_name + l[(9+len(crop_name)):36] + str(cultivo_ids[crop_name]) + l[37:48] + str(cultivo_ids[crop_name]) + l[49:54] + str(cultivo_ids[crop_name]) + l[55:69] + str(0) + l[70:72] + str(cultivo_ids[crop_name]) + l[73:]
    if len(crop_name) < len(info[4]): 
        difference = len(info[4]) - len(crop_name) 
        crop_name_with_spaces = crop_name.ljust(5+difference)  # crea espacios
        line = l[:9] + crop_name_with_spaces + l[(9+len(crop_name_with_spaces)):36] + str(cultivo_ids[crop_name]) + l[37:48] + str(cultivo_ids[crop_name]) + l[49:54] + str(cultivo_ids[crop_name]) + l[55:69] + str(0) + l[70:72] + str(cultivo_ids[crop_name]) + l[73:]
    else:
        line = l[:9] + crop_name + l[(9+len(crop_name)):36] + str(cultivo_ids[crop_name]) + l[37:48] + str(cultivo_ids[crop_name]) + l[49:54] + str(cultivo_ids[crop_name]) + l[55:69] + str(0) + l[70:72] + str(cultivo_ids[crop_name]) + l[73:]
    return line


def add_line(nombre_input, numero_linea):
    add_linea_SQX(nombre_input, numero_linea)
    add_linea_Batch(nombre_input, numero_linea)


def add_linea_SQX(nombre_input, numero_linea):
    f = open('C:/DSSAT47/Sequence/' + nombre_input + '.SQX','r')
    lines = f.readlines()
    f.close()

    lines.insert(12+numero_linea,' 1 ' + str(numero_linea+1) + ' 1 0 Maiz                       2  1  0  1  2  0  2  0  0  0  0  0  2\n')

    f = open('C:/DSSAT47/Sequence/' + nombre_input + '.SQX','w')
    f.writelines(lines)
    f.close()


def add_linea_Batch(nombre_input, numero_linea):
    f= open("C:/DSSAT47/DSSBatch.v47","r")
    lines = f.readlines()
    f.close()
    line_filex = 12 + numero_linea
    lines.insert(line_filex,'C:\\DSSAT47\\Sequence\\' + nombre_input + '.SQX' + '                                                               1      1      ' + str(numero_linea+1) + '      1      0\n')
    #lines.insert(14,r'C:\DSSAT47\Sequence\U' + 'BAR2001.SQX                                                                 1      1      ' + str(numero_linea+1) + '      1      0\n')

    f= open("C:/DSSAT47/DSSBatch.v47","w")
    f.writelines(lines)
    f.close()


def get_sequence_name(cultivos):
    name_sequence = ''
    for i in range(len(cultivos)):
        if cultivos[i] == 'Soja2':
            name_sequence = name_sequence + 'S2'
        elif cultivos[i] == 'Barbecho':
            if i != len(cultivos)-1:
                name_sequence = name_sequence + '-'
        else:
            if i < len(cultivos)-1 and cultivos[i+1] != 'Barbecho':
                name_sequence = name_sequence + cultivos[i][0] + '&'
            else:
                name_sequence = name_sequence + cultivos[i][0]
    return name_sequence


def get_name_nivel_tecnologico(num_nivel_tecnologico):
    if num_nivel_tecnologico == 0:
        return 'Bajo'
    if num_nivel_tecnologico == 1:
        return 'Medio'
    if num_nivel_tecnologico == 2:
        return 'Alto'


def get_next_crop(cultivos,j):
    if j == len(cultivos)-1:
        return cultivos[0]
    else:
        return cultivos[j+1]


def delete_barbecho_and_without_duplicates(cultivos):
    cultivos_sin_duplicados = list(set(cultivos))
    if 'Barbecho' in cultivos_sin_duplicados:
        cultivos_sin_duplicados.remove('Barbecho')
    return cultivos_sin_duplicados


def remove_barbecho_from_sequence(sequence):
   return [value for value in sequence if value != 'Barbecho']


def get_colour(nivel_tecnologico):
    if nivel_tecnologico == 'Bajo':
        return 'red'
    if nivel_tecnologico == 'Medio':
        return 'green'
    if nivel_tecnologico == 'Alto':
        return 'blue'


def get_promedio_total(values):
    promedio = sum(values)/len(values)
    return promedio


def actualizar_fechas(name_input,cultivos,first_year):
    f= open('C:/DSSAT47/Sequence/' + name_input + '.SQX','r')
    lines = f.readlines()
    checker = None 
    current_year = first_year
    for i, l in enumerate(lines):
        info = l.split()
        if checker and len(l.strip()) == 0:
            checker = None
        if checker and info[15] in cultivos:    
            index_cultivo = get_index_cultivo(info[15],cultivos)
            lines[i] = l[:3]+ str(int(current_year+index_cultivo)) +l[5:]
        if '@P PDATE EDATE' in l: # Llegue a la matriz PLANTING DETAILS
            checker = True
    out = open('C:/DSSAT47/Sequence/' + name_input + '.SQX', 'w')
    out.writelines(lines)
    out.close()


def get_index_cultivo(crop,cultivos):
    j = 0
    for i in range(len(cultivos)):
        if crop == cultivos[i]:
            return j
        if cultivos[i] != 'Barbecho':
            j += 1


def calculate_soil_damage(l):
    performance = int(l.split()[6])
    topwt = int(l.split()[5])
    soil_damage = (topwt - performance)/1000 
    return soil_damage