def bin_to_dec(bin):

    if(bin[0] == '0'):
        sizeofbin = len(bin)
        # str format does not support to item assignment
        # so I created new empty str object
        newbin = ''
        for i in range(sizeofbin):
            if (bin[i] == '0'):
                newbin = newbin + '1'
            else:
                newbin = newbin + '0'
        decimal_value = -int(newbin,2)
    elif(bin[0] == '1'):
        decimal_value = int(bin,2)


    return decimal_value