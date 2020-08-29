"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
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

import pytest 
import config_sorting
from DataStructures import arraylist as slt



def cmpfunction (element1, element2):
    if element1["movies_id"] == element2["movies_id"]:
        return 0
    elif element1["movies_id"] < element2["movies_id"]:
        return -1
    else:
        return 1


@pytest.fixture
def lst ():
    lst = slt.newList(cmpfunction)
    return lst


@pytest.fixture
def movies ():
    movies = []
    movies.append({'movies_id':'1', 'movies_title':'Title 1', 'author':'author 1'})
    movies.append({'movies_id':'2', 'movies_title':'Title 2', 'author':'author 2'})
    movies.append({'movies_id':'3', 'movies_title':'Title 3', 'author':'author 3'})
    movies.append({'movies_id':'4', 'movies_title':'Title 4', 'author':'author 4'})
    movies.append({'movies_id':'5', 'movies_title':'Title 5', 'author':'author 5'})
    print (movies[0])
    return movies


@pytest.fixture
def lstmovies(movies):
    lst = slt.newList(cmpfunction)
    for i in range(0,5):    
        slt.addLast(lst,movies[i])    
    return lst



def test_empty (lst):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0



def test_addFirst (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addFirst (lst, movies[1])
    assert slt.size(lst) == 1
    slt.addFirst (lst, movies[2])
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == movies[2]




def test_addLast (lst, movies):
    assert slt.isEmpty(lst) == True
    assert slt.size(lst) == 0
    slt.addLast (lst, movies[1])
    assert slt.size(lst) == 1
    slt.addLast (lst, movies[2])
    assert slt.size(lst) == 2
    movie = slt.firstElement(lst)
    assert movie == movies[1]
    movie = slt.lastElement(lst)
    assert movie == movies[2]




def test_getElement(lstmovies, movies):
    movie = slt.getElement(lstmovies, 1)
    assert movie == movies[0]
    movie = slt.getElement(lstmovies, 5)
    assert movie == movies[4]





def test_removeFirst (lstmovies, movies):
    assert slt.size(lstmovies) == 5
    slt.removeFirst(lstmovies)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, 1)
    assert movie  == movies[1]



def test_removeLast (lstmovies, movies):
    assert slt.size(lstmovies) == 5
    slt.removeLast(lstmovies)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, 4)
    assert movie  == movies[3]



def test_insertElement (lst, movies):
    assert slt.isEmpty(lst) is True
    assert slt.size(lst) == 0
    slt.insertElement (lst, movies[0], 1)
    assert slt.size(lst) == 1
    slt.insertElement (lst, movies[1], 2)
    assert slt.size(lst) == 2
    slt.insertElement (lst, movies[2], 1)
    assert slt.size(lst) == 3
    movie = slt.getElement(lst, 1)
    assert movie == movies[2]
    movie = slt.getElement(lst, 2)
    assert movie == movies[0]



def test_isPresent (lstmovies, movies):
    movie = {'movies_id':'10', 'movies_title':'Title 10', 'author':'author 10'}
    print(slt.isPresent (lstmovies, movies[2]))
    assert slt.isPresent (lstmovies, movies[2]) > 0
    assert slt.isPresent (lstmovies, movie) == 0
    


def test_deleteElement (lstmovies, movies):
    pos = slt.isPresent (lstmovies, movies[2])
    assert pos > 0
    movie = slt.getElement(lstmovies, pos)
    assert movie == movies[2]
    slt.deleteElement (lstmovies, pos)
    assert slt.size(lstmovies) == 4
    movie = slt.getElement(lstmovies, pos)
    assert movie == movies[3]


def test_changeInfo (lstmovies):
    movie10 = {'movies_id':'10', 'movies_title':'Title 10', 'author':'author 10'}
    slt.changeInfo (lstmovies, 1, movie10)
    movie = slt.getElement(lstmovies, 1)
    assert movie10 == movie


def test_exchange (lstmovies, movies):
    movie1 = slt.getElement(lstmovies, 1)
    movie5 = slt.getElement(lstmovies, 5)
    slt.exchange (lstmovies, 1, 5)
    assert slt.getElement(lstmovies, 1) == movie5
    assert slt.getElement(lstmovies, 5) == movie1