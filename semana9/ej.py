import networkx as nx
import matplotlib.pyplot as plt

# Crear grafo dirigido y ponderado
G = nx.DiGraph()

# Agregar aristas con pesos (costos en USD)
G.add_edge("Ibarra", "Quito", weight=10)
G.add_edge("Quito", "Santo Domingo", weight=15)
G.add_edge("Quito", "Manta", weight=30)
G.add_edge("Santo Domingo", "Manta", weight=12)
G.add_edge("Manta", "Portoviejo", weight=5)
G.add_edge("Portoviejo", "Guayaquil", weight=20)
G.add_edge("Guayaquil", "Cuenca", weight=25)
G.add_edge("Cuenca", "Loja", weight=18)
G.add_edge("Quito", "Cuenca", weight=35)
G.add_edge("Santo Domingo", "Guayaquil", weight=22)
G.add_edge("Guayaquil", "Loja", weight=40)

# Fijar posiciones para visualización estable
pos = nx.spring_layout(G, seed=354)

# Dibujar el grafo
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='lawngreen', node_size=2000,
        font_size=14, font_weight='bold', arrows=True, arrowstyle='-|>', arrowsize=20)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo Dirigido: Rutas entre Ibarra y Loja", fontsize=18, color='darkgreen')
plt.axis('off')
plt.show()



# Definir ciudades costeras
costeras = {"Manta", "Portoviejo", "Guayaquil"}

# Obtener todas las rutas posibles más cortas en costo (puede haber varias con mismo costo)
rutas_posibles = nx.all_simple_paths(G, source="Ibarra", target="Loja")

# Filtrar las rutas que pasen por al menos una ciudad costera
rutas_validas = []
for ruta in rutas_posibles:
    if any(ciudad in ruta for ciudad in costeras):
        costo = sum(G[ruta[i]][ruta[i+1]]['weight'] for i in range(len(ruta) - 1))
        rutas_validas.append((ruta, costo))

# Verificar si hay alguna ruta válida
if rutas_validas:
    # Seleccionar la ruta más económica entre las válidas
    mejor_ruta, mejor_costo = min(rutas_validas, key=lambda x: x[1])

    # Mostrar resultados

    
    print("\n\t==== CAMINO MÁS ECONÓMICO ENTRE IBARRA Y LOJA (CON COSTERA) ====\n")
    print("Contexto: Se busca la ruta más económica de Ibarra a Loja que pase por una ciudad costera.")
    print("Ruta encontrada:", " → ".join(mejor_ruta))
    print("Costo total:", mejor_costo, "$")
    print("Ciudades costeras en la ruta:", costeras.intersection(mejor_ruta))


else:
    print("No hay ninguna ruta de Ibarra a Loja que pase por una ciudad costera.")
