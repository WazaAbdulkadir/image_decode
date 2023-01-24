# Inverse zigzag scan of a matrix
# Arguments are: a 1-by-m*n array,
# where m & n are vertical & horizontal sizes of an output matrix.
# Function returns a two-dimensional matrix of defined sizes,
# consisting of input array items gathered by a zigzag method.
#
# Matlab Code:
# Alexey S. Sokolov a.k.a. nICKEL, Moscow, Russia
# June 2007
# alex.nickel@gmail.com

import numpy as np

def inverse_zigzag(input, vmax, hmax):
    # print input.shape

    # initializing the variables
    # ----------------------------------
    h = 0
    v = 0

    vmin = 0
    hmin = 0

    output = np.zeros((vmax, hmax))

    i = 0
    # ----------------------------------

    while ((v < vmax) and (h < hmax)):
        # print ('v:',v,', h:',h,', i:',i)
        if ((h + v) % 2) == 0:  # going up

            if (v == vmin):
                # print(1)

                output[v, h] = input[i]  # if we got to the first line

                if (h == hmax):
                    v = v + 1
                else:
                    h = h + 1

                i = i + 1

            elif ((h == hmax - 1) and (v < vmax)):  # if we got to the last column
                # print(2)
                output[v, h] = input[i]
                v = v + 1
                i = i + 1

            elif ((v > vmin) and (h < hmax - 1)):  # all other cases
                # print(3)
                output[v, h] = input[i]
                v = v - 1
                h = h + 1
                i = i + 1


        else:  # going down

            if ((v == vmax - 1) and (h <= hmax - 1)):  # if we got to the last line
                # print(4)
                output[v, h] = input[i]
                h = h + 1
                i = i + 1

            elif (h == hmin):  # if we got to the first column
                # print(5)
                output[v, h] = input[i]
                if (v == vmax - 1):
                    h = h + 1
                else:
                    v = v + 1
                i = i + 1

            elif ((v < vmax - 1) and (h > hmin)):  # all other cases
                output[v, h] = input[i]
                v = v + 1
                h = h - 1
                i = i + 1

        if ((v == vmax - 1) and (h == hmax - 1)):  # bottom right element
            # print(7)
            output[v, h] = input[i]
            break

    return output