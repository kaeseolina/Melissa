from math import sqrt

def svobodnoe_padenie(high):
    vf = sqrt(0 ** 2) + 2 * 9.8 * high
    print(f'скорость при приземлении равна {vf} м/c2')

h = int(input('сколько метров высота падения? '))
svobodnoe_padenie(h)
