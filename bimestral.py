"""Ejercicio Bimestral
Programa que recibe el valor del cheque a cambiar e informa cuántos billetes de cada denominación debe entregar."""


print("----------------------------")
print("---------- CAJERO ----------")
print("----------------------------")

# input 
cheque = int (input ("Digite el valor del cheque: "))
conta_monedas_100=0
conta_billetes_10000=0
conta_billetes_2000=0

# processing
while cheque !=0:
    monedas_100=cheque
    billetes_10000=(monedas_100-monedas_100%10000)//10000
    monedas_100=monedas_100%10000
    billetes_2000=(monedas_100-monedas_100%2000)//2000
    monedas_100=monedas_100%2000
    monedas_100=(monedas_100-monedas_100%100)//100
    monedas_100=monedas_100%100   
    print ('Cantidad de billetes de 10000: ' + repr (billetes_10000))
    print ('Cantidad de billetes de 2000: ' + repr (billetes_2000))
    print ('Cantidad de monedas de 100: ' + repr (monedas_100))
    conta_monedas_100=conta_monedas_100 + monedas_100
    conta_billetes_10000=conta_billetes_10000 + billetes_10000
    conta_billetes_2000=conta_billetes_2000 + billetes_2000
    cheque = int (input ("Digite el valor del cheque: "))

else:
    print("Fin del día")

# output

print("El total de billetes de 10000 utilizados fueron: " + str(conta_billetes_10000))
print("El total de billetes de  de 2000 utilizados fueron: " + str(conta_billetes_2000))
print("El total de monedas de 100 utilizadas fueron:  " + str(conta_monedas_100))
