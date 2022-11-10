import numpy as np #Importing the Numpy Library.
import matplotlib.pyplot as plt #Importing the Matplotlib Library.

#In order to use np.loadtxt in the context of this experiment we converted the
#leaning orrientation of the ellipse so that 1 = "right" and 0 = "left".

#Loading in our arrays for low and medium damping levels.
Speed_low, Orientation_low, Time10_low, AB_low ,CD_low , Speed_med, Orientation_med, Time10_med, AB_med , CD_med = np.loadtxt('NX3_aquired_low&med.csv', unpack=True, delimiter=",")
#Loading in our arrays for high damping level.
Speed_hi, Orientation_hi, Time10_hi, AB_hi, CD_hi = np.loadtxt('NX3_aquired_high.csv', unpack=True, delimiter=",")

#Calculating AB/CD for all levels of damping, no units.
ABoverCD_low = AB_low/CD_low 
ABoverCD_med = AB_med/CD_med
ABoverCD_hi = AB_hi/CD_hi

#Distance from plotting table to centre of cylinder.
wire2table = 1 #metres

#Calculating angular frequencies for damping levels in rad per sec.
omega_low = np.array(2*np.pi*(10/Time10_low))
omega_med = np.array(2*np.pi*(10/Time10_med))
omega_hi = np.array(2*np.pi*(10/Time10_hi))

#Calculating inverse sine for AB/CD for damping levels in rad.
arcsin_low = np.arcsin(ABoverCD_low)
arcsin_med = np.arcsin(ABoverCD_med)
arcsin_hi = np.arcsin(ABoverCD_hi)

#Calculating amplitudes for damping levels in rad.
amplitude_low = np.array(np.arctan(CD_low/2))
amplitude_med = np.array(np.arctan(CD_med/2))
amplitude_hi = np.array(np.arctan(CD_hi/2))

#In the following 3 while loops we are converting our values from the arcsin
#of AB/CD into the correct quadrants.

n = 0 #Initialising the counter on our while loop.

x = np.linspace(1.75, 4.5)

while n < 10:
    if Orientation_low[n] == 1:
        arcsin_low[n] = -arcsin_low[n]
    else:
        arcsin_low[n] = arcsin_low[n] - np.pi
    n = n + 1

n = 0 #Initialising the counter on our while loop.

while n < 10:
    if Orientation_med[n] == 1:
        arcsin_med[n] = -arcsin_med[n]
    else:
        arcsin_med[n] = arcsin_med[n] - np.pi
    n = n + 1

n = 0 #Initialising the counter on our while loop.

while n < 8:
    if Orientation_hi[n] == 1:
        arcsin_hi[n] = -arcsin_hi[n]
    else:
        arcsin_hi[n] = arcsin_hi[n] - np.pi
    n = n + 1
    
#Setting our new inverse sine values to the corresponding phase (Phi) values.
phi_low = np.array(arcsin_low)
phi_med = np.array(arcsin_med)
phi_hi = np.array(arcsin_hi)

###############
#UNCERTAINTIES#
###############

delta_time = 0.25/10 #seconds
delta_wire2table = 0.02 #metres
delta_AB = 0.2*10**(-3) #metres
delta_CD = 0.2*10**(-3) #metres
delta_omega_low = (20*np.pi*delta_time)/Time10_low #rad per sec
delta_omega_med = (20*np.pi*delta_time)/Time10_med #rad per sec
delta_omega_hi = (20*np.pi*delta_time)/Time10_hi #rad per sec
delta_amplitude_low = ((np.cos(amplitude_low)**2)/2)*np.sqrt(delta_CD**2 + (CD_low * delta_wire2table)**2)
delta_amplitude_med = ((np.cos(amplitude_med)**2)/2)*np.sqrt(delta_CD**2 + (CD_med * delta_wire2table)**2)
delta_amplitude_hi = ((np.cos(amplitude_hi)**2)/2)*np.sqrt(delta_CD**2 + (CD_hi * delta_wire2table)**2)
delta_phi_low = np.sqrt(((1/(CD_low * np.cos(phi_low)))*(delta_AB))**2 + (((AB_low * np.cos(phi_low))/(CD_low**2))*(delta_CD))**2)
delta_phi_med = np.sqrt(((1/(CD_med * np.cos(phi_med)))*(delta_AB))**2 + (((AB_med * np.cos(phi_med))/(CD_med**2))*(delta_CD))**2)
delta_phi_hi = np.sqrt(((1/(CD_hi * np.cos(phi_hi)))*(delta_AB))**2 + (((AB_hi * np.cos(phi_hi))/(CD_hi**2))*(delta_CD))**2)

