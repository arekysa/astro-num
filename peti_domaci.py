"""
1. Одредити тренутак у ком је привидна магнитуда астероида Рјугу 17.35 и опада. Одредити стопу опадања
магнитуде за тај тренутак. Тренутака може да буде више!
"""
# ^ magnituda opada => objekat postaje sjajniji ako se invertuje y osa znaci da trazimo rast grafika

# uvodjenje potrebnih biblioteka
import numpy as np
import matplotlib.pyplot as plt
import Splajn_interpolacija as spl

t, m  = np.loadtxt('Ryugy_light_curve.txt', delimiter=',', unpack=True) # ucitavanje podataka

mag_trazena = 17.35 # magnituda iz zadatka
trazeno_t = spl.inverse_interp(t, m, [mag_trazena]) # svi trenuci u kojima je magnituda 17.35 nevezano od toga da li opada ili raste
print(f'Svi trenuici gde je prividna magnituda = {mag_trazena}, nevezano od toga da li raste ili opada:\n',trazeno_t)


t_opada = [] # niz gde cuvamo sve trenutke gde magnituda opada (tj obejakt posatje sjajniji)

for i in range(len(trazeno_t)): # prolazimo kroz sve nadjenje trenutke
  izvod = spl.spline_der(t, m, [trazeno_t[i]], 1) # trazimo prvi izvod
  if izvod < 0: # ako je prvi izvod negativan znaci da magnituda opada
    t_opada.append(trazeno_t[i]) # zapamtimo tu vrednost
    print('Trenutak u kom magnituda opada', t_opada)
    print(f'Stopa opadanja = {np.abs(izvod[0]):.5f}')


# plot
#cisto radi pregleda grafika odradicemo inteprolaciju da imamo lepu glatku liniju umesto samo cvorova(tj dobijenih podataka)

tt = np.linspace(t[0], t[-1], 1000)
mm = spl.spline_interp(t, m, tt)

plt.figure(figsize=(10, 6))
plt.plot(t, m, '.', color='grey', label='Dobijeni podaci (cvorovi)')
plt.plot(tt, mm, color='black', label='Splajn interpolacija')
plt.plot(trazeno_t, np.ones(len(trazeno_t))*mag_trazena, 'o', color='cyan', label=f'Svi trenuci gde je m = {mag_trazena}')
plt.plot(t_opada, mag_trazena, 'o', color='red', label=f'Trenutak gde je m={mag_trazena} i opada')

plt.xlabel('Julijanski dan')
plt.ylabel('Prividna magnituda')
plt.gca().invert_yaxis()
plt.title(f'Kriva sjaja asteroida Rjugu')
plt.legend()
plt.grid()
plt.show()
