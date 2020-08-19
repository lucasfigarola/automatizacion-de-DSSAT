from setup import *
import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
import csv


def create_graphic_result(tipo,cant_years,name):
    x = []
    y = []
    pid = []
    colour = []

    path = os.path.join(my_path, 'result/result_' + tipo + '_' + str(cant_years) + '.txt')
    with open(path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[1]))
            pid.append(row[2])
            colour.append(row[3])

    fig, ax = plt.subplots()
    #ax.plot(x,y, ls="", color='black', marker="o")    
    for xi, yi, pidi, colouri in zip(x,y,pid,colour):
        ax.plot(xi,yi, ls="", color=colouri, marker="o") 
        ax.annotate(str(pidi), xy=(xi,yi), color='black')

    plt.grid(True)
    plt.xlabel('Rentabilidad')
    plt.ylabel(tipo)
    plt.title('Promedio ' + name + '\n' + 'Tipo ' + name + ': ' + tipo + '\n' + 'Cantidad de Años:' + str(cant_years))

    #alto = mpatches.Patch(color='blue', label='Alto', marker="o")
    #medio = mpatches.Patch(color='green', label='Medio', marker="o")
    #bajo = mpatches.Patch(color='red', label='Bajo', marker="o")

    alto, = plt.plot([], [], label='Alto', color='blue', lw=2)
    medio, = plt.plot([], [], label='Medio', color='green', lw=2)
    bajo, = plt.plot([], [], label='Bajo', color='red', lw=2)
    plt.legend(handles=[alto,medio,bajo])

    if name == 'Emergy':
        plt.xlim((0,3))
        plt.ylim((0,3))
    path = os.path.join(my_path, 'graphic/result_' + tipo + '_' + str(cant_years) + '.png')
    plt.savefig(path)
    plt.close(fig)
    #plt.show()


def create_graphic_standard(tipo,name,sequence,cant_years):
    x = []
    y = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    cant_years = str(cant_years)
    
    path = os.path.join(my_path, 'results/' + name + '_' + cant_years + '_' + sequence + '_' + 'Bajo' + '.txt')
    with open(path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x.append(row[0])
            y.append(float(row[1]))

    path = os.path.join(my_path, 'results/' + name + '_' + cant_years + '_' + sequence + '_' + 'Medio' + '.txt')
    with open(path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x2.append(row[0])
            y2.append(float(row[1]))

    path = os.path.join(my_path, 'results/' + name + '_' + cant_years + '_' + sequence + '_' + 'Alto' + '.txt')
    with open(path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x3.append(row[0])
            y3.append(float(row[1]))


    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))

    line, = ax1.plot(x3,y3, label='Alto', color='blue', lw=2)
    line, = ax1.plot(x2,y2, label='Medio', color='green', lw=2)
    line, = ax1.plot(x,y, label='Bajo', color='red', lw=2)
    
    title = 'Secuencia: ' + sequence

    #Escala logaritmica
    #ax1.set_yscale('symlog')

    #plt.yscale('log')
    #plt.xscale('log')

    #Detalles (titulo, etc..)
    plt.grid(True)
    plt.xlabel('Tiempo')
    plt.ylabel(tipo)
    plt.title(name + '\n' + title + '\n' + 'Cantidad de Años:' + cant_years)
    plt.legend(bbox_to_anchor=(0.3,0.85), loc='center right', borderaxespad=0.)

    path = os.path.join(my_path, 'graphics/' + name + cant_years  + '_' + sequence + '_' + 'Medio' + '.png')
    plt.savefig(path)
    #plt.show()
    plt.close(fig)


def create_graphic_emergy(tipo,name,sequence,cant_years):
    x = []
    y = []
    x2 = []
    y2 = []
    x3 = []
    y3 = []

    cant_years = str(cant_years)

    path = os.path.join(my_path, 'results/' + name + '_' + cant_years + '_' + sequence + '_' + 'Bajo' + '.txt')
    with open(path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[1]))

    path = os.path.join(my_path, 'results/' + name + '_' + cant_years + '_' + sequence + '_' + 'Medio' + '.txt')
    with open(path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x2.append(float(row[0]))
            y2.append(float(row[1]))

    path = os.path.join(my_path, 'results/' + name + '_' + cant_years + '_' + sequence + '_' + 'Alto' + '.txt')
    with open(path,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=' ')
        for row in plots:
            x3.append(float(row[0]))
            y3.append(float(row[1]))

    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1), (0,0))

    plt.scatter(x3,y3, label='Alto', color='blue', s=25, marker="o")
    plt.scatter(x2,y2, label='Medio', color='green', s=25, marker="o")
    plt.scatter(x,y, label='Bajo', color='red', s=25, marker="o")

    title = 'Secuencia: ' + sequence
    
    plt.grid(True)
    plt.xlabel('Rentabilidad')
    plt.ylabel(tipo)
    plt.title(name + '\n' + title + '\n' + 'Cantidad de Años:' + cant_years)
    plt.legend(bbox_to_anchor=(0.3,0.85), loc='center right', borderaxespad=0.)
    plt.ylim((0,4.5))
    path = os.path.join(my_path, 'graphics/' + name + '_' + cant_years + '_' + sequence + '_' + 'Alto' + '.png')
    plt.savefig(path)
    plt.close(fig)