def volume(R):
    V = (4*3.14*float(R)**3)/3
    return V
r = input("Введите радиус сферы: ")
print(volume(r))