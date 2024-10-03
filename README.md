# Automatic_names
Nombres automaticos para fotos de toga y birrete de graduación

Este script de python fue diseñado para los fotografos que hagan el trabajo de tomar fotos de graduación.

La creación de este script fue porque en mi trabajo tuvimos que tomar las fotos de toga y birrete de la
generación que se graduó en el semestre ENE-JUN 2024. Eran aproximadamente 30 grupos y cuando era hora
de tomar fotos a un grupo, los alumnos no llegaban en orden como viene en las listas del grupo, por lo
que me di la tarea de generar una manera de cambiar el nombre de las fotos default, a el nombre del
estudiante de manera automatizada.

REQUISITOS
Para poder usar este script, es necesario contar con Python

PROCESO
Primero, es necesario contar con las listas de cada grupo en archivos de Excel
Las listas deben ir acomodadas de la siguiente manera:

A        B      C              d
Nombre   Grupo  numero_impar   numero_par


Como los alumnos no llegan de manera ordenada, a la hora de tomar la foto al primer estudiante que llegue, tomarle dos fotos.
Preguntarle su nombre.
Buscarlo en el Excel y en la celda nC escribir numero impar y en la celda nD escribir la continuación del numero impar

Explicación de la enumeración
Como son dos fotos por alumno, por eso en la columna C debe de ir la primera foto(numero impar) y la segunda foto(numero par)
Ejemplo
Silvestre  333  1  2
Eduardo  333  3  4  

Una vez tomada las fotos, cambias las directorios donde estan tus fotos y el directorio donde quieres guardar las fotos ya con nombres de los
estudiantes

Guardar el excel en un directorio donde este el script

Ejecutar el script.


