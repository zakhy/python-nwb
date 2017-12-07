import math
a = int(input("Podaj współczynnik a: "))
b = int(input("Podaj współczynnik b: "))
c = int(input("Podaj współczynnik c: "))
zerowka = int(2-2)
delta = int((b*b)-(4*a*c))
pdelta = math.sqrt(delta)
bcd = int(b*(-1))
print('Delta wynosi: ' + str(delta) + ' a pierwiastek z niej wynosi ' + str(pdelta) + ".")
if delta==zerowka:
 wyjs0 = (bcd/(2*a))
 print("Oto miejsce zerowe:" + str(wyjs0))
if delta<0:
 print("Delta jest ujemna więc nie będzie żadnych miejsc zerowych :(")
if delta>0:
 wyjs1 = ((bcd+pdelta)/(2*a))
 wyjs2 = ((bcd-pdelta)/(2*a))
 print("Oto miejsca zerowe:" + str(wyjs1) + " i " + str(wyjs2) + ".")
 



