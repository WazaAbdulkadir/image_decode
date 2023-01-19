
import numpy as np

#arr = np.array([1, 2, 3, 4, 5])
#print(arr) 

file = open("example.bin","rb")
byte_read = file.read()
file.close()

print(f'bytes: {len(byte_read)}') 



#print (2+3)