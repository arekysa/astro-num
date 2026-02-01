"""
proceniti br zvezda koje se nalaze u naseljivoj zoni neke galaksije koja ima priblizno 10^11 zvezda. Zvezde su uniformno rasporedjene unutar galaksije radijusa (poluprecnik) 16kpc i debljina 1.2kpc
Naseljiva zona je oblika torusa sa unutrasnjim pp od 2.8kpc i spoljasnjim pp od 8.8kpc. Naseljive zvezde su one dugovecne i stabilne sto cini 7% ukupnog br zvezda u nastanjivopj zoni
"""
import numpy as np
import matplotlib.pyplot as plt
import random

# dati parametri u zadatku
R_gal = 16. 
h_gal = h_nastanjiva = 1.2 # stavljeno iste visine jer u zad nije receno drugacije
zvezde_ukupno = 1e11
udeo_stabilnih = 0.07  

r_unutar = 2.8
r_van = 8.8

N = 100000 # br tacaka za hit or miss

#r_gal = np.random.uniform(0, R_gal, N)  da je samo uniformnu rapsodelu po radijusu ali ne i povrsini
u = np.random.uniform(0, 1, N)
r_gal = R_gal * np.sqrt(u) # da bi gustina bila proporcionalna povrsini
theta = np.random.uniform(0, 2*np.pi, N) # da mogu tacke da se stvore u celom prstenu
z = np.random.uniform(-h_gal/2, h_gal/2, N) # postavljen centar na nula

# provera koje su tacke u zoni
hit = (r_gal >= r_unutar) & (r_gal <= r_van) 
hits = np.sum(hit)

# procena br zvezda
udeo_zapremine = hits / N # sto je vece N ova aproksimacija je veoma dobra analitickoj jer greska kod monte karlo metode opada po formuli: greska = 1/sqrt(n)
zvezde_u_zoni = zvezde_ukupno * udeo_zapremine
zvezde_naseljive = zvezde_u_zoni * udeo_stabilnih

print(f'Broj tacaka za metodu: {N}')
print(f'Broj pogodaka: {hits}')
print(f'Udeo zapremina naseljive zone: {udeo_zapremine*100:.3f} %')
print(f'Broj zvezda u naseljivoj zoni: {zvezde_u_zoni:.3e}')
print(f'Broj naseljivih zvezda: {zvezde_naseljive:.3e}')

"""
jedan od ispisa:

Broj tacaka za metodu: 100000
Broj pogodaka: 27104
Udeo zapremina naseljive zone: 27.104 %
Broj zvezda u naseljivoj zoni: 2.710e+10
Broj naseljivih zvezda: 1.897e+09

"""

# 2d plot u x, y ravni radi vizuelizacije
x = r_gal * np.cos(theta)
y = r_gal * np.sin(theta)

fig, ax = plt.subplots(figsize=(7, 7))

plt.scatter(x[hit], y[hit], s=1, alpha=0.5, color='lightgreen', label='Pogoci')
plt.scatter(x[~hit], y[~hit], s=1, alpha=0.5, color='lightcoral', label='Promasaji')

spolja = plt.Circle((0,0), r_van, fill=False, color='navy', linewidth=2, label='Naseljiva zona')
unutra = plt.Circle((0,0), r_unutar, fill=False, linewidth=2, color='navy')
galaksija = plt.Circle((0,0), R_gal, fill=False, linewidth=2, color='purple', label='Galaksija')
ax.add_patch(spolja)
ax.add_patch(unutra)
ax.add_patch(galaksija)

plt.legend(markerscale=5)
plt.xlabel('X - osa [$kpc$]')
plt.ylabel('Y - osa [$kpc$]')
plt.title('Pticija perspektiva hit or miss metode na galaksiji i njenoj naseljivoj zoni')
plt.show()