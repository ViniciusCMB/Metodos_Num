import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
D = 1.0  # Coeficiente de difusão
ka = 1.0  # Parâmetro ka
kb = 1.0  # Parâmetro kb
L = 1.0  # Comprimento L
Lf = 1.0  # Comprimento Lf
CE = 1.0  # Concentração na fronteira x=0
N = 100  # Número de pontos de grade

# Discretização do domínio
dx = (L + Lf) / (N - 1)
x = np.linspace(0, L + Lf, N)

# Matriz de coeficientes e vetor de termos constantes
A = np.zeros((N, N))
b = np.zeros(N)

# Preenchimento da matriz A e do vetor b
for i in range(1, N-1):
    if x[i] < L:
        A[i, i-1] = D / dx**2
        A[i, i] = -2 * D / dx**2 - ka
        A[i, i+1] = D / dx**2
    else:
        A[i, i-1] = D / dx**2
        A[i, i] = -2 * D / dx**2 - kb
        A[i, i+1] = D / dx**2

# Condições de contorno
A[0, 0] = 1.0
b[0] = CE
A[-1, -2] = -1.0 / dx
A[-1, -1] = 1.0 / dx

# Resolução do sistema linear
C = np.linalg.solve(A, b)

# Plot do perfil de concentração
plt.plot(x, C, label='Perfil de Concentração')
plt.xlabel('x')
plt.ylabel('C(x)')
plt.legend()
plt.show()