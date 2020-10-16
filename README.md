# Herramienta para automatización de DSSAT

- Lucas A. Figarola: lfigarola@dc.uba.ar 
- Felipe Ghersa: felipeghersa@agro.uba.ar
- Rodrigo Castro: rcastro@dc.uba.ar
- Diego O. Ferraro: ferraro@agro.uba.ar

*Universidad de Buenos Aires (UBA), Facultad de Ciencias Exactas y Naturales, Departamento de Computación. CONICET, Instituto de Ciencias de la Computación (ICC)*

*Universidad de Buenos Aires (UBA), Facultad de Agronomía, Cátedra de Cerealicultura. UBA-CONICET, Instituto de Investigaciones Fisiológicas y Ecológicas Vinculadas a la Agricultura (IFEVA)*

## Acerca de:

La herramienta de automatización de [DSSAT](https://dssat.net/) (Decision Support Systems for Agrotechnology Transfer), un programa de simulación de rendimiento de cultivos, fue desarrollada en Python 3 y permite automatizar la parametrización de variables de manejo (elección de cultivos en una secuencia, nivles de fertilización y aplicación de fitosanitarios), así como la generación de archivos requeridos para correr el programa.

A partir de una lista de cultivos C={C_1,…,C_c } se generan todas las combinaciones o secuencias S={S_1,…,S_s} de 1 a 4 cultivos sucesivos. Por razones agronómicas y de uso del suelo, es necesario generar reglas que restrinjan el conjunto de secuencias que serán simuladas. De este modo, un conjunto de restricciones sobre la generación de secuencias es la imposibilidad de sembrar ciertos cultivos mientras que haya otro cultivo sin cosechar en el lote simulado. Por ejemplo, en la localidad de Pergamino, el maíz se siembra a mediados de septiembre, mientras que el trigo se cosecha hacia fines de noviembre. Como consecuencia, surge una imposibilidad de sembrar el maíz como cultivo sucesivo a trigo. La Figura 1 muestra un grafo que representa las transiciones factibles en función de la fecha de siembra y fecha de cosecha para un conjunto de cultivos teóricos C_c.

![Figura 2](/img/Grafo_DSSAT.png)

En función de las secuencias seleccionadas, utilizando los criterios de factibilidad, se procede a construir estructuras de datos necesarias para ejecutar DSSAT. En la Figura 2, se presenta el flujo de información para la automatización de DSSAT que comienza con la generación secuencias agronómicamente factibles. Luego, la aplicación requiere que se defina el sitio (i.e. clima y suelo) así como los cultivares y las variables de manejo mediante un conjunto de archivos de texto. Dichos archivos alimentan el módulo principal de simulación, que luego predice un conjunto de variables de desempeño productivo y ambiental como el rendimiento, el uso del agua o el uso y lixiviación de nutrientes. De este modo, es necesario generar los coeficientes genéticos de cultivares para las especies seleccionadas en las secuencias, las variables diarias de las series climáticas y las características de los perfiles del suelo. Estos archivos no serán modificados en la automatización de modo que pueden ser generados de forma manual o utilizando a la interfaz gráfica que provee DSSAT (i.e. GenCalc para coeficientes genéticos de cultivares, Weatherman para series climáticas y SBuild para características del suelo).

A partir de esta información, se procede con la generación de un archivo .SQX que DSSAT toma como entrada para simular en modo de secuencia. A diferencia del modo de experimento o simulación de temporada, la secuencia simula las condiciones iniciales del cada cultivo de manera sucesiva, de modo que utiliza los valores de salida de condiciones del suelo en tiempo t-1 para simular el cultivo en tiempo t. Este archivo suele generarse manualmente o mediante la interfaz gráfica de DSSAT, XBuild [9]. En el archivo .SQX es necesario especificar las características de los perfiles del suelo, la serie climática y los cultivares de cada especie que serán utilizados en la simulación. Asimismo, se deben indicar detalles de siembra para cada cultivo (i.e. fecha, densidad, profundidad, y distribución, dirección y distancia entre hileras). Por último, es necesario indicar los detalles de la fertilización (i.e. fecha, producto, método, profundidad y cantidad). 

![Flujo](//Flujo_DSSAT.png)

Dado que se quiere evaluar el desempeño de distintas combinaciones de variables de manejo (en particular, secuencias de cultivo y niveles tecnológicos definidos por cantidad y tipo de fertilizante y fitosanitarios aplicados) mediante scripts de Python se modificará la secuencia de cultivos S_s y la cantidad de fertilizante aplicado Q_qfc, donde q = 1,...,Q es la cantidad correspondiente a nivel tecnológico bajo, medio o alto, del tipo de fertilizante f = 1,...,F, para el cultivo c = 1,...,C. La secuencia simulada será modificada a partir de la matriz de tratamientos en el archivo .SQX. La cantidad de fertilizante aplicado será modificada utilizando un criterio de ±30% a partir del nivel medio definido en el archivo .SQX inicial para cada cultivo simulado [11]. Este valor se puede modificar en función de los requerimientos de simulación. Luego, para ejecutar DSSAT desde línea de comando, se generó un script para crear un archivo Batch correspondiente a la secuencia simulada (ver código en la Sección Acceso).

Por último, dado que DSSAT simula el rendimiento alcanzable (i.e. limitado por agua y nutrientes), se definieron coeficientes de corrección del rendimiento para obtener un valor estimado del rendimiento actual (i.e. limitado por recursos y efectos de adversidades biológicas). Estos coeficientes se definieron en función del nivel tecnológico aplicado, simulando el efecto de la aplicación de fitosanitarios sobre el rendimiento.


## Requerimientos de Instalación:

La herramienta de automatización fue desarrollada en **Python 3**.

- Paquetes requeridos:
  - Matplotlib
  - Numpy

Es necesario contar con una instalación de **DSSAT**, solo disponible para Microsoft Windows. Para descargar DSSAT es necesario ingresar a la página (https://apps.agapps.org/ide/serial/index.php/request?sft=3) y solicitar a los desarrolladores el envío del instalador por correo electrónico. Junto con el instalador se envian los manuales de instrucciones así como referencias de uso del software.

![DSSAT](/img/DSSAT_Main.png)

## Insumos


- Suelo
- Clima
- Genotipo
- SQX inicial
- Matriz de restricciones

## Requerimientos .SQX

  Se debe respetar los ids de cada cultivo. Ejemplo:
  Para la matriz treatments los valores de CU, MP, MF deben corresponder al valor del id del cultivo. Ademas se debe tener dos lineas para esta matriz como en el siguiente ejemplo:
  
  ![DSSAT](/img/treatments.png)
  
  En cultivar el @C debe ser el id del cultivo.
  
  ![DSSAT](/img/cultivars.png)
  
  En planting details el @P debe ser el id del cultivo.
  
  ![DSSAT](/img/planting.png)
  
  En fertilizers el @F debe ser el id del cultivo.
  
  ![DSSAT](/img/fertilizers.png)
  
  En harvest details el @H debe ser el id del cultivo.
  
  ![DSSAT](/img/harvest_details.png)

## Instrucciones para correr la herramienta
 
 Ejecutar el archivo script.py
 
 En su forma basica, el script puede ser usado inmediatamente ingresando un nombre de un archivo .SQX que se debe encontrar en la carpeta secuence dentro de DSSAT.
En script.py estan las principales funciones para correr el script. Hay dos opciones para correr: La funcion script_sequences que corre DSSAT para cada secuencia generada en el sequence_generator. La funcion run_generator_sequences que corre DSSAT para secuencias especificas que quieras probar. 

## Salida: Prueba de Concepto
