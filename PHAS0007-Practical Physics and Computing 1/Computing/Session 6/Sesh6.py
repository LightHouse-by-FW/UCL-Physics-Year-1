import numpy as np

L = np.pi
x_input = np.pi/2
j = 1  
k = 1
n_terms = 5
fsum = 0

while j <= n_terms:
    term = (4/np.pi)*(1/j)*np.sin((j*np.pi*x_input)/L)
    print(term)
    fsum = fsum + term
    print(fsum)
    j = j + 2
    k = k + 1
print(fsum)