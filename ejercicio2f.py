#2_Calcular el perímetro y área de un triángulo dada su base y su altura.

def imprimir_area (base:int, altura:int):
    area= base*altura
    return area


def imprimir_perimetro (base:int, altura:int):
    perimetro= (base+altura)*2
    return (perimetro)


#Devuelvo una lista con área y perímetro

def imprimir_area_y_perimetro (base:int, altura:int):
    area= imprimir_area (base, altura)
    perimetro= imprimir_perimetro(base,altura)
    vCuenta= []
    vCuenta.append (area)
    vCuenta.append(perimetro)
    return vCuenta

#Principal
lado1= int(input("Dime el valor del lado 1 \n"))
lado2= int(input("Dime el valor del lado 2 \n"))

vNum= imprimir_area_y_perimetro(lado1,lado2)
print("El área es", vNum[0])
print("El perímetro es", vNum[1])