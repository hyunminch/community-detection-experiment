import time

from cdlib import algorithms, viz, evaluation
import networkx as nx
import matplotlib.pyplot as plt


threshold_size = 3000


def benchmark_running_time(G):
    t0 = time.time()
    coms = algorithms.louvain(G)
    louvain_modularity = evaluation.newman_girvan_modularity(G, coms)
    z_louvain_modularity = evaluation.z_modularity(G, coms)
    t1 = time.time()
    coms = algorithms.leiden(G)
    leiden_modularity = evaluation.newman_girvan_modularity(G, coms)
    z_leiden_modularity = evaluation.z_modularity(G, coms)
    t2 = time.time()

    print('Leiden Running Time: ', t2 - t1)
    print('Leiden Modularity: ', leiden_modularity)
    print('Leiden Z Modularity: ', z_leiden_modularity)
    print('Louvain Running Time: ', t1 - t0)
    print('Louvain Modularity: ', louvain_modularity)
    print('Louvain Z Modularity: ', z_louvain_modularity)

    if len(G) < threshold_size:
        t0 = time.time()
        coms = algorithms.greedy_modularity(G)
        cnm_modularity = evaluation.newman_girvan_modularity(G, coms)
        z_cnm_modularity = evaluation.z_modularity(G, coms)
        t1 = time.time()
        coms = algorithms.girvan_newman(G, level=3)
        gn_modularity = evaluation.newman_girvan_modularity(G, coms)
        z_gn_modularity = evaluation.z_modularity(G, coms)
        t2 = time.time()

        print('CNM Running Time: ', t1 - t0)
        print('CNM Modularity: ', cnm_modularity)
        print('CNM Z Modularity: ', z_cnm_modularity)
        print('Girvan-Newman Running Time', t2 - t1)
        print('Girvan-Newman Modularity: ', gn_modularity)
        print('Girvan-Newman Z Modularity: ', z_gn_modularity)


def main():
    with open('politicians.csv') as f:
        politicians = f.readlines()

    with open('git.csv') as f:
        git = f.readlines()
    
    karate_club = nx.karate_club_graph()
    facebook_politicians = nx.parse_edgelist(politicians, nodetype=int)
    git = nx.parse_edgelist(git, nodetype=int)

    print('Benchmarking karate club...')
    benchmark_running_time(karate_club)
    print('Benchmarking facebook politicians...')
    benchmark_running_time(facebook_politicians)
    print('Benchmarking git...')
    benchmark_running_time(git)


if __name__ == '__main__':
    main()
