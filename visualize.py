import time

from cdlib import algorithms, viz, evaluation
import networkx as nx
import matplotlib.pyplot as plt


G = nx.karate_club_graph()

def visualize(alg):
    coms = alg(G)
    pos = nx.spring_layout(G)
    viz.plot_network_clusters(G, coms, pos)
    plt.show()

visualize(algorithms.leiden)
