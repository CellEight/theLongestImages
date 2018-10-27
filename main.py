import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import sys

def getBytesFromFile(filename):
    return open(filename, "rb").read()

def  byteToRow(byte):
    row = np.zeros(8)
    for i in range(8):
        if byte&(2**i) != 0:
            row[i] = 1
    return row

def fileToLongestImage(filename):
    file = getBytesFromFile(filename)
    Longestimage = list()
    for i in range(len(file)):
            Longestimage.append(byteToRow(file[i]))
    return Longestimage


image = fileToLongestImage(str(sys.argv[1]))
plt.imsave('LongestImage.png', np.array(image), cmap=cm.gray)
