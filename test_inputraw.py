import numpy as np
from matplotlib import pylab as plt
import pdb

filename = 'E:/projects/matconvnet/data/Body_composition/bone.raw'
A = np.fromfile(filename, dtype='int8', sep="")
A = A.reshape([512, 512,488])

pdb.set_trace()