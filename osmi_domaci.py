"""
jne kretanja zvezde:
x'' = -x-2xy
y'' = -y-x^2+y^2

pocetni uslovi:
(x0, y0) = (0,0)
(vx0, vy0) = (0.3, 0.4)
dt = 0.01
t_max = 1000

implementirati lepfrog integrator sa funkcijama ubrzanja:
ax = -x-2xy
ay = -y-x^2+y^2

plotovati trajektoriju u x,y ravni
plotovati (x, vx) i (y, vy)
"""

import numpy as np
import matplotlib.pyplot as plt

# pocetnin uslovi
dt = 0.01
t = 1000
x = [0]
y = [0]
vx = [0.3]
vy = [0.4]

iter = int(t/dt) # broj iteracija za for


def ubrzanje(x, y):
  ax = -x - 2*x*y
  ay = -y - x**2 + y**2
  return ax, ay

# leapforg algo, samo primena formule sa casa gde naizmenicno azuriramo ubrzanje i brzinu
for i in range(iter):
  ax, ay = ubrzanje(x[i], y[i])

  vx_pola = vx[i] + 0.5 * ax * dt
  vy_pola = vy[i] + 0.5 * ay * dt

  x.append(x[i] + vx_pola * dt)
  y.append(y[i] + vy_pola * dt)

  ax_novo, ay_novo = ubrzanje(x[i+1], y[i+1])

  vx.append(vx_pola + 0.5*(ax_novo)*dt)
  vy.append(vy_pola + 0.5*(ay_novo)*dt)

# plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Trajektorija zvezde', color='blue')
plt.title('Trajektorija zvezde u x, y ravni')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.axis('equal')
plt.show()

# plot faznih portreta
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x, vx, label='vx', color='red')
plt.title('Graf (x, vx)')
plt.xlabel('x')
plt.ylabel('vx')

plt.subplot(1, 2, 2)
plt.plot(y, vy, label='vy', color='green')
plt.title('Graf (y, vy)')
plt.xlabel('y')
plt.ylabel('vy')

plt.tight_layout()

plt.show()

