import numpy as np

import matplotlib.pyplot as plt

# Definindo parâmetros
Lx = 1.0  # comprimento do domínio
Nx = 50  # número de pontos no espaço
dx = Lx / (Nx - 1)  # passo no espaço
alpha = 0.01  # constante alpha
k = 0.1  # constante k
dt = 0.01  # passo no tempo
T = 1.0  # tempo total
Nt = int(T / dt)  # número de passos no tempo

# Condições de contorno
CE = 1.0  # valor de C em x = 0

# Inicializando a matriz de coeficientes e o vetor de solução
A = np.zeros((Nx, Nx))
C = np.zeros(Nx)

# Preenchendo a matriz de coeficientes A
for i in range(1, Nx-1):
    A[i, i-1] = -alpha / dx**2
    A[i, i] = 1 / dt + 2 * alpha / dx**2 + k
    A[i, i+1] = -alpha / dx**2

# Condições de contorno
A[0, 0] = 1.0
A[-1, -1] = 1.0
A[-1, -2] = -1.0

# Inicializando a solução
C[0] = CE

# Loop no tempo
for n in range(Nt):
    # Vetor de termos independentes
    b = C / dt
    b[0] = CE
    b[-1] = 0.0

    # Resolvendo o sistema linear
    C = np.linalg.solve(A, b)

# Plotando o resultado
x = np.linspace(0, Lx, Nx)
plt.plot(x, C, label=f't={T}')
plt.xlabel('x')
plt.ylabel('C')
plt.title('Perfil de C em função de x')
plt.legend()
plt.show()