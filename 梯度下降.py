#梯度下降
y1 = [95.364693, 97.217205,75.195834, 60.105519, 49.342380,37.400286,51.057128,25.500619,5.259608]  # 价格

x1 = [0.000000,1.000000,2.000000,3.000000,4.000000,5.000000,6.000000,7.000000,8.000000,]  # 面积

z1 = [3,3,2,4,5,3,2,4,2]


def h0(o0, o1, o2, x, z):
    return o1 * x + o2 * z + o0


# 根据对o0 o1 o2求导，分别求和得
def get_o0(o0, o1, o2, x, z):
    s=0
    for each in range(9):
        s = s + h0(o0, o1, o2, x1[each], z1[each]) - y1[each]

    return s


def get_o1(o0, o1, o2, x, z):
    s=0
    for each in range(9):
        s = s + (h0(o0, o1, o2, x1[each], z1[each]) - y1[each]) * x1[each]

    return s


def get_o2(o0, o1, o2, x, z):
    s=0
    for each in range(9):
        s = s + (h0(o0, o1, o2, x1[each], z1[each]) - y1[each]) * z1[each]
    return s

def main():
    a0 = a1 = a2 = 0
    b0 = get_o0(a0, a1, a2, x1, z1)
    b1 = get_o1(a0, a1, a2, x1, z1)
    b2 = get_o2(a0, a1, a2, x1, z1)
    print(b0,b1,b2)

    print("让程序跑一会")
    while abs(b0) > 0.01 or abs(b1) > 0.010 or abs(b2) > 0.01:
        a0 = a0 - 0.03 * 0.11 * b0
        a1 = a1- 0.03 * 0.11* b1
        a2 = a2 - 0.03 * 0.11 * b2
        b0 = get_o0(a0, a1, a2, x1, z1)
        b1 = get_o1(a0, a1, a2, x1, z1)
        b2 = get_o2(a0, a1, a2, x1, z1)
        print(b0, b1, b2)

    print(a0, a1, a2)


if __name__ == "__main__":
    main()
