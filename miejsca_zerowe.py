import math
a = int(input("Podaj współczynnik a: ")) 
b = int(input("Podaj współczynnik b: "))
c = int(input("Podaj współczynnik c: "))
zerowka = int(2-2) # zerowka bedzie oznaczac zero... nie pamietam nawet czemu tak wtedy to zrobilem
delta = int((b*b)-(4*a*c))
bcd = int(b*(-1)) 
print('Delta wynosi: ', str(delta))
if delta==zerowka:
 pdelta = math.sqrt(delta)
 print(" a pierwiastek z niej wynosi ", str(pdelta), ".")
 wyjs0 = (bcd/(2*a))
 print("Oto miejsce zerowe:", str(wyjs0))
if delta<0:
 print("Delta jest ujemna więc nie będzie żadnych miejsc zerowych :(")
if delta>0:
 pdelta = math.sqrt(delta)
 print(" a pierwiastek z niej wynosi ", str(pdelta), ".")
 wyjs1 = ((bcd+pdelta)/(2*a))
 wyjs2 = ((bcd-pdelta)/(2*a))
 print("Oto miejsca zerowe:", str(wyjs1), " i ", str(wyjs2), ".")
