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



#class Vehiculo:
#    color = 'blanco'
#    ruedas = 4
#    puertas = 4
#
#class Coche(Vehiculo):
#    velocidad = '100km/h'
#    cilindrada = '120cv'
#
#peugeot = Coche()
#print(peugeot.color, peugeot.ruedas, peugeot.puertas, peugeot.velocidad, peugeot.cilindrada)

#
#class Alumno:
#    nombre = 'Pedro'
#    nota = 5
#
#    def imprimir(self):
#        print(self.nombre)
#        print(self.nota)
#    
#    def aprobado(self):
#        if self.nota >= 5: print('Está aprobado')
#        else: print('está suspendido')
#pedro = Alumno()
#pedro.imprimir()
#pedro.aprobado()
#

#from operaciones import maths
#
#print(maths.sumar(2, 2))
#
#print(maths.restar(2, 2))
#
#print(maths.multi(2, 2))
#
#print(maths.divi(2, 2))

#file = open('../py/filename.txt', 'w')
#file.write('Primera línea \n')
#
#file = open('../py/filename.txt', 'r')
#datos = file.read()
#print(datos)
#import pickle
#
#class Vehiculo:
#    color = 'rojo'
#    vel = 100
#    def __init__(self, color, vel):
#        self.color = color
#        self.vel = vel
#    def getColor(self):
#        return self.color 
#
#f = open('datos.bin', 'rb')
#coche = pickle.load(f)
#f.close()
#
#print(type(coche))
#print(coche.getColor())



#paises= []
#for i in range(5):
#    paises.append(input('Introduce un pais: '))
#paises = set(paises)
#l = list(paises)
#l.sort()
#print(f'Los paises son {l}')


#from functools import reduce
#lista = [3, 1, 4, 7, 2, 8, 9, 11, 10]
#filtrada = []
#
#for elemento in lista:
#    if elemento % 2:
#        filtrada.append(elemento)
#
#print(filtrada)
#
#def add(x, y):
#    return x + y
#print(reduce(add, filtrada))


#import tkinter
#from tkinter import RIGHT, ttk
#import sys
#from turtle import right
#
#window = tkinter.Tk()
#
#window.columnconfigure(0,weight=1)
#window.columnconfigure(0,weight=4)
#
#selected = tkinter.StringVar()
#
#r1 = ttk.Radiobutton(window, text='Si', value='1', variable=selected)
#r2 = ttk.Radiobutton(window, text='No', value='2', variable=selected)
#r3 = ttk.Radiobutton(window, text='Quizá', value='3', variable=selected)
#
#r1.grid(column=0, row=1, pady=5, padx=5)
#r2.grid(column=0, row=2, pady=5, padx=5)
#r3.grid(column=0, row=3, pady=5, padx=5)
#
#def reiniciar(event):
#    selected.set(None)
#
#botonReinicio= tkinter.Button(window, text='Reinicio', command=reiniciar)
#botonReinicio.grid(column=0, row=4, pady=5, padx=5)
#botonReinicio.bind('<Button-1>', reiniciar)
#
#window.mainloop()

#import sys
#import tkinter
#from tkinter import ttk
#
#
#window = tkinter.Tk()
#
#window.columnconfigure(0,weight=1)
#window.columnconfigure(0,weight=4)
#label = tkinter.Label(window, text='Lista', bg='blue', fg='black')
#label.grid(column=0, row=0, sticky=tkinter.W)
#lista = ['Windows', 'macOS', 'Linux', 'MS DOS', 'BeOS']
#lista_items = tkinter.StringVar(value=lista)
#listbox = tkinter.Listbox(window, height=20, listvariable=lista_items)
#listbox.grid(column=0, row=2, sticky=tkinter.W)
#
#window.mainloop()
#sys.exit()

import sqlite3

conn = sqlite3.connect('ficher.db')

cursor = conn.cursor()

nombre=input('Escribe el nombre del alumno: ')
query = f"SELECT * FROM Alumnos WHERE nombre='{nombre}'"
print("Query a ejecutar: ", query)

rows = cursor.execute(query)

data = rows.fetchone()
print('data es ', type(data))
print(data)

cursor.close()
conn.close()