"""
Користећи фајл Moon_crust.dat наћи профиле дебљина Мјесечеве коре на латитудама [-80, -40, 0, 40, 80]
Профиле плотовати на истом графику. Задатак урадити коришћењем сплајн интерполације. Даље, треба наћи максималне и
минималне дебљине код кривих свих пет профила користећи np.max и np.min. Наћи профиле разлика између одређених
парова латитуда [-80, 0] i [80, 0] 
 и (треба "одузети" назначене криве). На крају, израчунати коефицијенте корелације између свих профила користећи np.corrcoef.
"""

# uveodjenje potrebnih biblioteka
import numpy as np
import matplotlib.pyplot as plt
import Splajn_interpolacija as spl

# ucitavanje podataka
D = np.loadtxt('Moon_crust.dat')
print(D.shape) # kako je shape (6480, 10) moramo da ga reshapujemo radi lakseg rada
D = np.reshape(D, [180, 360])

# prikaz debljine meseceve koore i postavljanje vizuelno koje ltatitude uzimamo
longituda = np.linspace(0, 360, 360)
latituda = np.linspace(-90, 90, 180)
X, Y = np.meshgrid(longituda, latituda)
print(X.shape, Y.shape)

korak = 20 # korak po longitudi
fi = np.arange(-80, 120, 40) # latitude na kojima se traze profili
longituda0 = np.arange(0 + korak, 360, step = korak)
plt.contourf(X, Y, D, cmap='terrain', levels = 50) # stavljeno vise level-a da plot ispadne lepsi vizuelno
plt.xlabel(r'Longituda [$^{\circ}$]')
plt.ylabel(r'Latituda [$^{\circ}$]')
plt.title("Konture Meseceve kore")
plt.colorbar(label=r'Debljina kore [$km$]')
for i in fi:
  plt.scatter(longituda0, np.ones(len(longituda0))*i, marker='.',color='red')
plt.show()

# kod za plotovanje svih profila, min i max svakog profila
x = np.linspace(0, 360, 360)
y = np.linspace(-90, 90, 180)

profili = [] # niz gde cemo cuvati sve profile radi lakseg oduzimanja

fig, axes = plt.subplots(len(fi), 1, figsize=(12, 2*len(fi)), sharex=True)

for lat in range (len(fi)):
    d_interp = np.zeros(len(x))
    for i in range(len(x)):
        dd = D[:, i]
        d_interp[i] = spl.spline_interp(y, dd, [fi[lat]])
    
    profili.append(d_interp) # cuvanje dobijenog profila u niz
    print(f"Maksimalna i minimalna debljina kore za {fi[lat]}°, max={np.max(d_interp):.3f} i min={np.min(d_interp):.3f}")
    ax = axes[lat]
    ax.plot(x, d_interp, '-', color='blue')
    ax.set_ylabel(r'Debljina kore [$km$]')
    ax.set_title(f'Profil Meseceve kore na lat = {fi[lat]}°')

axes[-1].set_xlabel(r'Longituda [$^{\circ}$]')
plt.tight_layout()
plt.show()
"""
objasnjenje za unutrasnju for petlju iznad:
prolazim kroz sve longitude i u svakoj od longituda radim interpolaciju na fiksnoj latitudi (koja ce biti jedna od onih fi), i u d_interp dobijam debljinu kore u svakoj longitudi za tu fiksnu latitudu i spoljnom petjlom radim to za sve latitude iz fi.

ispis koda za max i  min svakog profila:
Maksimalna i minimalna debljina kore za -80°, max=87.907 i min=25.883
Maksimalna i minimalna debljina kore za -40°, max=86.734 i min=21.396
Maksimalna i minimalna debljina kore za 0°, max=107.688 i min=18.937
Maksimalna i minimalna debljina kore za 40°, max=90.415 i min=36.794
Maksimalna i minimalna debljina kore za 80°, max=72.766 i min=50.909

"""


# razlike profila (-80, 0) i (80, 0)
diff_neg80_0 = profili[0] - profili[2] # kako nam niz profila izgleda ovako [profil_-80, profil_-40, profil_0, profil_40, profil_80]
diff_80_0 = profili[4] - profili[2]
# plot razlika
plt.figure(figsize=(12,5))
plt.plot(x, diff_neg80_0, '-', color='red', label='razlika: -80° - 0°')
plt.plot(x, diff_80_0, '-', color='green', label='razllika: 80° - 0°')
plt.xlabel(r'Longituda [$^{\circ}$]')
plt.ylabel(r'Razlika debljina kore [$km$]')
plt.title('Razlike debljina profila Meseceve kore')
plt.legend()
plt.show()

# korelacije izmedju profila
print('Matrica korelacija izmedju svih profila:\n')
print(np.corrcoef(profili))

# plot matrice korelacije
fig, ax = plt.subplots(figsize=(6,5))
corr_matrix = np.corrcoef(profili)
# prikaz matrice kao heatmap
cax = ax.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)

ax.set_xticks(np.arange(len(fi)))
ax.set_yticks(np.arange(len(fi)))
ax.set_xticklabels(fi)
ax.set_yticklabels(fi)
plt.gca().invert_yaxis()
ax.set_xlabel(r'Latituda [$^{\circ}$]')
ax.set_ylabel(r'Latituda [$^{\circ}$]')
ax.set_title('Matrica korelacije izmedju profila')

fig.colorbar(cax, ax=ax, label='Korelacija')

# upisivanje vrednosti korelacije na plot
for i in range(len(fi)):
    for j in range(len(fi)):
        ax.text(j, i, f"{corr_matrix[i,j]:.2f}", ha="center", va="center", color="black")

plt.tight_layout()
plt.show()