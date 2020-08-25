import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

bool = 1
while(bool == 1):
	R = float(input("Enter Resitance: "))

	Kalibrierung = np.loadtxt("Pt100_Kalibrierung.csv")
	S = interp1d(Kalibrierung[:,0], Kalibrierung[:,1], kind='cubic')
	print(S(R),"K  ",S(R)-273.15,"°C")
	#S2 = S(R) -273.15
	#print(S2+"C")

if R==0:
	bool=0