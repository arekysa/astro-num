"""
uzorak sadrzi N_0 = 10^6 atoma sa konstantom raspada lambda = 0.01s^-1
dif jne: dN/dt = -lambda*N
analiticko resenje: N(t) = N_0 * e^(-lambda*t)
resiti ojlerovom metodom
"""

import numpy as np
import matplotlib.pyplot as plt

# dato iz zad
N_0 = [10**6]      
lambd = 0.01   
dt = 1           
t = 100

# analiticko resenje
vreme = np.arange(0, t + dt, dt) # niz zbog lakseg plota
N_analiticki = N_0 * np.exp(-lambd*np.array(vreme))

# ojlerova metoda
for i in range(1, len(vreme)):
  N_0.append(N_0[i-1] + (-lambd*N_0[i-1])*dt)
# ^ mogao je i da se napravi novi niz pa da s etu cuvaju vrednosti al ovako samo dodajemo na kraj novo izracunate vrednosti

# plot
plt.figure(figsize=(10, 6))
plt.plot(vreme, N_analiticki, label='Analiticko resenje', color='blue')
plt.plot(vreme, N_0, label='Ojlerova metoda', color='red', linestyle ='--')
plt.title('Poredjenje Ojlerove metode sa analitickim resenjem')
plt.xlabel('Vreme (s)')
plt.ylabel('Broj atoma N')
plt.legend()
plt.show()