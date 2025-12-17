# 1.Користећи фајл 'Spektar Sunca.txt' наћи таласне дужине
# на којима је интензитет зрачења максималан и минималан.
import numpy as np

l, I = np.loadtxt('Spektar Sunca.txt', delimiter=',', skiprows=2, unpack=True)

# prvi nacin - preko fora
min_I = np.min(I)
max_I = np.max(I)

# for petlja da nadjemo odgovarajuci index min i max
for i in range(len(l)):
    if I[i] == min_I:
        min_l = l[i]
    elif I[i] == max_I:
        max_l = l[i]

print('\n')
print("Talasna duzina max intenziteta: ", max_l)
print("Talasna duzina min intenziteta: ", min_l)
print('#############################################')

# drugi nacin - preko ugradjenih fja u numpy (brze)
idx_min = np.argmin(I)
idx_max = np.argmax(I)
min_l = l[idx_min]
max_l = l[idx_max]

print("Talasna dužina max intenziteta:", max_l)
print("Talasna dužina min intenziteta:", min_l)
print('\n')

# 2. Модификовати код тако да рачуна вриједности
# ексцентричне аномалије за низ вриједности средње аномалије [0-2pi] за
# више вриједности ексцентрицитета (нпр. e=0.05, 0.2, 0.5).
""" Dobijen kod koji treba da se modifikuje
e = 0.05
M = 2.56
tacnost = 1e-8
delta = 2 * tacnost
E = M
br = 0
while np.abs(delta) > tacnost:
    br += 1
    f = E - e * np.sin(E) - M
    fprim = 1 - e * np.cos(E)
    delta = f / fprim
    E = E - delta
print(E)
print(br)"""

# modifikovano kod spakovano u funkciju da bude preglednije
def kepler(M, e, tacnost = 1e-8):
    M = M.reshape(1, -1) # pravimo od jednog niza kolonu a od drugog red radi lakse vektorizacije
    e = e.reshape(-1, 1)

    E = M.copy()
    delta = np.ones_like(E) * 2 * tacnost
    br = 0

    while np.all(np.abs(delta)) > tacnost:
        br += 1
        f = E - e * np.sin(E) - M
        fprim = 1 - e * np.cos(E)
        delta = f / fprim
        E = E - delta

    return E, br


M = np.linspace(0, 2*np.pi, 100) # niz od 100elem
e = np.array([0.05, 0.2, 0.5]) # niz ekscentriciteta

E, br = kepler(M, e)
print(E)
print(E.shape)
print(br)
