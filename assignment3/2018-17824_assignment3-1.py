import argparse


def parse_args(p_list):
    parser = argparse.ArgumentParser()
    parser.add_argument('--A', default='6329', type=int)
    parser.add_argument('--B', default='8537', type=int)
    args = parser.parse_args()
    if args.A not in p_list or args.B not in p_list:
        parser.error("At least one of the input is not a prime number with 4 digits")

    return args


def load_primes(txt_path):
    f = open(txt_path, "r")
    lines = f.readlines()
    all = "".join(lines) # join lines
    all = all.split()
    all = map(int, all)
    f.close()

    # only want the 4-digit primes
    p_list = [p for p in all if 1000 <= p and p <= 9999]
    return p_list


def adj_list(p_list):
    '''
    ############################ Function description ############################

    Design a function that returns an adjacency list representation of the graph
    of primes in the form of dictionary. The edges of the graph connect the prime
    numbers which have only a single different digit, such as 6329 - 6529.

    ##############################################################################
    '''
    edges = {}
    ##### Please write your code down here #####
    for i in range(len(p_list)):
        edges[p_list[i]] = []
        for j in range(len(p_list)):
            if(((int)(str(p_list[i])[0]!=str(p_list[j])[0]) + (int)(str(p_list[i])[1]!=str(p_list[j])[1]) + (int)(str(p_list[i])[2]!=str(p_list[j])[2]) + (int)(str(p_list[i])[3]!=str(p_list[j])[3]))==1):
                edges[p_list[i]].append(p_list[j])
                
    return edges


def shortest_path(a, b, p_list):
    '''
    ############################ Function description ############################

    Design a function that returns the length of the shortest path from one to an-
    other. You can use the return value of "adj_list".

    ##############################################################################
    '''
    n = 0
    ##### Please write your code down here #####
    edges = adj_list(p_list)
    pred = {}
    visited = {}
    queue = [a]

    for primes in range(len(p_list)):
        visited[p_list[primes]] = False
        
    while(len(queue)!=0 and queue[0]!=b):
        popped = queue[0]
        queue = queue[1:]
        visited[popped] = True
        for popped_adj_elements_idx in range(len(edges[popped])):
            if(visited[edges[popped][popped_adj_elements_idx]] == False):
                if edges[popped][popped_adj_elements_idx] not in queue:
                    pred[edges[popped][popped_adj_elements_idx]] = popped
                    queue.append(edges[popped][popped_adj_elements_idx])

    if(len(queue)==0): return -1 ## Cannot Find b on BFS Started at a :: ERROR HANDLING

    temp = b
    while(temp!=a):
        temp = pred[temp]
        n = n+1
    return n


if __name__ == '__main__':
    '''
    # The input will be randomly changed by TAs when grading.
    # The default strings are set as the example in the homework pdf.
    # If you execute <python3 2020-00000_assignment3-1.py>, the two prime numbers will be set by the default.
    # You can also use your own strings by executing command  <python3 2020-00000_assignment3-1.py --A 1033 --B 8179>
    # You can freely define a new function or import modules if you need.
    # You should "not" modify the "main" function
    # You are "not" allowed to use the modules that directly calculate the shortest path, such as "Dijkstar" or "NetworkX".
    '''
    prime_txt = 'prime.txt'
    prime_list = load_primes(prime_txt)
    args = parse_args(prime_list)
    A = args.A
    B = args.B
    print('Input number A : {:d}'.format(A))
    print('Input number B : {:d}'.format(B))
    N = shortest_path(A, B, prime_list)
    print('The length of the desired shortest path from A to B is : {:d}'.format(N))

