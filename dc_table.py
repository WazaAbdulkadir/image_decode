import numpy as np
#def dc_table():
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
    elif arr == '111110':
        size = 8
    elif arr == '1111110':
        size = 9
    elif arr == '11111110':
        size = 10
    elif arr == '111111110':
        size = 11
    else:
        #print("send new bit or it is impossible dc size code ")
        size = 12

    return size