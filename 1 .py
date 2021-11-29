 start = time()
        func(*args)
        print(f'Время работы функции: {time() - start}')
    return vremyafunc

def decorat(func):
    def name(*args):
        print(f'Была вызвана функция {func.__name__}')
        func(*args)
    return name


@vremya
@decorat
def s_uchastka(l, w):
    print(f'Площадь участка равна {round(l * w / 43560, 6)} акров')

@vremya
@decorat
def svobodnoe_padenie(high):
    vf = sqrt(0 ** 2) + 2 * 9.8 * high
print(f'скорость при приземлении равна {vf} м/c')


l, w = int(input('введите длину: ')), int(input('введите ширину: '))
s_uchastka(l, w)
h = int(input('сколько метров высота падения? '))
svobodnoe_padenie(h)
