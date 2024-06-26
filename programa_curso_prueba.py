"""
El fichero calificaciones.csv contiene las calificaciones de un curso. 
Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas. 
Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en 
la al final del curso (convocatoria ordinaria). 

Escribir un programa que contenga las siguientes funciones:

1.	Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, 
donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. 
La lista tiene que estar ordenada por apellidos.

2.	Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y añada a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial 
de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

3.	Una función que reciba una lista de diccionarios como la que devuelve la función anterior 
y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. 
Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los 
exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.


Se  debe  habilitar  GIT y  crear un   repositorio  en GITHUB ,  donde se realicen  “COMMIT”  por  cada  función (actualizaciones mínimas).
"""
import csv

# 1.	Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, 
# donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. 
# La lista tiene que estar ordenada por apellidos.

def recibir_calificaciones():
    lista = []
    ruta_archivo = input("Ingrese la ruta al archivo: ")
    with open(ruta_archivo, "r", newline="") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        pos = 0
        for linea in lector_csv:
            if pos != 0:
                for i in range(2, len(lector_csv)):
                    if linea[i] == "":
                        linea[i] = "0,0"
                        # Apellidos	Nombre	Asistencia	Parcial1	Parcial2	Ordinario1	Ordinario2	Practicas	OrdinarioPracticas
                Apellidos = linea[0]
                Nombre = linea[1]
                Asistencia = linea[2]
                Parcial1 = linea[3]
                Parcial2 = linea[4]
                Ordinario1 = linea[5]
                Ordinario2 = linea[6]
                Practicas = linea[7]
                OrdinarioPracticas = linea[8]
                lista.append({
                    'Apellidos':Apellidos,
                    'nombre': Nombre,
                    'Asistencia': Asistencia,
                    'Parcial1': Parcial1,
                    'Parcial2': Parcial2,
                    'Ordinario1': Ordinario1,
                    'Ordinario2': Ordinario2,
                    'Practicas': Practicas,
                    'OrdinarioPracticas': OrdinarioPracticas,
                                })
            else:
                pos = 1
    return lista
