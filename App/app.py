"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista .
"""

import config as cf
import sys
import csv
from ADT import list as lt
from DataStructures import listiterator as it
from DataStructures import liststructure as lt
from Sorting import selectionsort as ss
from Sorting import shellsort as shs


from time import process_time 


def loadCSVFile (file, tipo_lista, cmpfunction=None, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file
            Archivo csv del cual se importaran los datos
        sep = ";"
            Separador utilizado para determinar cada objeto dentro del archivo
        Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None  
    """
    if tipo_lista == 1:
        lst = lt.newList("ARRAY_LIST") #Usando implementacion arraylist
    else:
        lst = lt.newList("SINGLE_LINKED") #Usando implementacion arraylist
    #lst = lt.newList() #Usando implementacion linkedlist
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lt.addLast(lst,row)
    except:
        print("Hubo un error con la carga del archivo")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return lst


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("5- Consultar elementos ordenados por un criterio")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if lst['size']==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0
        iterator = it.newIterator(lst)
        while  it.hasNext(iterator):
            element = it.next(iterator)
            if criteria.lower() in element[column].lower(): #filtrar por palabra clave 
                counter+=1           
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def less(element1, element2):
    if int(element1['id']) < int(element2['id']):
        return True
    return False

def greater(element1, element2):
    if int(element1['id']) > int(element2['id']):
        return True
    return False


def cmpVoteAverage_less (movie1, movie2):
    return ( float(movie1['vote_average']) > float(movie2['vote_average']))

def cmpVoteAverage_greater (movie1, movie2):
    return ( float(movie1['vote_average']) < float(movie2['vote_average']))


def cmpVoteCount_less(movie1, movie2):
    return (float(movie1['vote_count']) > float(movie2['vote_count']))


def cmpVoteCount_greater(movie1, movie2):
    return (float(movie1['vote_count']) < float(movie2['vote_count']))

def countElementsByCriteria(criteria, column, lst1, lst2):
    """
    Retorna la cantidad de elementos que cumplen con un criterio para una columna dada
    """
    moviesCasting = lst2
    moviesDetails = lst1
    i = 1
    tamanio_casting = lt.size(moviesCasting)
    peliculasDirigidas = []
    suma = 0
    while i <= tamanio_casting:
        pelicula = lt.getElement(moviesCasting, i)
        director = pelicula['director_name']
        id_pelicula = pelicula['id']
        if director == criteria:
            j = 1
            tamanio_details = lt.size(moviesDetails)
            while j <= tamanio_details:
                p = lt.getElement(moviesDetails, j)
                id_p = p['id']
                nombre_pelicula = p['original_title']
                voto = p['vote_average']
                if id_p == id_pelicula:
                    peliculasDirigidas.append(nombre_pelicula)
                    suma += float(voto)
                j += 1
        i += 1
    promedio = suma / len(peliculasDirigidas)
    return peliculasDirigidas,len(peliculasDirigidas), promedio



def orderElementsByCriteria(cant_peliculas, orden, cmpfunction, tipo_lista):
    """
    Retorna una lista con cierta cantidad de elementos ordenados por el criterio
    """
    if tipo_lista == 1:
        tipo_lista = 'ARRAY_LIST'
    else:
        tipo_lista = 'SINGLE_LINKED'

    if cmpfunction == 1:
        if orden == 1:
            cmpfunction = cmpVoteAverage_less
        else:
            cmpfunction = cmpVoteAverage_greater
    else:
        if orden == 1:
            cmpfunction = cmpVoteCount_less
        else:
            cmpfunction = cmpVoteCount_greater
    
    if orden == 1:
        orden = less
    else:
        orden = greater

    movielist = loadCSVFile("Data/theMoviesdb/prueba2.csv", tipo_lista, orden) #llamar funcion cargar datos
    shs.shellSort(movielist, cmpfunction)
    sublista = lt.subList(movielist, 1, cant_peliculas)
    i = 1
    nombres_peliculas = []
    while i <= cant_peliculas:
        elemento = lt.getElement(sublista, i)
        nombres_peliculas.append(elemento['original_title'])
        i += 1
    return nombres_peliculas
    
def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados

    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista1 = lt.newList()   # se require usar lista definida
    lista2 = lt.newList() 

    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                tipo_lista = int(input('Que tipo de lista quiere? (1) ARRAY_LIST o (2) SINGLE_LINKED: '))
                lista1 = loadCSVFile("Data/theMoviesdb/prueba2.csv",tipo_lista) #llamar funcion cargar datos
                print("Datos cargados, ",lista1['size']," elementos cargados")
                lista2 = loadCSVFile("Data/theMoviesdb/prueba.csv", tipo_lista) #llamar funcion cargar datos
                print("Datos cargados, ",lista2['size']," elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene ",lista1['size']," elementos")
            elif int(inputs[0])==3: #opcion 3
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    criteria =input('Ingrese el nombre del director que desea buscar: \n')
                    counter=countElementsFilteredByColumn(criteria, "nombre", lista1, lista2) #filtrar una columna por criterio  
                    print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                if lista2==None or lista2['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:
                    criteria =input('Ingrese el nombre del director: \n')
                    column = 'vote_average'
                    counter=countElementsByCriteria(criteria,column,lista1, lista2)
                    print("La lista de todas las películas dirigidas por " + criteria + " es:")
                    for i in counter[0]:
                        print(i)
                    print("El total de películas dirigidas por " + criteria + " es: " + str(counter[1]))
                    print("El promedio de la calificación de sus peliculas es de: " + str(counter[2]))

            elif int(inputs[0])==5: #opcion 5
                if lista1==None or lista1['size']==0: #obtener la longitud de la lista
                    print("La lista esta vacía")
                else:   
                    cant_peliculas =int(input('Cuantas peliculas quieres ver: \n'))
                    orden = int(input('Quieres una lista (1) Ascendente o (2) Descendente:'))
                    criteria = int(input('Quiere por (1) Calificacion promedio o (2) Numero de votos: '))

                    counter=orderElementsByCriteria(cant_peliculas, orden, criteria, tipo_lista) #filtrar una columna por criterio  
                    if criteria == 1:
                        criteria = 'calificacion promedio'
                    else:
                        criteria = 'numero de votos'

                    if orden == 1:
                        orden = 'ascendentemente'
                    else:
                        orden = 'descendentemente'
                    
                    print("La lista de peliculas ordenada ", orden, ' por el criterio de ', criteria, 'son: ')
                    for peliculas in counter:
                        print(peliculas)
                    
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

            
                
if __name__ == "__main__":
    main()