# importamos las librerias necesarias
import networkx as nx
import matplotlib.pyplot as plt

# Creamos el grafo
G = nx.Graph()
# Añadimos las aristas junto a sus pesos (costos)
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

pos = nx.spring_layout(G, seed=40)
ciudades_costeras = {"Manta", "Portoviejo", "Guayaquil"}

def camino_mas_barato(origen, destino, pasar_por_costera=False):
    # Si no se requiere pasar por costera, usa Dijkstra normal
    if not pasar_por_costera:
        camino = nx.dijkstra_path(G, source=origen, target=destino, weight='weight')
        costo = nx.dijkstra_path_length(G, source=origen, target=destino, weight='weight')
        pasa_por_costera = any(ciudad in camino for ciudad in ciudades_costeras)
        return camino, costo, pasa_por_costera
    # Si se requiere pasar por costera, busca todos los caminos y el más barato que pase por una costera
    caminos = list(nx.all_simple_paths(G, source=origen, target=destino))
    mejor_camino = None
    mejor_costo = float('inf')
    for camino in caminos:
        if any(ciudad in camino for ciudad in ciudades_costeras):
            costo = sum(G[camino[i]][camino[i+1]]['weight'] for i in range(len(camino)-1))
            if costo < mejor_costo:
                mejor_costo = costo
                mejor_camino = camino
    if mejor_camino:
        return mejor_camino, mejor_costo, True
    else:
        # Si no existe camino que pase por costera, retorna el más barato normal
        camino = nx.dijkstra_path(G, source=origen, target=destino, weight='weight')
        costo = nx.dijkstra_path_length(G, source=origen, target=destino, weight='weight')
        return camino, costo, False

# Ejemplo de uso:
origen = "Ibarra"
destino = "Loja"
pasar_por_costera = True  # Cambia a False si no quieres obligar a pasar por costera

camino, costo, pasa_por_costera = camino_mas_barato(origen, destino, pasar_por_costera)

plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lawngreen', node_size=2000, font_size=16,
        font_color='black', font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

if pasa_por_costera:
    path_edges = list(zip(camino, camino[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
    plt.title(f"Ruta más económica de {origen} a {destino} (con ciudad costera)", fontsize=18, fontweight='bold', color='darkblue')
else:
    plt.title(f"Ruta más económica de {origen} a {destino} (sin ciudad costera)", fontsize=18, fontweight='bold', color='red')

plt.axis('off')
plt.show()

print("\n\t==== CAMINO MÁS BARATO ENTRE IBARRA Y LOJA ====\n")
print(f"CONTEXTO: Se desea enviar mercancía desde {origen} hasta {destino}.")
print("\nEl camino más barato es:", camino)
print("El costo del camino más barato es:", costo, "$")
if pasar_por_costera:
    if pasa_por_costera:
        print("El camino pasa por al menos una ciudad costera.")
    else:
        print("No existe ruta que pase por una ciudad costera, se muestra la ruta más barata.")
else:
    print("No se requiere pasar por una ciudad costera.")

