#二维
import numpy as np
import matplotlib.pyplot as plt

y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
x1 = [-1, -2, -3, -0.2, 0.1, 0.3, 11, 9, 12, 13]


def h0(o0, o1, x1):
    return 1 / (1 + np.exp(-o0 - o1 * x1))


def get_o0(o0, o1, x1):
    s = 0
    for i in range(len(y)):
        s = s + ((1 / (1 + np.exp(-o0 - o1 * x1[i]))) - y[i])
    return s


def get_o1(o0, o1, x1):
    s = 0
    for i in range(len(y)):
        s = s + ((1 / (1 + np.exp(-o0 - o1 * x1[i]))) - y[i])*x1[i]
    return s


def main():
    a0 = a1 = 0
    b0 = get_o0(a0, a1, x1)
    b1 = get_o1(a0, a1, x1)

    print(b0, b1)

    while(abs(b0)>0.15 or abs(b1)>0.15):
        a0 = a0 - 0.001 * b0
        a1 = a1 - 0.001 * b1

        b0 = get_o0(a0, a1, x1)
        b1 = get_o1(a0, a1, x1)

        print(b0,b1 )

    print(a0, a1)
    x_1 = np.arange(-10, 10, 0.1)
    y_1 = 1 / (1 + np.exp(a0 + a1 * x_1))
    plt.plot(x_1, y_1)
    plt.show()


if __name__ == "__main__":
    main()
