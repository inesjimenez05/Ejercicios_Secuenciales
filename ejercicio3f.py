#3_Dados los catetos de un triángulo rectángulo, calcular su hipotenusa

def calcularhipotenusa():
    cateto1= int(input("Cateto 1: \n"))
    cateto2= int(input("Cateto 2: \n"))
    print("La hipotenusa del triángulo es:", (((cateto1**2)+(cateto2**2))**(1/2)))

calcularhipotenusa()