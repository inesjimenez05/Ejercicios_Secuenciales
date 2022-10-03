#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de
#comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

salario=0
venta1=0
venta2=0
venta3=0

venta1=(int)(input("Cuánto ha ganado en la primera venta \n"))
venta2=(int)(input("Cuánto ha ganado en la segunda venta \n"))
venta3=(int)(input("Cuánto ha ganado en la segunda venta \n"))

print("La ganacia total ha sido de: ", ((venta1*1.1)+(venta2*1.1)+(venta3*1.1)), "€")