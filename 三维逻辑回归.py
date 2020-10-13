import numpy as np
import matplotlib.pyplot as plt
y=[0,0,0,1,1,1]
x1=[0.1,0.2,0.15,1.1,1.2,1.13]
x2=[0.1,0.2,0.15,1.1,1.2,1.13]
def h0(o0, o1, o2, x1, x2):
    return 1 / (1 + np.exp(-o0 - o1 * x1-o2*x2))
def get_o0(o0, o1, o2, x1, x2):
    s=0
    for i in range(len(y)):
        s =s+( 1 / (1 + np.exp(-o0 - o1 * x1[i]-o2*x2[i]))-y[i])
    return s
def get_o1(o0, o1, o2, x1, x2):
    s=0
    for i in range(len(y)):
        s =s+( 1 / (1 + np.exp(-o0 - o1 * x1[i]-o2*x2[i]))-y[i])*x1[i]
    return s
def get_o2(o0, o1, o2, x1, x2):
    s=0
    for i in range(len(y)):

        s =s+( 1 / (1 + np.exp(-o0 - o1 * x1[i]-o2*x2[i]))-y[i])*x2[i]
    return s
def main():
    a0 = a1 = a2 = 0
    b0 = get_o0(a0, a1, a2, x1, x2)
    b1 = get_o1(a0, a1, a2, x1, x2)
    b2 = get_o2(a0, a1, a2, x1, x2)
    print(b0, b1, b2)

    while(abs(b0)>0.01or abs(b1)>0.01or abs(b2)>0.01):
        a0 = a0 - 0.03 * b0
        a1 = a1 - 0.03 * b1
        a2 = a2 - 0.03 * b2
        b0 = get_o0(a0, a1, a2, x1, x2)
        b1 = get_o1(a0, a1, a2, x1, x2)
        b2 = get_o2(a0, a1, a2, x1, x2)
        print(b0, b1, b2)

    print(a0, a1, a2)



if __name__ == "__main__":
    main()
