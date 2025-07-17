## Ejercicio 3
## Expresión a resolver:** `9 - ((3 * 2) + (8 / 4))`

import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()

edges = [
    ('+','-'), # '+' tiene como hijo izquierdo '-'
    ('+','/'), # '+' tiene como hijo derecho '/'
    ('-', '9'), # '-' tiene como hijo izquierdo '9'
    ('-','*'), # '-' tiene como hijo derecho '*'
    ('*','3'), # '*' tiene como hijo izquierdo '3'
    ('*','2'), # '*' tiene como hijo derecho '2'
    ('/','8'), # '/' tiene como hijo izquierdo '8'
    ('/','4')  # '/' tiene como hijo derecho '4'

]

# Agregamos las aristas al grafo
G.add_edges_from(edges)
pos = {
    '+': (0, 2),     # Raíz
    '-': (-1.5, 1),  # Hijo izquierdo de '+'
    '/': (1.5, 1),   # Hijo derecho de '+'
    '9': (-2, 0),    # Hijo izquierdo de '-'
    '*': (-1, 0),    # Hijo derecho de '-'
    '3': (-1.5, -1), # Hijo izquierdo de '*'
    '2': (-0.5, -1), # Hijo derecho de '*'
    '8': (1, 0),     # Hijo izquierdo de '/'
    '4': (2, 0)      # Hijo derecho de '/'

}

#  dibujamos el arbol

plt.figure(figsize=(10, 5))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='chartreuse',
    node_size=2000,
    font_size=14,
    font_weight='bold',
    arrows=True
)

plt.title("Árbol de expresión: 9 - ((3 * 2) + (8 / 4))")
plt.axis('off')
plt.show()

# resultado de la operacion

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def construir_arbol():
    raiz = Nodo('-')
    raiz.izq = Nodo(9)
    raiz.der = Nodo('+')
    raiz.der.izq = Nodo('*')
    raiz.der.der = Nodo('/')
    raiz.der.izq.izq = Nodo(3)
    raiz.der.izq.der = Nodo(2)
    raiz.der.der.izq = Nodo(8)
    raiz.der.der.der = Nodo(4)
    return raiz

def evaluar(nodo):
    if isinstance(nodo.valor, int):
        return nodo.valor
    izq = evaluar(nodo.izq)
    der = evaluar(nodo.der)
    if nodo.valor == '+':
        return izq + der
    elif nodo.valor == '-':
        return izq - der
    elif nodo.valor == '*':
        return izq * der
    elif nodo.valor == '/':
        return izq / der
    
arbol = construir_arbol()
resultado = evaluar(arbol)
print("\t------------------------------------------")
print("\n\t GRAFO: 9 - ((3 * 2) + (8 / 4))")
print(" \n\t El resultado del grafo N° 3 es: ", resultado)
print("\t------------------------------------------")