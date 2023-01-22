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

#print(f'bytes: {len(byte_read)}')


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
    hextobin.append(bin(int(hex,base=16))[2:])  # since first two elements of each binary string: 0b don't include it.

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


########## trying to decode dc value ##########

# first two bytes: 1000_0111, 1101_1010
# It is certain first value must be DC. So since 100 matches with a DC code I will send it to dc_table module
#first_three_bit = all_bin_values[0:3]
#print(first_three_bit)

# 100 turns 3. This means 3 bits in a row represents the dc value:
#dc_table_size(first_three_bit)
# and it is 001 it corresponds to -6


#dc_value_length = dc_table_size(first_three_bit)

# convert bin dc value to decimal dc
#y = all_bin_values[3:6]
#test = bin_to_dec(y)
# it turns -6 and indeed it was the first dc value.



######### DECODE PROCESS #########

#dc_value_counter = 0
#while dc_value_counter < 1200:
#    handle_dc()
#    dc_value_counter += 1
#    handle_ac()



number_of_detected_dc_value = 0
bin_array_index = 0
dc_ac_array = []
dc_ac_index = 0
#decimal_dc_value = 0
while number_of_detected_dc_value < 1:


    #### handle dc values #####
    dc_value_detected =0
    dc_code_detection_array = ''
    while dc_value_detected != 1:
        dc_code_detection_array = dc_code_detection_array + all_bin_values[bin_array_index]
        bin_array_index +=1
        dc_size = dc_table_size(dc_code_detection_array)

        if (0 <= dc_size <= 11):
            dc_value_detected = 1
            number_of_detected_dc_value +=1
        else:
            print("add a bit to detect dc size")

    convert_dc_bin_value_to_decimal = ''
    for i in range (dc_size):
        convert_dc_bin_value_to_decimal = convert_dc_bin_value_to_decimal + all_bin_values[bin_array_index]
        bin_array_index +=1
        if (i == dc_size-1):
            decimal_dc_value = bin_to_dec(convert_dc_bin_value_to_decimal)

    #print(decimal_dc_value)

    #dc_ac_array[dc_ac_index] = decimal_dc_value
    #dc_ac_index +=1

    dc_ac_array.append(decimal_dc_value)


    #### handle ac values ####

    ac_counter = 1
    zero_count = 0

    # while ac_counter < 64:



#handle_dc()

#def handle_ac():



####### handle dc values ##########










#def handle_ac():

#def concatenate_dc_ac():

#def izigzag():

#inverse quatiozation leter inverse dct
#def idct():