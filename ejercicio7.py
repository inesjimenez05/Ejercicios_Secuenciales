#7_Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
minutos=0
horas=0

minutos=(int)(input("Dime los minutos \n"))
print(f"Los 140 {minutos} son {int(minutos/60)} horas y {minutos%60} minutos")