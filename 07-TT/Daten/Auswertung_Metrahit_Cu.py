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
Spektrum = np.loadtxt("CV_Kupfer.txt")

Spektrum[:,1] = Spektrum[:,1]
Spektrum[:,2] = Spektrum[:,2]
Spektrum[:,3] = Spektrum[:,3]/1000
Spektrum[:,4] = Spektrum[:,4]*10

S = interp1d(Kalibrierung[:,0], Kalibrierung[:,1], kind='cubic')
S2 = interp1d(Kalibrierung2[:,0], Kalibrierung2[:,1], kind='cubic')

Spektrum[:,1] = S(Spektrum[:,1])
Spektrum[:,2] = S(Spektrum[:,2])
Spektrum[:,3] = S2(Spektrum[:,3])
Spektrum[:,4] = S(Spektrum[:,4])

plt.figure()
plt.plot(Spektrum[:,0], Spektrum[:,1], label='Pt1000 Referenz')
plt.plot(Spektrum[:,0], Spektrum[:,2], label='Pt1000 Probe')
plt.plot(Spektrum[:,0], Spektrum[:,3], label='Pt1000 Diode')
plt.plot(Spektrum[:,0], Spektrum[:,4], label='Pt100 Referenz')
plt.legend()

plt.figure()
plt.plot(Spektrum[:,0], Spektrum[:,1], label='Pt1000 Referenz')
plt.plot(Spektrum[:,0], Spektrum[:,2], label='Pt1000 Probe')
plt.plot(Spektrum[:,0], Spektrum[:,2]-Spektrum[:,1], label='$\Delta$ T')
plt.legend()

plt.figure()
plt.plot(Spektrum[:,0], np.log(Spektrum[:,1]), label='Pt1000 Referenz')
plt.plot(Spektrum[:,0], np.log(Spektrum[:,2]), label='Pt1000 Probe')
plt.plot(Spektrum[:,0], np.log(Spektrum[:,2]-Spektrum[:,1]), label='$\Delta$ T')
plt.legend()

np.savetxt("CV_Kupfer_Temperaturen.txt", Spektrum, '%.9f')
