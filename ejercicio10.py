#10_Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
# 55% del promedio de sus tres calificaciones parciales.
# 30% de la calificación del examen final.
# 15% de la calificación de un trabajo final.

calificacion1=0
calificacion2=0
calificacion3=0
examen_final=0
trabajo_final=0

calificacion1=(int)(input("Nota primera calificación: \n"))
calificacion2=(int)(input("Nota segunda calificación: \n"))
calificacion3=(int)(input("Nota tercera calificación: \n"))
examen_final=(int)(input("Nota examen final: \n"))
trabajo_final=(int)(input("Nota trabajo final: \n"))

print("La nota final es de", (((calificacion1+calificacion2+calificacion3)/3)*0.55)+(examen_final*0.3)+(trabajo_final*0.15))