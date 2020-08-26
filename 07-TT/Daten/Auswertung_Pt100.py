import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

Spektrumfile = input("Enter file name: ")

Kalibrierung = np.loadtxt("Pt100_Kalibrierung.csv", delimiter=';')
Spektrum = np.loadtxt(Spektrumfile)
S = interp1d(Kalibrierung[:,0], Kalibrierung[:,1], kind='cubic')
Spektrum_new = S(Spektrum[:,1])

np.savetxt("Kalibrierung_"+Spektrumfile, np.c_[Spektrum[:,0], Spektrum_new], "%.9f")