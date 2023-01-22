
def ac_size_and_zero_count_table(arr):

    if (arr == '1010' or arr == '00' or arr == '01' or arr =='100' or arr =='1011' or arr == '11010' or arr == '1111000'
        or arr == '11111000' or arr == '1111110110' or arr == '1111111110000010' or arr == '1111111110000011'):
        zero_count = 0
        if (arr == '1010'):
            ac_size = 0
        elif (arr == '00'):
            ac_size = 1
        elif (arr== '01'):
            ac_size = 2
        elif (arr =='100'):
            ac_size = 3
        elif (arr =='1011'):
            ac_size = 4
        elif (arr =='11010'):
            ac_size = 5
        elif (arr =='1111000'):
            ac_size = 6
        elif (arr =='11111000'):
            ac_size = 7
        elif (arr =='1111110110'):
            ac_size = 8
        elif (arr =='1111111110000010'):
            ac_size = 9
        elif (arr == '1111111110000011'):
            ac_size = 10

    elif(arr == '1100' or arr == '11011' or arr== '1111001' or arr == '111110110' or arr == '11111110110' or arr=='1111111110000100'
    or arr=='1111111110000101' or arr =='1111111110000110' or arr=='1111111110000111' or arr=='1111111110001000'):
        zero_count = 1
        if (arr == '1100'):
            ac_size = 1
        elif (arr == '11011'):
            ac_size = 2
        elif (arr == '1111001'):
            ac_size = 3
        elif (arr == '111110110'):
            ac_size = 4
        elif (arr == '11111110110'):
            ac_size = 5
        elif (arr == '1111111110000100'):
            ac_size = 6
        elif (arr == '1111111110000101'):
            ac_size = 7
        elif (arr == '1111111110000110'):
            ac_size = 8
        elif (arr == '1111111110000111'):
            ac_size = 9
        elif (arr == '1111111110001000'):
            ac_size = 10


    elif (arr == '11100' or arr == '11111001' or arr == '1111110111' or arr == '11111110100' or arr == '1111111110001001'
          or arr == '1111111110001010' or arr == '1111111110001011' or arr == '1111111110001100' or arr == '1111111110001101'
          or arr == '1111111110001110'):

        zero_count = 2
        if (arr == '11100'):
            ac_size = 1
        elif (arr == '11111001'):
            ac_size = 2
        elif( arr == '1111110111'):
            ac_size = 3
        elif( arr== '11111110100'):
            ac_size = 4
        elif(arr == '1111111110001001'):
            ac_size = 5
        elif (arr == '1111111110001010'):
            ac_size = 6
        elif (arr == '1111111110001011'):
            ac_size= 7
        elif (arr == '1111111110001100'):
            ac_size =8
        elif (arr == '1111111110001101'):
            ac_size = 9
        elif (arr == '1111111110001110'):
            ac_size = 10

    elif (arr == '111010' or arr =='111110111' or arr == '111111110101' or arr == '1111111110001111' or arr == '1111111110010000'
    or arr == '1111111110010001' or arr == '1111111110010010' or arr == '1111111110010011' or arr == '1111111110010100' or arr == '1111111110010101' ):
        zero_count = 3
        if (arr == '111010'):
            ac_size = 1
        elif(arr =='111110111'):
            ac_size =2
        elif (arr == '111111110101'):
            ac_size = 3
        elif (arr == '1111111110001111'):
            ac_size = 4
        elif (arr == '1111111110010000'):
            ac_size = 5
        elif (arr == '1111111110010001'):
            ac_size = 6
        elif (arr == '1111111110010010'):
            ac_size = 7
        elif (arr == '1111111110010011'):
            ac_size = 8
        elif (arr == '1111111110010100'):
            ac_size = 9
        elif (arr == '1111111110010101'):
            ac_size = 10



    elif (arr == '111011' or arr == '1111111000' or arr == '1111111110010110' or arr == '1111111110010111' or arr == '1111111110011000'
    or arr == '1111111110011001' or arr == '1111111110011010' or arr == '1111111110011011' or arr == '1111111110011100' or arr == '1111111110011101'):
        zero_count = 4
        if(arr == '111011'):
            ac_size = 1
        elif (arr == '1111111000'):
            ac_size = 2
        elif (arr == '1111111110010110'):
            ac_size = 3
        elif (arr == '1111111110010111'):
            ac_size = 4
        elif (arr == '1111111110011000'):
            ac_size = 5
        elif (arr == '1111111110011001'):
            ac_size = 6
        elif (arr == '1111111110011010'):
            ac_size = 7
        elif (arr == '1111111110011011'):
            ac_size = 8
        elif (arr == '1111111110011100'):
            ac_size = 9
        elif (arr == '1111111110011101'):
            ac_size = 10


    elif(arr =='1111010' or arr =='11111110111' or arr == '1111111110011110' or arr == '1111111110011111' or arr == '1111111110100000'
    or arr == '1111111110100001' or arr == '1111111110100010' or arr == '1111111110100011' or arr == '1111111110100100' or arr == '1111111110100101'):
        zero_count = 5
        if (arr == '1111010'):
            ac_size = 1
        elif (arr == '11111110111'):
            ac_size = 2
        elif(arr == '1111111110011110'):
            ac_size =3
        elif (arr == '1111111110011111'):
            ac_size = 4
        elif (arr == '1111111110100000'):
            ac_size = 5
        elif (arr == '1111111110100001'):
            ac_size = 6
        elif (arr == '1111111110100010'):
            ac_size = 7
        elif (arr == '1111111110100011'):
            ac_size = 8
        elif (arr == '1111111110100100'):
            ac_size = 9
        elif (arr == '1111111110100101'):
            ac_size = 10

    elif(arr=='1111011' or arr == '111111110110' or arr == '1111111110100110' or arr == '1111111110100111' or arr == '1111111110101000'
    or arr == '1111111110101001' or arr == '1111111110101010' or arr == '1111111110101011' or arr == '1111111110101100' or arr == '1111111110101101'):
        zero_count =10
        if (arr=='1111011'):
            ac_size = 1
        elif arr == '111111110110':
            ac_size =2
        elif arr == '1111111110100110':
            ac_size =3
        elif arr == '1111111110100111':
            ac_size = 4
        elif arr == '1111111110101000':
            ac_size = 5
        elif arr == '1111111110101001':
            ac_size = 6
        elif arr == '1111111110101010':
            ac_size = 7
        elif arr == '1111111110101011':
            ac_size = 8
        elif arr == '1111111110101100':
            ac_size = 9
        elif arr == '1111111110101101':
            ac_size = 10

    elif(arr == '11111010' or arr == '111111110111' or arr == '1111111110101110' or arr == '1111111110101111' or arr == '1111111110111000'
    or arr == '1111111110111001' or arr == '1111111110111010' or arr == '1111111110111011' or arr == '1111111110111100' or arr == '1111111110111101'):
        zero_count = 7
        if arr == '11111010':
            ac_size = 1
        elif arr == '111111110111':
            ac_size =2
        elif arr == '1111111110101110':
            ac_size =3
        elif arr == '1111111110101111':
            ac_size =4
        elif arr == '1111111110111000':
            ac_size = 5
        elif arr == '1111111110110001':
            ac_size = 6
        elif arr == '1111111110110010':
            ac_size = 7
        elif arr == '1111111110110011':
            ac_size = 8
        elif arr == '1111111110110100':
            ac_size = 9
        elif arr == '1111111110110101':
            ac_size = 10


    elif(arr == '111111000' or arr == '111111111000000' or arr == '1111111110110110'  or arr == '1111111110110111'  or arr == '1111111110111000'
    or arr == '1111111110111001' or arr == '1111111110111010' or arr == '1111111110111011' or arr == '1111111110111100' or arr == '1111111110111101'):
        zero_count = 8
        if arr == '111111000':
            ac_size = 1
        elif arr == '111111111000000':
            ac_size = 2
        elif arr == '1111111110110110':
            ac_size = 3
        elif arr == '1111111110110111':
            ac_size = 4
        elif arr == '1111111110111000':
            ac_size = 5
        elif arr == '1111111110111001':
            ac_size = 6
        elif arr == '1111111110111010':
            ac_size = 7
        elif arr == '1111111110111011':
            ac_size = 8
        elif arr == '1111111110111100':
            ac_size = 9
        elif arr == '1111111110111101':
            ac_size = 10


    elif (arr == '111111001' or arr == '1111111110111110' or arr == '1111111110111111' or arr == '1111111111000000' or arr == '1111111111000001'
            or arr == '1111111111000010' or arr == '1111111111000011' or arr == '1111111111000100' or arr == '1111111111000101' or arr == '1111111111000110'):
        zero_count = 9
        if arr == '111111001':
            ac_size = 1
        elif arr == '1111111110111110':
            ac_size = 2
        elif arr == '1111111110111111':
            ac_size = 3
        elif arr == '1111111111000000':
            ac_size = 4
        elif arr == '1111111111000001':
            ac_size = 5
        elif arr == '1111111111000010':
            ac_size = 6
        elif arr == '1111111111000011':
            ac_size = 7
        elif arr == '1111111111000100':
            ac_size = 8
        elif arr == '1111111111000101':
            ac_size = 9
        elif arr == '1111111111000110':
            ac_size = 10


    elif (arr == '111111010' or arr == '1111111111000111' or arr == '1111111111001000' or arr == '1111111111001001' or arr == '1111111111001010'
            or arr == '1111111111001011' or arr == '1111111111001100' or arr == '1111111111001101' or arr == '1111111111001110' or arr == '1111111111001111'):
        zero_count = 10
        if arr == '111111010':
            ac_size = 1
        elif arr == '1111111111000111':
            ac_size = 2
        elif arr == '1111111111001000':
            ac_size = 3
        elif arr == '1111111111001001':
            ac_size = 4
        elif arr == '1111111111001010':
            ac_size = 5
        elif arr == '1111111111001011':
            ac_size = 6
        elif arr == '1111111111001100':
            ac_size = 7
        elif arr == '1111111111001101':
            ac_size = 8
        elif arr == '1111111111001110':
            ac_size = 9
        elif arr == '1111111111001111':
            ac_size = 10


    elif (arr == '1111111001' or arr == '1111111111010000' or arr == '1111111111010001' or arr == '1111111111010010' or arr == '1111111111010011'
          or arr == '1111111111010100' or arr == '1111111111010101' or arr == '1111111111010110' or arr == '1111111111010111' or arr == '1111111111011000'):

        zero_count = 11
        if arr == '1111111001':
            ac_size = 1
        elif arr == '1111111111010000':
            ac_size = 2
        elif arr == '1111111111010001':
            ac_size = 3
        elif arr == '1111111111010010':
            ac_size = 4
        elif arr == '1111111111010011':
            ac_size = 5
        elif arr == '1111111111010100':
            ac_size = 6
        elif arr == '1111111111010101':
            ac_size = 7
        elif arr == '1111111111010110':
            ac_size = 8
        elif arr == '1111111111010111':
            ac_size = 9
        elif arr == '1111111111011000':
            ac_size = 10


    elif (arr == '1111111010' or arr == '1111111111011001' or arr == '1111111111011010' or arr == '1111111111011011' or arr == '1111111111011100'
          or arr == '1111111111011101' or arr == '1111111111011110' or arr == '1111111111011111' or arr == '1111111111100000' or arr == '1111111111100001'):

        zero_count = 12
        if arr == '1111111010':
            ac_size = 1
        elif arr == '1111111111011001':
            ac_size = 2
        elif arr == '1111111111011010':
            ac_size = 3
        elif arr == '1111111111011011':
            ac_size = 4
        elif arr == '1111111111011100':
            ac_size = 5
        elif arr == '1111111111011101':
            ac_size = 6
        elif arr == '1111111111011110':
            ac_size = 7
        elif arr == '1111111111011111':
            ac_size = 8
        elif arr == '1111111111100000':
            ac_size = 9
        elif arr == '1111111111100001':
            ac_size = 10


    elif (arr == '11111111000' or arr == '1111111111100010' or arr == '1111111111100011' or arr == '1111111111100100' or arr == '1111111111100101'
          or arr == '1111111111100110' or arr == '1111111111100111' or arr == '1111111111101000' or arr == '1111111111101001' or arr == '1111111111101010'):

        zero_count = 13
        if arr == '11111111000':
            ac_size = 1
        elif arr == '1111111111100010':
            ac_size = 2
        elif arr == '1111111111100011':
            ac_size = 3
        elif arr == '1111111111100100':
            ac_size = 4
        elif arr == '1111111111100101':
            ac_size = 5
        elif arr == '1111111111100110':
            ac_size = 6
        elif arr == '1111111111100111':
            ac_size = 7
        elif arr == '1111111111101000':
            ac_size = 8
        elif arr == '1111111111101001':
            ac_size = 9
        elif arr == '1111111111101010':
            ac_size = 10


    elif (arr == '1111111111101011' or arr == '1111111111101100' or arr == '1111111111101101' or arr == '1111111111101110' or arr == '1111111111101111'
          or arr == '1111111111110000' or arr == '1111111111110001' or arr == '1111111111110010' or arr == '1111111111110011' or arr == '1111111111110100'):

        zero_count = 14
        if arr == '1111111111101011':
            ac_size = 1
        elif arr == '1111111111101100':
            ac_size = 2
        elif arr == '1111111111101101':
            ac_size = 3
        elif arr == '1111111111101110':
            ac_size = 4
        elif arr == '1111111111101111':
            ac_size = 5
        elif arr == '1111111111110000':
            ac_size = 6
        elif arr == '1111111111110001':
            ac_size = 7
        elif arr == '1111111111110010':
            ac_size = 8
        elif arr == '1111111111110011':
            ac_size = 9
        elif arr == '1111111111110100':
            ac_size = 10


    elif (arr == '11111111001' or arr == '1111111111110101' or arr == '1111111111110110' or arr == '1111111111110111' or arr == '1111111111111000' or arr == '1111111111111001'
          or arr == '1111111111111010' or arr == '1111111111111011' or arr == '1111111111111100' or arr == '1111111111111101' or arr == '1111111111111110'):

        zero_count = 15
        if arr == '11111111001': # if sixteen consecutive zero
            ac_size = 0
        elif arr == '1111111111110101':
            ac_size = 2
        elif arr == '1111111111110110':
            ac_size = 3
        elif arr == '1111111111110111':
            ac_size = 4
        elif arr == '1111111111111000':
            ac_size = 5
        elif arr == '1111111111111001':
            ac_size = 6
        elif arr == '1111111111111010':
            ac_size = 7
        elif arr == '1111111111111011':
            ac_size = 8
        elif arr == '1111111111111100':
            ac_size = 9
        elif arr == '1111111111111101':
            ac_size = 10

    return (zero_count, ac_size)