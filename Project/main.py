import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Physical constants
A = 10
b = 0.25
v = 2

# Other constants
MIN_VAL = 0
MAX_VAL = 100
STEP = 1
DELAY = 60 # delay between frames in ms
FLAG_Z = 1
FLAG_T = 2

z = np.arange(MIN_VAL, MAX_VAL, STEP)
t = np.arange(MIN_VAL, MAX_VAL, STEP)

size = z.size # z.size = t.size

# Wawe functions
def f1(i = -1, flag = 0): # i and flag are used in animation part
    if flag == FLAG_Z:
        return A * np.exp(-b*(z+i-v*t)**2)
    if flag == FLAG_T:
        return A * np.exp(-b*(z[i]-v*t[i])**2)
    return A * np.exp(-b*(z-v*t)**2)

def f2(i = -1, flag = 0): # i and flag are used in animation part
    if flag == FLAG_Z:
        return A * np.sin(b*(z+i-v*t))
    if flag == FLAG_T:
        return A * np.sin(b*(z[i]-v*t[i]))
    return A * np.sin(b*(z-v*t))

def f3():
    return A / (b*(z-v*t)**2 + 1)

def f4():
    return A * np.exp(-b*(b*z**2+v*t))

def f5():
    return A * np.sin(b * z) * np.cos((b * v * t) ** 3)

def show_graphs():
    fig, ([plt1, plt2], [plt3, plt4]) = plt.subplots(2, 2)

    plt1.plot(z, f1(), linestyle='--')
    for el, f in zip([plt1, plt2, plt3, plt4], [f2(), f3(), f4(), f5()]):
        el.plot(z, f, linestyle='--')
        el.grid(linestyle='--')
        el.set_xlim(MIN_VAL, MAX_VAL)
        el.set_ylim(-1.5 * A, 1.5 * A)

    plt.show()

def show_animation():
    fig, ([plt1, plt2], [plt3, plt4]) = plt.subplots(2, 2)

    line1, = plt1.plot(z, f1(), linestyle = 'dotted')
    plt1.grid(linestyle='--')
    plt1.set_xlim(MIN_VAL, MAX_VAL)
    plt1.set_ylim(-A, A)

    def animate1(i):
        i %= size
        line1.set_ydata(f1(i, FLAG_Z))
        return line1,

    ani1 = animation.FuncAnimation(fig, animate1, interval=DELAY, blit=True, save_count=50)

    line2, = plt2.plot(z, f2(), linestyle='dotted')
    plt2.grid(linestyle='--')
    plt2.set_xlim(MIN_VAL, MAX_VAL)
    plt2.set_ylim(-A, A)

    def animate2(i):
        i %= size
        line2.set_ydata(f2(i, FLAG_Z))
        return line2,

    ani2 = animation.FuncAnimation(fig, animate2, interval=DELAY, blit=True, save_count=50)

    line3, = plt3.plot(t, f1(), 'black')
    plt3.grid(linestyle='--')
    plt3.set_xlim(MIN_VAL, MAX_VAL / 2)
    plt3.set_ylim(-A, A)
    x_data1 = []
    y_data1 = []

    def animate3(i):
        global x_data1
        global y_data1

        i %= size
        if i == 0:
            x_data1 = []
            y_data1 = []

        x_data1.append(t[i])
        y_data1.append(f1(i, FLAG_T))

        line3.set_xdata(x_data1)
        line3.set_ydata(y_data1)

        return line3,

    ani3 = animation.FuncAnimation(fig, animate3, interval=DELAY, blit=True, save_count=50)

    line4, = plt4.plot(t, f2(), 'black')
    plt4.grid(linestyle='--')
    plt4.set_xlim(MIN_VAL, MAX_VAL)
    plt4.set_ylim(-A, A)
    x_data2 = []
    y_data2 = []

    def animate4(i):
        global x_data2
        global y_data2

        i %= size
        if i == 0:
            x_data2 = []
            y_data2 = []

        x_data2.append(t[i])
        y_data2.append(f2(i, FLAG_T))

        line4.set_xdata(x_data2)
        line4.set_ydata(y_data2)

        return line4,

    ani4 = animation.FuncAnimation(fig, animate4, interval=DELAY, blit=True, save_count=50)

    plt.show()

def main():
    show_graphs()
    show_animation()

if __name__ == '__main__':
    main()
