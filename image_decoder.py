from tkinter import Image

import numpy as np
import binascii

from dc_table import dc_table_size
from dc_bin_to_decimal import bin_to_dec
from calc_ac_size_and_zero_count import  ac_size_and_zero_count_table
from izigzag import inverse_zigzag
from scipy.fftpack import ifft, idct
from matplotlib import pyplot as plt
from PIL import Image

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


"""
########## decode test for dc value ##########

first two bytes: 1000_0111, 1101_1010
# It is certain first value must be DC. So since 100 matches with a DC code I will send it to dc_table module
first_three_bit = all_bin_values[0:3]
print(first_three_bit)

# 100 turns 3. This means 3 bits in a row represents the dc value:
dc_table_size(first_three_bit)
# and it is 001 it corresponds to -6


dc_value_length = dc_table_size(first_three_bit)

# convert bin dc value to decimal dc
y = all_bin_values[3:6]
test = bin_to_dec(y)
# it turns -6 and indeed it was the first dc value.
"""


######### DECODE BITSTREAM INTO DECIMAL AC AND DC VALUES #########

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
while number_of_detected_dc_value < 1200:

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

    # There were some missing DC values, I found out when dc value is zero for loop was not handling it so I have added this if else structure
    if (dc_size == 0):
        dc_ac_array.append(0)
    else:
        convert_dc_bin_value_to_decimal = ''
        for i in range (dc_size):
            convert_dc_bin_value_to_decimal = convert_dc_bin_value_to_decimal + all_bin_values[bin_array_index]
            bin_array_index +=1
            if (i == dc_size-1):
                decimal_dc_value = bin_to_dec(convert_dc_bin_value_to_decimal)
                dc_ac_array.append(decimal_dc_value)

    #print(decimal_dc_value)

    #dc_ac_array[dc_ac_index] = decimal_dc_value
    #dc_ac_index +=1



    #### handle ac values ####
    ac_counter = 1
    while ac_counter < 64:

        ac_value_detected = 0
        ac_code_detection_array = ''
        while ac_value_detected != 1:
            ac_code_detection_array = ac_code_detection_array + all_bin_values[bin_array_index]
            bin_array_index +=1
            numberofzero_and_sizeofacvalue=ac_size_and_zero_count_table(ac_code_detection_array)

            if 0 <= numberofzero_and_sizeofacvalue[0] <= 15 and  0<= numberofzero_and_sizeofacvalue[1] <= 10 :
                ac_value_detected = 1
            else:
                print('add a bit to detect ac value')



        numberofzero = numberofzero_and_sizeofacvalue[0]
        sizeof_nonzero_ac = numberofzero_and_sizeofacvalue[1]
        ### if else structure to check if EOB and sixteen zero without EOB  ###
        if (numberofzero == 0 and sizeof_nonzero_ac == 0) : #1010 detected: EOB
            for i in range(64-ac_counter):
                dc_ac_array.append(0)
            ac_counter = 64

        elif (numberofzero == 15 and sizeof_nonzero_ac == 0) : # sixteen zero in a row but it is not EOB
            for i in range(16):
                dc_ac_array.append(0)
            ac_counter = ac_counter +16

        else:
            for i in range(numberofzero):
                dc_ac_array.append(0)
            ac_counter = ac_counter + numberofzero_and_sizeofacvalue[0] + 1 #numberofzero_and_sizeofacvalue[1]


        convert_ac_bin_value_to_decimal = ''
        for i in range(sizeof_nonzero_ac):
            convert_ac_bin_value_to_decimal = convert_ac_bin_value_to_decimal + all_bin_values[bin_array_index]
            bin_array_index +=1
            if(i == sizeof_nonzero_ac-1):
                decimal_ac_value = bin_to_dec(convert_ac_bin_value_to_decimal)
                dc_ac_array.append(decimal_ac_value)


#########  BITSTREAM DECODED INTO DECIMAL DC AND AC VALUES #########




####### Inverse DPCM ######

## check dc components
dc_components = []
for i in range (0,len(dc_ac_array),64):
    dc_components.append(dc_ac_array[i])

# dc components after inverse dpcm
for i in range(len(dc_components)-1):
    dc_components[i+1] = dc_components[i] + dc_components[i+1]

j = 0
for i in range(0,len(dc_ac_array),64):
    dc_ac_array[i] = dc_components[j]
    j = j + 1




###### Inverse Zigzag ########
square_array = np.zeros((240,320))
mid_array = np.zeros((8,8))
line_array = []
# send 1*64 array get 8*8 array
xindex = 0
yindex = 0
mid_array_ready = 0
for i in range(len(dc_ac_array)):  #len(dc_ac_array)

    if (i%64==0 and i != 0):
        mid_array= inverse_zigzag(line_array,8,8)
        line_array = []
        mid_array_ready = 1

    line_array.append(dc_ac_array[i])

    if(mid_array_ready):
    #for j in range(1,1200):
        square_array[yindex:yindex+8, xindex:xindex+8] = mid_array
        xindex +=8
        mid_array_ready = 0
        if (xindex == 320):
            xindex = 0
            yindex += 8



########## Inverse Quantization ##########

Quantization_table = [[16,11,10,16,24,40,51,61],[12,12,14,19,26,58,60,55],[14,13,16,24,40,57,69,56],[14,17,22,29,51,87,80,62],
                      [18,22,37,56,68,109,103,77],[24,35,55,64,81,104,113,92], [49,64,78,87,103,121,120,101], [72,92,95,98,112,100,103,99]]


Iqntz_array = np.zeros((240,320))

for i in range(0,240,8):
    for j in range(0,320,8):
        Iqntz_array[i:i+8,j:j+8] = np.multiply(square_array[i:i+8,j:j+8],Quantization_table)





#########  IDCT  #########

Idct_array = np.zeros((240,320))

for i in range(0,240,8):
    for j in range(0,320,8):
        Idct_array[i:i+8,j:j+8] = idct(idct( (Iqntz_array[i:i+8,j:j+8]), axis=0 , norm='ortho'), axis=1 , norm='ortho')


intIdct =Idct_array.astype(int)

image = intIdct + 128

#plt.imshow(image, cmap='gray')

img = Image.fromarray(np.uint8(image),'L')
img.save("decodedimage.TIFF")

plt.imshow(img,cmap='gray')
