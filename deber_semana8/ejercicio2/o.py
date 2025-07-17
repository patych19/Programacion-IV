## Ejercicio 2
## Expresión a resolver:** `((6 / 2) + (1 + 1)) * (4 - 2)`

import matplotlib.pyplot as plt
import networkx as nx
G = nx.DiGraph()
edges = [
    ('*', 'pri+'),    # '*' tiene como hijo izquierdo '+'
    ('*', '-'),    # '*' tiene como hijo derecho '-'
    ('pri+', '/'),    # '+' tiene como hijo izquierdo '/'
    ('pri+', 'seg+'),    # '+' tiene como hijo derecho '+'
    ('/', '6'),    # '/' tiene como hijo izquierdo '6'
    ('/', '2a'),    # '/' tiene como hijo derecho '2'
    ('seg+', '1a'),    # '+' tiene como hijo izquierdo '1'
    ('seg+', '1b'),    # '+' tiene como hijo derecho '1'
    ('-', '4'),    # '-' tiene como hijo izquierdo '4'
    ('-', '2b')     # '-' tiene como hijo derecho '2'
]

pos = {
    '*': (0, 2),        # Raíz
    'pri+': (-1.5, 1),  # Hijo izquierdo de '*'
    '-': (1.5, 1),      # Hijo derecho de '*'
    '/': (-2, 0),       # Hijo izquierdo de 'pri+'
    '6': (-2.5, -1),    
    '2a': (-1.5, -1),
    'seg+': (0, 0),
    '1a': (-0.5, -1),
    '1b': (0.5, -1),
    '4': (1, 0),
    '2b': (2, 0)
}

# dibujamos el arbol

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

plt.title("Árbol de expresión: ((6 / 2) + (1 + 1)) * (4 - 2)")
plt.axis('off')
plt.show()

