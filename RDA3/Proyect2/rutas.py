import networkx as nx

def construir_grafo():
    G = nx.Graph()
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
    return G

def calcular_ruta(origen, destino):
    G = construir_grafo()
    ciudades_costeras = {"Manta", "Portoviejo", "Guayaquil"}

    try:
        camino = nx.dijkstra_path(G, origen, destino, weight='weight')
        costo = nx.dijkstra_path_length(G, origen, destino, weight='weight')
        pasa_costera = any(ciudad in camino for ciudad in ciudades_costeras)
        return camino, costo, pasa_costera
    except nx.NetworkXNoPath:
        return None, None, None

