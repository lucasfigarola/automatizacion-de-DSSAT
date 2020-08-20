# automatizacion-de-DSSAT

Automatización del modelo de simulación de cultivos DSSAT es una herramienta creada en python que automatiza la generación de archivos requeridos por DSSAT para correr modelos.
En su forma basica, el script puede ser usado inmediatamente ingresando un nombre de un archivo .SQX que se debe encontrar en la carpeta secuence dentro de DSSAT.
En script.py estan las principales funciones para correr el script. Hay dos opciones para correr: La funcion script_sequences que corre DSSAT para cada secuencia generada en el sequence_generator. La funcion run_generator_sequences que corre DSSAT para secuencias especificas que quieras probar. 
