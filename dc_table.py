import numpy as np
#def dc_table():
# değerler -128 ile 127 arasında olduğu için size 7 den sonrası bizim için mümkün değil dolayısıyla dc tablonun ilk 8 elemanını alacağım:
def dc_table_size(arr):
    if arr == '00':
        size = 0
    elif arr == '010':
        size = 1
    elif arr == '011':
        size = 2
    elif arr == '100':
        size = 3
    elif arr == '101':
        size = 4
    elif arr == '110':
        size = 5
    elif arr == '1110':
        size = 6
    elif arr == '11110':
        size = 7
    else:
        print("impossible dc size code ")

    return size