## Ejercicio 5
## Expresión a resolver:** `(5 + (2 * (8 - 3))) / (6 - (1 + 2))`

import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo dirigido
G = nx.DiGraph()

edges = [
    ('/', 'pri+'),      # '/' tiene como hijo izquierdo 'pri+'
    ('/', 'pri-'),      # '/' tiene como hijo derecho 'pri-'
    ('pri+', '5'),      # 'pri+' tiene como hijo izquierdo '5'
    ('pri+', 'seg*'),   # 'pri+' tiene como hijo derecho 'seg*'
    ('seg*', '2'),      # 'seg*' tiene como hijo izquierdo '2'
    ('seg*', 'seg-'),   # 'seg*' tiene como hijo derecho 'seg-'
    ('seg-', '8'),      # 'seg-' tiene como hijo izquierdo '8'
    ('seg-', '3'),      # 'seg-' tiene como hijo derecho '3'
    ('pri-', '6'),      # 'pri-' tiene como hijo izquierdo '6'
    ('pri-', 'seg+'),   # 'pri-' tiene como hijo derecho 'seg+'
    ('seg+', '1'),      # 'seg+' tiene como hijo izquierdo '1'
    ('seg+', '2b')      # 'seg+' tiene como hijo derecho '2b'
]

# Agregamos las aristas
G.add_edges_from(edges)

pos = {
    '/': (0, 3),
    'pri+': (-2, 2),
    'pri-': (2, 2),
    '5': (-3, 1),
    'seg*': (-1, 1),
    '2': (-1.5, 0),
    'seg-': (-0.5, 0),
    '8': (-0.7, -1),
    '3': (-0.3, -1),
    '6': (1, 1),
    'seg+': (3, 1),
    '1': (2.7, 0),
    '2b': (3.3, 0)
}

# Dibujar el grafo
plt.figure(figsize=(12, 6))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightgreen',
    node_size=2200,
    font_size=12,
    font_weight='bold',
    arrows=True
)

plt.title("Árbol de expresión: (5 + (2 * (8 - 3))) / (6 - (1 + 2))")
plt.axis('off')
plt.show()

# resultado de la operacion

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def construir_arbol():
    raiz = Nodo('/')
    raiz.izq = Nodo('+')
    raiz.der = Nodo('-')
    raiz.izq.izq = Nodo(5)
    raiz.izq.der = Nodo('*')
    raiz.izq.der.izq = Nodo(2)
    raiz.izq.der.der = Nodo('-')
    raiz.izq.der.der.izq = Nodo(8)
    raiz.izq.der.der.der = Nodo(3)
    raiz.der.izq = Nodo(6)
    raiz.der.der = Nodo('+')
    raiz.der.der.izq = Nodo(1)
    raiz.der.der.der = Nodo(2)
    return raiz


def evaluar(nodo):
    if isinstance(nodo.valor, (int, float)):
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
print(resultado)
print("\t------------------------------------------")
print("\n\t GRAFO: ((5 + (2 * (8 - 3))) / (6 - (1 + 2)))")
print("\n\t El resultado del grafo N°5 : ", resultado)
print("\t------------------------------------------")
