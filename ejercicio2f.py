#2_Calcular el perímetro y área de un rectángulo dada su base y su altura.

def imprimir_areaYperimetro ():
    base=int(input("Diga la base: \n"))
    altura=int(input("Diga la altura: \n"))
    area=(base*altura)/2
    perimetro=base+altura+((altura**2+base**2)**(1/2))
    print("El área del triángulo es ", area, "y el perímetro del triángulo es ", perimetro)

imprimir_areaYperimetro()

'''
def imprimir_perimetro():
    base=int(input("Diga la base: \n"))
    altura=int(input("Diga la altura: \n"))
    return base+altura+((altura**2+base**2)**(1/2))

def imprimir_area():
    base=int(input("Diga la base: \n"))
    altura=int(input("Diga la altura: \n"))
    return (base*altura)/2

perimetro=imprimir_perimetro()
area=imprimir_area()

print("El perímetro del triángulo es: ", perimetro)
print("El área del triángulo es", area)
'''