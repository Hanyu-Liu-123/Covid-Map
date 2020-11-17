from heapq import *

"""
This file should be used for creating the graph class for COVID-MAP database.

Either implement the graph class by adjaceny list or matrix.
"""


class graph:

    def __init__(self):
        self.adjacency_list = {}
        self.weights_list = {}

    def add_node(self, node):
        if node in self.adjacency_list:
            raise ValueError("This node is already in the list!")
        self.adjacency_list[node] = set()
        self.weights_list[node] = {}

    def add_edge(self, node1, node2, weight1, weight2=None):
        if weight2 is None:
            weight2 = weight1
        self.adjacency_list[node1].add(node2)
        self.adjacency_list[node2].add(node1)
        self.weights_list[node1][node2] = weight1
        self.weights_list[node2][node1] = weight2

    def get_nodes(self):
        return self.adjacency_list.keys()

    def is_edge(self, node1, node2):
        if node1 in self.adjacency_list[node2] and node2 in self.adjacency_list[node1]:
            return True, self.weights_list[node1][node2]
        return False, None

    def get_neighbors(self, node):
        return self.weights_list[node].items()

    def __str__(self):
        rep = ""
        for node in self.adjacency_list:
            rep += str(node) + ": ["
            for next in self.adjacency_list[node]:
                rep += '(' + next + ',' + str(self.weights_list[node][next]) + ')'
                rep += ','
            rep.strip(',')
            rep += ']\n'
        return rep.strip()

    def dijkstra(self, start, end):

        heap = []
        heappush(heap, (0, start))
        visited = {start}
        priority = {start: 0}
        parent = {start: start}

        while len(heap) > 0:
            distance, current = heappop(heap)

            if current == end:
                print(parent)
                print(distance)
                return get_path(parent, start, end)

            for next, weight in self.get_neighbors(current):
                next_priority = distance + weight

                if next not in visited:
                    heappush(heap, (next_priority, next))
                    visited.add(next)
                    priority[next] = next_priority
                    parent[next] = current

                elif next_priority < priority[next]:
                    heap.remove((priority[next], next))
                    heappush(heap, (next_priority, next))
                    priority[next] = next_priority
                    parent[next] = current


def get_path(dictionary, source_node, end_node):
    if dictionary[end_node] == source_node:
        return [source_node, end_node]
    else:
        new_key = dictionary[end_node]
        return get_path(dictionary, source_node, new_key) + [end_node]


def test():
    testGraph = graph()

    testGraph.add_node("Albermale County, Virginia")
    testGraph.add_node("Warren County, Virginia")
    testGraph.add_node("Orange County, California")
    testGraph.add_node("Area 51")

    testGraph.add_edge("Albermale County, Virginia", "Warren County, Virginia", 5, 5)
    testGraph.add_edge("Albermale County, Virginia", "Orange County, California", 50, 50)
    testGraph.add_edge("Orange County, California", "Warren County, Virginia", 35, 35)
    testGraph.add_edge("Warren County, Virginia", "Area 51", 2, 2)
    testGraph.add_edge("Area 51", "Orange County, California", 2, 2)

    print(testGraph.dijkstra("Albermale County, Virginia", "Orange County, California"))

#test()
