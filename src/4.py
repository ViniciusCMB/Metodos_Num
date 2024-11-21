import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
Lx = 1.0  # comprimento do domínio
T = 1.0   # tempo total de simulação
alpha = 0.01
u = 1.0
CE = 1.0

# Parâmetros de discretização
Nx = 50  # número de pontos no espaço
Nt = 1000  # número de pontos no tempo
dx = Lx / (Nx - 1)
dt = T / Nt

# Verificar a restrição do passo de tempo
if dt > 1 / (2 * alpha * (dx**2) + u * dx):
    raise ValueError(
        "O passo de tempo não satisfaz a condição de estabilidade.")

# Inicializar a matriz de concentração
C = np.zeros((Nt, Nx))

# Condição inicial
C[0, :] = 0.0

# Condição de contorno
C[:, 0] = CE

# Loop de tempo
for n in range(0, Nt-1):
    for i in range(1, Nx-1):
        C[n+1, i] = (C[n, i] + dt * (-u * (C[n, i] - C[n, i-1]) / dx +
                                     alpha * (C[n, i+1] - 2 * C[n, i] + C[n, i-1]) / dx**2))
    # Condição de contorno Neumann no final do domínio
    C[n+1, -1] = C[n+1, -2]

# Plotar o resultado
x = np.linspace(0, Lx, Nx)
plt.plot(x, C[-1, :], label=f't={T}')
plt.xlabel('x')
plt.ylabel('C')
plt.title('Perfil de concentração C(x) ao longo do tempo')
plt.legend()
plt.show()
