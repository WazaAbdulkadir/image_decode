import numpy as np
import binascii

from dc_table import dc_table_size
from dc_bin_to_decimal import bin_to_dec

#arr = np.array([1, 2, 3, 4, 5])
#print(arr) 

file = open("football_bitstream2.bin","rb")
# I added .hex because without it hex values was translating into ascii
byte_read = file.read().hex()
file.close()

print(f'bytes: {len(byte_read)}') 

#bayt okuma testi
#part = byte_read[0]
#part = byte_read[0:40]
#print(part)


########## create byte array  #########
take_byte  = []
number_of_bytes = len(byte_read)

for i in range(0,number_of_bytes,2):
    take_byte.append(byte_read[i:i+2])
    #print(take_byte)


########## converts bytes to bin numbers ########
hextobin = []

for i in range (int(number_of_bytes/2)):
    #seperate bytes
    hex = take_byte[i]
    # hex = binascii.hexlify(take_byte[i])
    #covert to bin
    hextobin.append(bin(int(hex,base=16))[2:])  # since first two elements of each binary string: b'   don't include it.

    if(len(hextobin[i]) != 8 ):
        lenofbin = len(hextobin[i])
        addzero = 8-lenofbin
        hextobin[i] = addzero*'0' + hextobin[i]

    #print(hextobin)



######### create one big binary array #########
lenofbin_array = len(hextobin)
all_bin_values = ''
for i in range(lenofbin_array):
    all_bin_values = all_bin_values + hextobin[i]



# first two bytes: 1000_0111, 1101_1010
# ilk gelen deger dc ilk byte ın ilk bitinden başlayarak dc code tablosundan bir degerle eşleşene kadar
# bir sonraki bitine bakacağız.
# 100, ile eşleşiyor yani; sonraki 3 bit(001) dc değer o da -6 ya takbul eder.



#def handle_dc():

####### handle dc values ##########
first_three_bit = all_bin_values[0:3]
#print(first_three_bit)
#dc_table(first_three_bit)
dc_value_length = dc_table_size(first_three_bit)
# dc_value_length == 3


# convert bin dc value to decimal dc
y = all_bin_values[3:6]

test = bin_to_dec(y)











#def handle_ac():

#def concatenate_dc_ac():

#def izigzag():

#inverse quatiozation leter inverse dct
#def idct():