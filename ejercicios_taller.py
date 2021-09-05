# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 23:40:54 2021

@author: Eduardo Alvear
"""

# Ejercicio 1.1 
def ejercicio1():
    y = ( ( 5 + 2 - 5)**2 * 5 + 8 / 2 - 30) / 2 * 5 - 3
    return y

# Ejercicio 1.2 
def ejercicio2():
    z = 5
    n = 3
    m = z - n
    y = (((z + 2 - n)**2 * m + 8 / 2 - 30) / 2 * 5 - 3 )**5 + 15 * 3 - 9 / 3
    return y

# Ejercicio 1.3
def ejercicio3():
    z = 5
    n = ((8+2-4)**2 * 5 + 8 + 7 / 2 - 30* 5 ) / 2 * 5 - 3;
    m = z**2 * 3 + n;
    y = ((((z+2-n)**2 * m+8/2 - 30) / 2 * 5 - 3)**5 + 15 * 3 - 9 / 3)**2 - 5 / 4
    return y


def ejercicio2(p, v, t):
    return (p * v) / (0.37 * (t + 460))

def ejercicio3(edad):
    return (200 - edad) / 10

def ejercicio4(inv1, inv2, inv3):
    total = inv1 + inv2 + inv3
    porcentaje1 = inv1 * 100 / total
    porcentaje2 = inv2 * 100 / total
    porcentaje3 = inv3 * 100 / total
    return porcentaje1, porcentaje2, porcentaje3

def ejercicio5(saldo):
    return saldo + (saldo * 0.015)

def ejercicio6(sueldo):
    ley = sueldo * 0.01
    seguro_social = sueldo * 0.04
    seguro_forsozo = sueldo * 0.005
    caja = sueldo * 0.05
    sueldo_final = sueldo - ley - seguro_social - seguro_forsozo - caja

    return ley, seguro_social, seguro_forsozo, caja, sueldo_final

def ejercicio7(n_palabras, tam, col):
    return (n_palabras * 20000) + (tam * 15000) + (col * 25000)

def ejercicio8(tiempo):
    return 100000 + (120000 * (tiempo - 1))

def ejercicio9(tiempo_horas):
    descuento = (tiempo_horas * 20000) * 0.05
    pago = tiempo_horas * 20000 - descuento
    return pago, descuento

def ejercicio10(inicial, final):
    return (inicial - final) - ((inicial - final) * 0.2)