###############
###############

#Importing a tool from scipy in order to fit a a curve to our data.
from scipy import optimize

#Defining the function of the amplitude for the torsion pendulum which is true
#for all damping levels.
def amplitude(x, const_lambda, mom_inertia, torsion_k, max_torque):
    return max_torque/np.sqrt(((x*const_lambda)**2)+(mom_inertia*(x**2 - (torsion_k/mom_inertia)))**2)

#Using scipy's curve fit function in order to find out the most appropraite values
#for our variables in the context of our amplitude function.
params_amp_low, params_amp_low_covariance = optimize.curve_fit(amplitude, omega_low, amplitude_low)
params_amp_med, params_amp_med_covariance = optimize.curve_fit(amplitude, omega_med, amplitude_med)
params_amp_hi, params_amp_hi_covariance = optimize.curve_fit(amplitude, omega_hi, amplitude_hi)

print("For low damping lambda = " + str(params_amp_low[0]) + ", moment of inertia = " + str(params_amp_low[1]) + ", torsion constant = " + str(params_amp_low[2]) + ", max torque = " + str(params_amp_low[3]))
print("For medium damping lambda = " + str(params_amp_med[0]) + ", moment of inertia = " + str(params_amp_med[1]) + ", torsion constant = " + str(params_amp_med[2]) + ", max torque = " + str(params_amp_med[3]))
print("For high damping lambda = " + str(params_amp_hi[0]) + ", moment of inertia = " + str(params_amp_hi[1]) + ", torsion constant = " + str(params_amp_hi[2]) + ", max torque = " + str(params_amp_hi[3]))

#Plotting all of our data points and curve fittings on one axis.
plt.figure(1)
plt.plot(x, amplitude(x, params_amp_low[0], params_amp_low[1], params_amp_low[2], params_amp_low[3]))
plt.plot(x, amplitude(x, params_amp_med[0], params_amp_med[1], params_amp_med[2], params_amp_med[3]))
plt.plot(x, amplitude(x, params_amp_hi[0], params_amp_hi[1], params_amp_hi[2], params_amp_hi[3]))
plt.scatter(omega_low, amplitude_low, label="Low", marker="x")
plt.scatter(omega_med, amplitude_med, label="Medium",  marker="x")
plt.scatter(omega_hi, amplitude_hi,  label="High",  marker="x")
plt.errorbar(omega_low, amplitude_low, xerr=delta_omega_low, yerr=delta_amplitude_low, fmt="none")
plt.errorbar(omega_med, amplitude_med, xerr=delta_omega_med, yerr=delta_amplitude_med, fmt="none")
plt.errorbar(omega_hi, amplitude_hi, xerr=delta_omega_hi, yerr=delta_amplitude_hi, fmt="none")
plt.grid(True) #Plots a grip in the backdrop of the data to give reference for the user.
plt.legend() #Gives a small key for the reader to easily tell what data is for which crystal.
plt.title("Amplitude VS Angular Frequency for Various Damping Levels") #Setting the title of graph.
plt.xlabel("Angular frequency (rad/sec)") #Setting the x-axis label.
plt.ylabel('Amplitude (rad)') #Setting the y-axis label.
plt.savefig('NX3 Amplitude.pdf', format='pdf'); #Saving file as a PDF and using semicolon to end.
plt.show()
plt.close();

plt.figure(2)
plt.plot(omega_low, phi_low, label="Low", marker="x")
plt.plot(omega_med, phi_med, label="Medium",  marker="x")
plt.plot(omega_hi, phi_hi,  label="High",  marker="x")
plt.errorbar(omega_low, phi_low, xerr=delta_omega_low, yerr=delta_phi_low, fmt="none")
plt.errorbar(omega_med, phi_med, xerr=delta_omega_med, yerr=delta_phi_med, fmt="none")
plt.errorbar(omega_hi, phi_hi, xerr=delta_omega_hi, yerr=delta_phi_hi, fmt="none")
plt.grid(True)
plt.legend()
plt.title("Phase Difference VS Angular Frequency for Various Damping Levels") #Setting the title of graph.
plt.xlabel("Angular frequency (rad/sec)") #Setting the x-axis label.
plt.ylabel('Phase (rad)') #Setting the y-axis label.
plt.savefig('NX3 Phase.pdf', format='pdf'); #Saving file as a PDF and using semicolon to end.
plt.show()
plt.close();
