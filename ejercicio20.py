#20_Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 
#céntimos o 10 céntimos).

monedas2=0
monedas1=0
monedas50=0
monedas20=0
monedas10=0

monedas2=(int)(input("Número de monedas de 2€ \n"))
monedas1=(int)(input("Número de monedas de 1€ \n"))
monedas50=(int)(input("Número de monedas de 50 cent \n"))
monedas20=(int)(input("Número de monedas de 20 cent \n"))
monedas10=(int)(input("Número de monedas de 10 cent \n"))

print("Total", ((monedas2*2)+monedas1), "euros", ((monedas50*50)+(monedas20*20)+(monedas10*10)), "céntimos")