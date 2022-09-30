#Ejercicio_2

from email.mime import base


base=0
altura=0

base=(int)(input("Di la base del rectángulo: \n"))
altura=(int)(input("Di la altura del rectángulo: \n"))

print("El área del rectángulo es: ", (base*altura))
print("El perímetro del rectángulo es: ",((2*base)+(2*altura)))