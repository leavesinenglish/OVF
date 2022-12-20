import numpy as np
from scipy.linalg import solve_banded


class Solver:
    def __init__(self, x0, x1, space_steps, dt):
        self.dx = (x1 - x0) / (space_steps + 1)
        self.dt = dt
        self.N = space_steps
        self.x = np.linspace(x0, x1, space_steps + 2)
        k_a = np.array([- self.dt / (2 * self.dx ** 2) for _ in self.x[1:-1]])
        k_b = np.array([1 + self.dt / self.dx ** 2 for _ in self.x[1:-1]])
        k_c = k_a
        c_diag = np.concatenate([[0], [0], k_a])
        b_diag = np.concatenate([[1], k_b, [1]])
        a_diag = np.concatenate([k_c, [0], [0]])
        self.matrix = np.row_stack([c_diag, b_diag, a_diag])

    def crank_nicolson_iter_step(self, U, f):
        k_d = np.array([self.dt / (2 * self.dx ** 2) for _ in self.x[1:-1]])
        right_part = np.concatenate([[0], U[1:-1] + k_d * (U[:-2] - 2 * U[1:-1] + U[2:]) + f[1:-1] , [0]])
        return solve_banded((1, 1), self.matrix, right_part)