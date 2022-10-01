#3_Dados los catetos de un triángulo rectángulo, calcular su hipotenusa

cateto1=0
cateto2=0
hipotenusa=0

cateto1= (int)(input("Cuánto mide el primer cateto: \n"))
cateto2= (int)(input("Cuánto mide el segundo cateto: \n"))

hipotenusa= (((cateto1**2)+(cateto2**2))**0.5)

print("La hipotenusa del triáungulo es", hipotenusa)