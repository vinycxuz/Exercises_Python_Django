""" Exemplo de modularizacao"""
from cmath import pi
import math

def area_triangulo(base: float, altura: float) -> float:
    resultado = (base * altura)/2
    return resultado

def area_circulo(raio: float) -> float:
    resultado = math.pi * (raio**2)
    return resultado

