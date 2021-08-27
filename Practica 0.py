#******************************************************************************
#* Autor: Señorito Antonio
#* Descripcion:  Rangos y Aleatorio
#* Fecha: 25/08/2021
#* Version: 1 Padrino
#******************************************************************************

#Libreria para datos aleatorios
import random 

#Libreria para generar graficas Gauss
import matplotlib.pyplot as plt

#Numero aleatorio
print(random.randint(1,20))

#Rango aleatorio
print(random.randrange(10,100, 2))

#Recomendar una lista al azar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Lista original', lista)

#Genera una grafica de campana Gauss
random.shuffle(lista)
print('Lista mix mix', lista)
campana = [random.gauss(1, 0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show()