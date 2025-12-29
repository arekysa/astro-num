# koristeci topografija.dat koji ima ekvidistantne log i lat
# zadatak - odrediti nadmorsku visinu za proizvoljnu longitudu na Marsu koristeci interpolacioni polinom

import numpy as np
import math

# kod za sredisnje razlike sa casa
def sredisnje_razlike(y):
    red = len(y)-1 # ред интерполациононог полинома (то је исто ред разлика)
    razlike = []
    for i in range(0,red):
        razlike.append(np.zeros(red-i))

    y1 = y
    for i in range(0,red):
        for j in range(0,red-i):
            razlike[i][j] =y1[j+1]-y1[j]
    y1 = razlike[i]

    sredisnje=[]
    for i in range(0,red):
        if red % 2 == 0: # непаран број чворова (паран ред полинома)
            if i % 2 !=0:
                sredisnje.append(razlike[i][int(np.ceil((len(razlike[i]))/2.))-1])
            else:
                sredisnje.append(np.mean([razlike[i][int(len(razlike[i])/2)-1],
                razlike[i][int(len(razlike[i])/2)]]))

        else: # паран број чворова (непаран ред полинома) - Бесел
            if i % 2 !=0:
                sredisnje.append(np.mean([razlike[i][int(int(len(razlike[i])/2))-1],
                razlike[i][int(int(len(razlike[i])/2))]]))
            else:
                sredisnje.append(razlike[i][int(np.ceil((len(razlike[i]))/2.))-1])

    return sredisnje

# kod za stirlingoiv polinom dat u fajlu sa git-a
def stirling(x, y, x0, red):
    # x,y - cvorovi interpolacije
    # x0 - arg za koji se vrsi interpolacija
    # red - red interpolacionog polinoma

    if np.mod(red,2)!=0:
        print('stirlingov polinom mora biti parnog reda')
        exit()

    h = x[1]-x[0]
    indeks = np.argwhere(x < x0)[-1][0]

    q = (x0 - x[indeks])/h
    if q>=0.5:
        x = x[indeks-int(red/2)+1:indeks+int(red/2)+2]
        y = y[indeks-int(red/2)+1:indeks+int(red/2)+2]
    else:
        x = x[indeks - int(red / 2):indeks + int(red / 2) + 1]
        y = y[indeks - int(red / 2):indeks + int(red / 2) + 1]
    sredisnje = sredisnje_razlike(y)

    P = y[int(np.floor(len(x)/2))]
    q = (x0-x[int(np.floor(len(x)/2))])/h
    q_parno = 1
    q_neparno = 0

    for i in range(1,int((len(x)+1)/2)):
        q_parno = q_parno * (q**2-(i-1)**2)

        if i ==1:
            q_neparno = q
        else:
            q_neparno = q_neparno*(q**2-(i-1)**2)

        P = P + q_neparno/math.factorial(2*i-1)*sredisnje[2*i-2]
        P = P + q_parno/math.factorial(2*i)*sredisnje[2*i-1]

    return P # preuredjen kod da nam samo vraca polinom a ne i cvorove



h = np.loadtxt('topografija.dat', skiprows=2) # ucitavanje podataka
longituda=np.arange(0.125, 360, step=0.25) # niz ekv dist longituda

######### ako zelimo visine za sve latitude na odredjenoj longitudi ###########

latituda=np.arange(-89.875, 90, step=0.25) # niz ekv dist latituda
log0 = 125.623 # neka fiksna longituda za koju interpoliramo da dobijemo visinu

for lat in range(len(latituda)): # prolazimo kroz sve latitude i za fiksnu longitutdu trazimo visinu
    visine = h[lat, :] # uzima visine samo za tu latitudu i sve longitude
    h0 = stirling(longituda, visine, log0, red=6) # trazim visinu
    print(f'Visina na latitudi:{latituda[lat]}, i longitudi:{log0} je: ', np.round(h0, 3))

# ako zelimo visinu za fiksiranu latitudu i fiksiranu longitudu, gde interpoliramo po longitudi
lat_indeks = 40
visine = h[lat_indeks, :]

log0 = 125.623
h0 = stirling(longituda,visine,log0,red=6)
print('Trazena visina je: ', np.round(h0,3))
