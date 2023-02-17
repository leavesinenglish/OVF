import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

matplotlib.use("TkAgg")

L = 1
x = np.linspace(-L, L, int(L / 0.03))
y = np.linspace(-L, L, int(L / 0.03))
t = np.linspace(0, 2, int(2 / 0.01))

u = np.zeros((x.size, y.size, t.size))

dT = t[1] - t[0]
dX = x[1] - x[0]
dY = y[1] - y[0]

X = dT / (2 * dX ** 2)
Y = dT / (4 * dY ** 2)

aX = -X
bX = 1 + 2 * X
cX = -X

aY = -Y
bY = 1 + 2 * Y
cY = -Y


def f(x_, y_, t_):
    return (1 - x_ ** 2 / L ** 2) * (1 - y_ ** 2 / L ** 2) + (y_ / L + 1) * (1 - y_ ** 2 / L ** 2) * np.sin(
        2 * np.pi * t_)


def diX(ix, iy, it):
    return Y * u[ix][iy + 1][it] + (1 - 2 * Y) * u[ix][iy][it] + Y * u[ix][iy - 1][it] + f(x[ix], y[iy], t[it])


def diY(ix, iy, it):
    return X * u[ix + 1][iy][it] + (1 - 2 * X) * u[ix][iy][it] + X * u[ix - 1][iy][it] + f(x[ix], y[iy], t[it])


def c_X(i):
    if i == 0:
        return cX / bX
    return cX / (bX - aX * c_X(i - 1))


def c_Y(i):
    if i == 0:
        return cY / bY
    return cY / (bY - aY * c_Y(i - 1))


def d_X(ix, iy, it):
    if ix == 0:
        return diX(ix, iy, it - 1) / bX
    return (diX(ix, iy, it - 1) - aX * d_X(ix - 1, iy, it)) / (bX - aX * c_X(ix - 1))


def d_Y(ix, iy, it):
    if iy == 0:
        return diY(ix, iy, it - 1) / bY
    return (diY(ix, iy, it - 1) - aX * d_Y(ix, iy - 1, it)) / (bY - aY * c_Y(iy - 1))


def Un_x(iy, it):
    N = x.size - 2
    c_vec = np.empty(N)
    for i in range(0, N):
        c_vec[i] = c_X(i)

    d_vec, xn = (np.empty(N), np.empty(N))
    for i in range(0, N):
        d_vec[i] = d_X(i, iy, it)
        xn[i] = d_vec[i]

    for i in range(N - 1, 0, -1):
        xn[i - 1] = d_vec[i - 1] - c_vec[i - 1] * xn[i]

    for i in range(1, x.size - 1):
        u[i, iy, it] = xn[i - 1]


def Un_y(ix, it):
    N = x.size - 2
    c_vec = np.empty(N)
    for i in range(0, N):
        c_vec[i] = c_Y(i)

    d_vec, yn = (np.empty(N), np.empty(N))
    for i in range(0, N):
        d_vec[i] = d_Y(i, ix, it)
        yn[i] = d_vec[i]

    for i in range(N - 1, 0, -1):
        yn[i - 1] = d_vec[i - 1] - c_vec[i - 1] * yn[i]

    for i in range(1, x.size - 1):
        u[ix, i, it] = yn[i - 1]


def calculate():
    for it in range(1, t.size):
        print(it)
        for iy in range(1, y.size - 1):
            Un_x(iy, it)
        for ix in range(1, x.size - 1):
            Un_y(ix, it)


def temperature_map(it):
    temp_map = np.zeros((u.shape[0], u.shape[1]))
    for i in range(0, u.shape[0]):
        for j in range(0, u.shape[1]):
            temp_map[i][j] = u[i][j][it]

    return temp_map


def main():
    # X, Y = np.meshgrid(x, y)
    # F = []
    # for it in t:
    #     F.append(np.vectorize(f)(X,Y,it))
    # # F = np.vectorize(f)(X,Y,t)
    # def update_plot(frame):
    #     nonlocal plot
    #     plot.remove()
    #     plot = ax.plot_surface(X, Y, F[frame], cmap='magma', vmin=0, vmax=1)
    #     return plot,
    #
    # fig = plt.figure(figsize=(100, 100), dpi=200)
    # ax = plt.axes(projection='3d')
    # ax.set_zlim(0, 1)
    # plot = ax.plot_surface(X, Y, F[0])
    # fig.colorbar(plot, ax=ax)
    # ax.set_title('3D Heat map')
    # anim = animation.FuncAnimation(fig, update_plot, len(t), interval=0.1)
    # plt.show()

    calculate()

    def update(frame):
        nonlocal plot
        plot.remove()
        tmp = temperature_map(frame)[1:-1, 1:-1]
        plot = ax.pcolormesh(x[1:-1], y[1:-1], tmp, cmap='magma')
        plt.axis('off')
        return plot,

    fig = plt.figure()
    ax = plt.axes()
    plot = ax.pcolormesh(x[1:-1], y[1:-1], temperature_map(0)[1:-1, 1:-1], cmap='magma')
    plt.axis('off')
    ax.set_title('Heat map')
    anim = animation.FuncAnimation(fig, update, t.size, interval=30)
    plt.show()


main()