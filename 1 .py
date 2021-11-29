W = float(input('Введите ширину участка в футах: '))

H = float(input('Введите длинну участка в футах: '))

SQFT_PER_ACRE = (W * H)/43560
print ('Вот площадь участка в акрах -',SQFT_PER_ACRE)
