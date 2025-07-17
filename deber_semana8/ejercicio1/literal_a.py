# ejercicio 1 literal a 
import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
edges = [
    ('*', '+'),    # '+' tiene como hijo izquierdo '/'
    ('*', '-'),    # '+' tiene como hijo derecho '*'
    ('+', '7'),    # '/' tiene como hijo izquierdo '8'
    ('+', '2'),    # '/' tiene como hijo derecho '2'
    ('-', '5'),    # '*' tiene como hijo izquierdo '3'
    ('-', '3')     # '*' tiene como hijo derecho '4'
]

# Agregamos las aristas al grafo
G.add_edges_from(edges)

pos = { 
    '*': (0, 2),     # Raíz
    '+': (-1.5, 1),  # Hijo izquierdo de '+'
    '-': (1.5, 1),   # Hijo derecho de '+'
    '7': (-2, 0),    # Hijo izquierdo de '/'
    '2': (-1, 0),    # Hijo derecho de '/'
    '5': (1, 0),     # Hijo izquierdo de '*'
    '3': (2, 0)      # Hijo derecho de '*'


}
# Dibujamos el árbol
plt.figure(figsize=(10, 5))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=14,
    font_weight='bold',
    arrows=True
)
plt.title("Árbol de expresión: ((7 + 2) * (5 - 3))")
plt.axis('off')
plt.show()


# resultado de la operacion 
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def construir_arbol():  
    raiz = Nodo('*')
    raiz.izq = Nodo('+')
    raiz.der = Nodo('-')
    raiz.izq.izq = Nodo(7)
    raiz.izq.der = Nodo(2)
    raiz.der.izq = Nodo(5)
    raiz.der.der = Nodo(3)
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
print("\n\t GRAFO : ((7 + 2) * (5 - 3))")
print("\n\t Resultado del grafo N°1 : ", resultado)
print("\t------------------------------------------")