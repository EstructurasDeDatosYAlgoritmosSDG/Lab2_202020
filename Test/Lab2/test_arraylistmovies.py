import pytest
import csv
from DataStructures import arraylistiterator as it
from DataStructures import liststructure as lt

def test_carga():
    lst = []

    file = 'Data/themoviesdb/MoviesCastingRaw-small.csv'
    sep = ';'
    dialect = csv.excel()
    dialect.delimiter = sep

    assert (len(lst)==0), "La lista no empieza en cero"

    try:
        with open(file,encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile,dialect=dialect)

            for row in reader:
                lt.addLast(lst,row)
    except:
        assert False, "Se presento un error al cargar el archivo"