import os

import re

from openpyxl import Workbook
from openpyxl import load_workbook

#Acceder al archivo excel y acceder a la hoja1
libro_man = load_workbook("man.xlsx")
hoja_man = libro_man.active

#Rango de columnas/filas
rango_man = hoja_man["A1":"A50"]
rango_grupo = hoja_man["B1":"B50"]
rango_fotouno = hoja_man["C1":"C50"]
rango_fotodos = hoja_man["D1":"D50"]

#Listas
nombres_man=[]
grupos=[] 
fotouno=[]
fotodos=[] 


#Guardar el contenido de las celdas dentro de cada lista.
for celda1 in rango_man:
  for objeto1 in celda1:
    nombres_man.append(objeto1.value)

for celda2 in rango_grupo:
  for objeto2 in celda2:
    grupos.append(objeto2.value)

for celda3 in rango_fotouno:
  for objeto3 in celda3:
    fotouno.append(objeto3.value)

for celda4 in rango_fotodos:
  for objeto4 in celda4:
    fotodos.append(objeto4.value)

#Entrar al directorio de los grupos
os.chdir("C:/Users/Canal Halcón 1/Desktop/Nombres automaticos de archivos Python/grupos")

#Agregar el ".JPG" a cada valor de las listas fotouno, fotodos
#fotouno contiene la columna del excel de los numeros impartes
#fotodos contiene la columna del excel de los numeros pares
fotouno = [str(number) + ".JPG" for number in fotouno]
fotodos = [str(number) + ".JPG" for number in fotodos]


for a in os.listdir(): #Este ciclo sirve para entrar a cada grupo(carpeta)
    
  os.chdir("C:/Users/Canal Halcón 1/Desktop/Nombres automaticos de archivos Python/grupos/"+str(a)) #Aqui entraremos a cada grupo

  #Creamos una variable llamada lista, donde guardara todos los archivos del directorio actual(TODAS LAS FOTOS)
  lista=os.listdir()

  #Convertimos los valores de la lista en enteros y los guardamos en una nueva variable llamada nueva_lista
  nueva_lista = [int(re.search(r'\d+', elemento).group()) for elemento in lista]

  #Ordenamos la lista(de menor a mayor)
  nueva_lista.sort()

  #Creamos otra lista llamada lista_revertida donde convertirmos los valores de la lista nueva_lista en string agregandoles
  #al final de cada elemento el valor de ".JPG"
  lista_revertida = [str(numero) + ".JPG" for numero in nueva_lista]

  """
  Todo este procedimiento de crear 3 listas distintas se hace por un error del modulo os ya que no permite acomodar de manera
  correcta la lista desde un principio

  """

  for b in lista_revertida: #Ahora estaremos "entrando" en cada imagen
    #b toma el valor de los elementos de lista_revertida(Recordar que lista_revertida contiene todas las fotos)
    bandera=0 
    #la variable bandera será nuestro indicador si el match se cumple (0 = no cumple / 1 = cumplio)
    i=0
    #la variable i servirá para ubicar los nombres de los alumnos
    for c in fotouno:
      #c toma el valor de los elementos de la lista fotouno
      if(b == c):
        #Si se cumple la condición, significa que hubo un match entre las listas, por lo que ahora si, se cambiara el nombre de
        #la foto al nombre real de la estudiante
        os.replace(b, "C:/Users/Canal Halcón 1/Desktop/Nombres automaticos de archivos Python/gpo/"+str(nombres_man[i] + '.JPG'))
        bandera=1 #Como se cumplio el match, cambiamos el valor de bandera
      i = i + 1 #debe de estar aumentando para poder ubicar correctamente el nombre del alumno
      if(bandera==1): 
        break
        #Detemos el ciclo (for c in fotouno) para que "entremos" o cambiemos a otra de imagen de la lista_revertida
    i = 0 #Es necesario reinciar la variable i cuando se salga del ciclo(for c in fotouno)

    '''
    En caso de que se salga del ciclo(for c in fotouno) sin hacer un match, necesitamos entrar a otro ciclo(for c in fotodos).
    Si el script llega hasta aquí, significa que el valor de b contiene una foto con numeración par

    '''
    #Mismo procedimiento, solo que c tomara el valor de los elementos de la lista fotodos
    for c in fotodos:
      if(b == c):
        os.replace(b, "C:/Users/Canal Halcón 1/Desktop/Nombres automaticos de archivos Python/gpo/"+str(nombres_man[i] + ' 2.JPG'))
        bandera=1
      i = i + 1
      if(bandera==1):
        break


#libro_man.save("man.xlsx") #No es necesaria esta linea ya que no modificamos el excel
print("listo")