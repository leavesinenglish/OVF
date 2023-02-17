from animate_solution import *
from diff_equation_solver import Solver


def f(x, y, t):
    return (1 - x ** 2 / L ** 2) * (1 - y ** 2 / L ** 2) + (y / L + 1) * (1 - y ** 2 / L ** 2) * np.sin(2 * np.pi * t)


L = 1
dt = 0.01
T = 2
N_x = 100
N_y = 100
a = -L
b = L
u_x = [Solver(a, b, N_x, dt) for _ in range(N_y)]
u_y = [Solver(a, b, N_y, dt/2) for _ in range(N_x)]
X, Y = np.meshgrid(u_x[0].x, u_y[0].x)
layer = []
solution = np.ones(shape=X.shape)
t = np.arange(0, T, dt)
current_iteration = 0
for it in t:
    print(f'{current_iteration} / {t.size}')
    layer.append(np.copy(solution))
    intensity = np.vectorize(f, otypes=[float])(X, Y, it)
    for j, s in enumerate(u_x):
        solution[j + 1, :] = s.crank_nicolson_iter_step(solution[j + 1, :], intensity[j + 1, :])
    for j, s in enumerate(u_y):
        solution[:, j + 1] = s.crank_nicolson_iter_step(solution[:, j + 1], intensity[:, j + 1])
    current_iteration += 1

animation_3D(X, Y, layer, interval=0.01)