
import matplotlib.pyplot as plt
import networkx as nx

# Creamos un nuevo grafo dirigido (DiGraph)
G = nx.DiGraph()

# Definimos las conexiones entre nodos (estructura del árbol)
edges = [
    ('+', '/'),    # '+' tiene como hijo izquierdo '/'
    ('+', '*'),    # '+' tiene como hijo derecho '*'
    ('/', '8'),    # '/' tiene como hijo izquierdo '8'
    ('/', '2'),    # '/' tiene como hijo derecho '2'
    ('*', '3'),    # '*' tiene como hijo izquierdo '3'
    ('*', '4')     # '*' tiene como hijo derecho '4'
]

# Agregamos las aristas al grafo
G.add_edges_from(edges)

# Definimos las posiciones para una visualización jerárquica
pos = {
    '+': (0, 2),     # Raíz
    '/': (-1.5, 1),  # Hijo izquierdo de '+'
    '*': (1.5, 1),   # Hijo derecho de '+'
    '8': (-2, 0),    # Hijo izquierdo de '/'
    '2': (-1, 0),    # Hijo derecho de '/'
    '3': (1, 0),     # Hijo izquierdo de '*'
    '4': (2, 0)      # Hijo derecho de '*'
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
plt.title("Árbol de expresión: ((8 / 2) + (3 * 4))")
plt.axis('off')
plt.show()
# Evaluación de la expresión ((8 / 2) + (3 * 4)) usando árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def construir_arbol():
    raiz = Nodo('+')
    raiz.izq = Nodo('/')
    raiz.der = Nodo('*')
    raiz.izq.izq = Nodo(8)
    raiz.izq.der = Nodo(2)
    raiz.der.izq = Nodo(3)
    raiz.der.der = Nodo(4)
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

# Construimos y evaluamos el árbol
arbol = construir_arbol()
resultado = evaluar(arbol)
print(resultado)




