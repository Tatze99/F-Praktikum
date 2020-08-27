# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:37:20 2020

@author: Martin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy import optimize
 
Kalibrierung = np.loadtxt("Pt100_Kalibrierung.csv")

Kalibrierung2 = np.loadtxt("Kalibrierung_Diode.csv")
Spektrum = np.loadtxt("Halbleitermessung_Ge.txt")

Spektrum[:,1] = Spektrum[:,1]*10
Spektrum[:,3] = Spektrum[:,3]/1000

S = interp1d(Kalibrierung[:,0], Kalibrierung[:,1], kind='cubic')
S2 = interp1d(Kalibrierung2[:,0], Kalibrierung2[:,1], kind='cubic')

Spektrum[:,1] = S(Spektrum[:,1])
Spektrum[:,2] = S(Spektrum[:,2])
Spektrum[:,3] = S2(Spektrum[:,3])

plt.figure()
# plt.plot(1/Spektrum[:,1], np.log(1/Spektrum[:,4]))
# plt.plot(1/Spektrum[:,2], np.log(1/Spektrum[:,4]))
plt.plot(1/Spektrum[:,3], np.log(1/Spektrum[:,4]))

plt.figure()
plt.plot(Spektrum[:,0], Spektrum[:,1])

np.savetxt("Halbleitermessung_Zeitverlauf.txt", Spektrum, '%.9f')
