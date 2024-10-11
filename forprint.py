from metodos import rk4

import numpy as np
import matplotlib.pyplot as plt

def sistema(x, t):
    f1, f2 = x
    dx1dt = -np.exp((-10)/(f2+273))*f1
    dx2dt = (1000*np.exp((-10)/(f2+273))*f1)-(10*(f2-20))
    return np.array([dx1dt, dx2dt])  # Corrigido para retornar um array numpy corretamente

Tini = 20  # temperatura inicial em graus Celsius
Cini = 10  # concentração inicial em gmol/L

x0 = [Cini, Tini]  # vetor de condições iniciais
t = np.linspace(0, 10, 1001)  # vetor de tempo de 0 a 10 segundos com diferentes resoluções

solucao = rk4(sistema, x0, t)

plt.plot(t, solucao[:, 1], label=f'Temperatura do reator T(t) com {t[-1]/(len(t)-1)} de passo')  # plota o gráfico da temperatura

plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (K)')
plt.legend()
plt.grid()
plt.show()
