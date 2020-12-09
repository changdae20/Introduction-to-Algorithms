import ast
import numpy as np

def load_args(txt_path):
    with open(txt_path, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        edge_list = ast.literal_eval(lines[1])
        src = int(lines[2])
        dst = int(lines[3])
        k = int(lines[4])

    return n, edge_list, src, dst, k

def build_graph(n, edge_list):
    '''
    ############################ Function description ############################
    Design a function that returns the graph, given edge_list.
    A graph can be of any type, such as list, dict or class.
    ##############################################################################
    '''
    graph = np.ones([n,n])
    graph = float("inf") * graph
    ##### Please write your code down here #####
    for i in range(len(edge_list)):
        graph[edge_list[i][0]][edge_list[i][1]] = edge_list[i][2]
    return graph


def find_cheapest_total_fare(n, edge_list, src, dst, k):
    '''
    ############################ Function description ############################

    Design a function that returns the cheapest total fare, given n, edge_list, src, dst, k.
    If there is no available path, return -1.

    ##############################################################################
    '''
    total_fare = 0
    graph = build_graph(n, edge_list)
    ##### Please write your code down here #####
    d = float("inf") * np.ones([n])
    d[src] = 0

    for i in range(k-1):
        d_copy = d*1
        for u in range(n):
            for v in range(n):
                if(graph[u][v]<float("inf")):
                    if(d[v] > d_copy[u] + graph[u][v]):
                        d[v] = d[u] + graph[u][v]

    total_fare = -1 if d[dst]==float("inf") else d[dst]                   
    return total_fare


if __name__ == '__main__':
    '''
    # The input will be randomly changed by TAs when grading.    
    # You can freely define a new function or class.
    # You should "not" modify the "main" function
    # Only the python standard library(https://python.readthedocs.io/en/stable/library/index.html) and numpy are available.
    '''
    input_txt = 'input.txt'
    args = load_args(input_txt)

    output = find_cheapest_total_fare(*args)
    print(f'The cheapest total fare from {args[2]} to {args[3]} is : {output}')



