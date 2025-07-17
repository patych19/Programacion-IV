import matplotlib.pyplot as plt
import networkx as nx

# Crear el grafo dirigido
G = nx.DiGraph()

# Definimos las conexiones del árbol de expresión
edges = [
    ('/', '*'),   # '/' tiene como hijo izquierdo '*'
    ('/', '-2'),  # '/' tiene como hijo derecho '-2'
    ('*', '-1'),  # '*' tiene como hijo izquierdo '-1'
    ('*', '+1'),  # '*' tiene como hijo derecho '+1'
    ('-1', '10'), # '-1' tiene como hijo izquierdo '10'
    ('-1', '2'),  # '-1' tiene como hijo derecho '2'
    ('+1', '6'),  # '+1' tiene como hijo izquierdo '6'
    ('+1', '1'),  # '+1' tiene como hijo derecho '1'
    ('-2', '8'),  # '-2' tiene como hijo izquierdo '8'
    ('-2', '+2'), # '-2' tiene como hijo derecho '+2'
    ('+2', '3'),  # '+2' tiene como hijo izquierdo '3'
    ('+2', '1b')  # '+2' tiene como hijo derecho '1b'
] 

# Agregar aristas al grafo
G.add_edges_from(edges)

# Posiciones definidas manualmente para buena visualización
pos = {
    '/': (0, 3),
    '*': (-2, 2),
    '-2': (2, 2),
    '-1': (-3, 1),
    '+1': (-1, 1),
    '10': (-3.5, 0),
    '2': (-2.5, 0),
    '6': (-1.5, 0),
    '1': (-0.5, 0),
    '8': (1.5, 1),
    '+2': (2.5, 1),
    '3': (2, 0),
    '1b': (3, 0)
}

# Dibujar el grafo
plt.figure(figsize=(12, 6))
nx.draw(
    G, pos,
    with_labels=True,
    node_color='skyblue',
    node_size=2000,
    font_size=14,
    font_weight='bold',
    arrows=True
)

plt.title("Árbol de expresión: ((10 - 2) * (6 + 1)) / (8 - (3 + 1))", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()


# resultado de la operacion

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

def construir_arbol():
    raiz = Nodo('/')
    raiz.izq = Nodo('*')
    raiz.der = Nodo('-')
    raiz.izq.izq = Nodo('-')
    raiz.izq.der = Nodo('+')
    raiz.izq.izq.izq = Nodo(10)
    raiz.izq.izq.der = Nodo(2)
    raiz.izq.der.izq = Nodo(6)
    raiz.izq.der.der = Nodo(1)
    raiz.der.izq = Nodo(8)
    raiz.der.der = Nodo('+')
    raiz.der.der.izq = Nodo(3)
    raiz.der.der.der = Nodo(1)
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
print("\n\t------------------------------------------")
print("\n\tGRAFO: ((10 - 2) * (6 + 1)) / (8 - (3 + 1))")
print("\n\tEl resultado del grafo N° 4 es:", resultado)
print("\n\t------------------------------------------")
