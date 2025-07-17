


# importamos las librerias

import networkx as nx
import matplotlib.pyplot as plt     

# creamos el grafo

G = nx.Graph()

# añadimos las aristas junto a sus pesos(costos)

"""Quito → Ambato: 10
Quito → Riobamba: 18
 Ambato → Cuenca: 25
 Riobamba → Cuenca: 20"""

G.add_edge("Quito", "Ambato", weight=10)
G.add_edge("Quito","Riobamba",weight=18)
G.add_edge("Ambato", "Cuenca", weight=25)
G.add_edge("Riobamba", "Cuenca", weight=20)

# definimos la posicion de cada uno de los nodos 

pos = nx.spring_layout(G)

# dibujamos el grafo

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='mediumpurple', node_size=2000, font_size=16, font_color='black', font_weight='bold', edge_color='gray')

# mostramos los pesos de las aristas

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G,pos ,edge_labels=labels)

# titulo del grafo

plt.title("Grafo de Rutas entre Ciudades", fontsize=20, fontweight='bold', color='darkblue')
plt.axis('off') 
plt.show()

# encontramos el camino mas barato entre quito y cuenca 

camino_mas_barato = nx.dijkstra_path(G, source="Quito", target="Cuenca", weight='weight')
costo = nx.dijkstra_path_length(G, source="Quito", target="Cuenca", weight='weight')    

# mostramos los resultados
print("\n\t====CAMINO MAS BARATO ENTRE CUENCA Y QUITO=====\n")
print("CONTEXTO:Se desea entregar un paquete desde Quito a Cuenca donde se requeriere encontrar el camino mas barato ")
print("El camino más barato de Quito a Cuenca es:", camino_mas_barato)
print("El costo del camino más barato es:", costo)