
'''
Dijkstra's Algorithm
Useful for finding shortest path between two nodes in a directed graph

Last Updated: 2016-May-24
First Created: 2016-May-23

Python 2.7
Chris
'''

def test_undirected_weighted_graph(graph):
    '''
    Test undirected graph has no accidental one-way edges,
    and that the graph weights also match.
    '''
    for idx, item in enumerate(graph):
        for connected_node in item.iterkeys():
            if idx not in graph[connected_node].iterkeys() or graph[connected_node][idx] != item[connected_node]:
                print 'error with nodes', idx, connected_node

    print 'Test completed'

def dijkstra(graph, source, destination):
    '''
    Dijkstra's Algorithm
    Useful for finding shortest path between two nodes in a weighted graph.
    Takes a weighted graph and source node and returns shortest route and distance.
    '''

    node_bfs = [[float('inf'), None] for _ in range(len(graph))] # for each node, set default distance and parent
    node_bfs[source][0] = 0

    queue = [x for x in range(len(graph))] # enqueue every node

    while queue:
        min_distance = float('inf')
        # find the node in queue with shortest distance
        for idx in queue:
            if node_bfs[idx][0] < min_distance:
                min_distance = node_bfs[idx][0]
                min_distance_node = idx

        queue.pop(queue.index(min_distance_node))

        for nebor in graph[min_distance_node]:
            if nebor in queue:
                # alt checks whether this path to nebor node is shorter than current shortest stored.
                alt = min_distance + graph[min_distance_node][nebor]
                if alt < node_bfs[nebor][0]:
                    node_bfs[nebor][0] = alt
                    node_bfs[nebor][1] = min_distance_node

    print node_bfs, '\n'
    return get_distance_and_path(node_bfs, destination)


def get_distance_and_path(results, destination):
    '''
    Takes a list of lists of dijkstra results (in the form [distance, parent]) and a destination.
    Returns shortest distance and path from source (used to generate results)
    '''
    distance, parent = results[destination]
    path = [destination]
    path_distance = [results[destination][0]]

    while parent != None:
        path.insert(0, parent)
        path_distance.insert(0, results[parent][0])
        parent = results[parent][1]

    return distance, path, path_distance

def print_results(distance, path, path_distance, example_names):
    '''
    Prints results from running the algorithm.
    '''
    print 'The shortest distance is %d , and the path is: ' %(distance)
    for idx, node in enumerate(path):
        print idx, example_names[node], path_distance[idx]

def testing():
    '''
    Quick tests.
    '''
    test_graph = [{1: 10, 4: 900}, {0: 10, 2: 20}, {1: 20, 3: 30}, {2: 30, 4: 40}, {0: 900, 3: 40}]
    test_graph2 = [{1: 100, 4: 90}, {0: 100, 2: 20}, {1: 20, 3: 30}, {2: 30, 4: 40}, {0: 90, 3: 40}]

def run():
    '''
    Run example - distancegraph.png.
    '''

    example_names = ['Champlain', 'Albany', 'Newburgh', 'New York', 'Highgate Springs',\
    'Derby Line', 'St. Johnsbury', 'White River Jct.', 'Springfield', 'Hartford',\
    'New Haven', 'Concord', 'Sturbridge', 'Providence', 'Reading', 'Weston', 'Canton', 'Boston']

    # weighted adjacency list - see distancegraph.png
    example_graph = [{1: 178}, {0: 178, 2: 90, 8: 87}, {1: 90, 3: 69, 9: 97}, {2: 69, 10: 81}, {7: 130},\
    {6: 50}, {5: 50, 7: 60, 11: 105}, {4: 130, 6: 60, 8: 122, 11: 64}, {1: 87, 7: 122, 9: 27, 12: 36},\
    {2: 97, 8: 27, 10: 39, 12: 43}, {3: 81, 9: 39, 13: 102}, {6: 105, 7: 64, 14: 56},\
    {8: 36, 9: 43, 15: 51}, {10: 102, 16: 32}, {11: 56, 15: 19, 17: 15},\
    {12: 51, 14: 19, 16: 21, 17: 17}, {13: 32, 15: 21, 17: 20}, {14: 15, 15: 17, 16: 20}]

    source = 'New York'
    destination = 'Boston'

    source_idx = example_names.index(source)
    destination_idx = example_names.index(destination)

    #test_undirected_weighted_graph(example_graph)

    distance, path, path_distance = dijkstra(example_graph, source_idx, destination_idx)

    print_results(distance, path, path_distance, example_names)

def run2():
    '''
    Another example - http://rosettacode.org/wiki/Dijkstra's_algorithm. And rcode.png.
    '''

    example_names = ['a', 'b', 'c', 'd', 'e', 'f']
    example_graph = [{1: 7, 2: 9, 5: 14}, {2: 10, 3: 15}, {3: 11, 5: 2}, {4: 6}, {5: 9}]

    source = 'a'
    destination = 'e'

    source_idx = example_names.index(source)
    destination_idx = example_names.index(destination)

    distance, path, path_distance = dijkstra(example_graph, source_idx, destination_idx)

    print_results(distance, path, path_distance, example_names)
