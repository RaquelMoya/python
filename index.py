#print("Hola, soy Raquel")
#print("Estoy empezando el curso de python")
#print("Espero aprender mucho")

#hola = "Hola Mundo"

#print(hola)

#print(type(hola))




#edad = int(input('Dime tu edad: '))
#print(edad)
#
#if edad > 18:
#    print('Eres mayor de edad')
#else:
#    print('No eres mayor de edad')



#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
#impares = []
#
#for num in numeros:
#    if num %2 == 1:
#        impares.append(num)
#       
#print(impares)



#rango = list(range(1, 101))
#print(rango)
#print(list(reversed(rango)))





#from cmath import pi
#
#
#def triangulo (base, altura):
#    area = (base*altura)/2
#    return area
#
#def circulo (radio):
#    area = pi*radio**2
#    return area
#
#print(triangulo(1,2))
#print(circulo(2))
#
#def es_primo(num):
#    for n in range(2, num):
#        if num % n == 0:
#            print("No es primo", n, "es divisor")
#            return False
#    print("Es primo")
#    return True
#
#es_primo(13)
#es_primo(4)
#
#def es_bisiesto(anio: int) -> bool:
#    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
#
#print(es_bisiesto(2000))
#print(es_bisiesto(2001))



class Vehiculo:
    color = 'blanco'
    ruedas = 4
    puertas = 4

class Coche(Vehiculo):
    velocidad = '100km/h'
    cilindrada = '120cv'

peugeot = Coche()
print(peugeot.color, peugeot.ruedas, peugeot.puertas, peugeot.velocidad, peugeot.cilindrada)