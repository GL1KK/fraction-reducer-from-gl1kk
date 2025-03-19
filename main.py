drob = input("Введите в формате x/y x-числитель y-знаминатель")

values = list(map(int, drob.split('/')))

def nod(value1, value2):
    while value2 != 0:
        value1, value2 = value2, value1 % value2
    return value1
        
valueq1 = values[0]
valueq2 = values[1]

nod_value = nod(valueq1, valueq2)

simpvalue1 = valueq1 // nod_value
simpvalue2 = valueq2 // nod_value

print(f"{simpvalue1}/{simpvalue2}")