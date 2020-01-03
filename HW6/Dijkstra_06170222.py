from collections import defaultdict
import heapq
import math


class Graph(object):
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]
                             for row in range(vertices)]
        self.dict = defaultdict(list)
        
    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
    
    def Dijkstra(self, s):
        s = str(s)
        graph_dict = self.get_graph_dict()
        if not graph_dict:
            return

        pri_queue = list()
        history = set()

        heapq.heappush(pri_queue, (0, s))

        combine = {s: None}
        distance = self.get_distance(graph_dict, s)

        while len(pri_queue) > 0:
            pair = heapq.heappop(pri_queue)
            span = pair[0]
            vertex = pair[1]
            history.add(vertex)

            path_list = graph_dict[vertex].keys()
            for path in path_list:
                if path not in history:
                    new_dist = span + graph_dict[vertex][path]
                    if new_dist < distance[path]:
                        heapq.heappush(pri_queue, (new_dist, path))
                        combine[path] = vertex
                        distance[path] = new_dist

        return distance

    def get_graph_dict(self) -> dict:
        if len(self.graph) == 0:
            return

        result = {}
        for point in range(len(self.graph)):
            path_list = self.graph[point]

            data = {}
            for other, span in enumerate(path_list):
                if other == point or span == 0:
                    continue
                data[str(other)] = span

            result[str(point)] = data

        return result

    def get_distance(self, graph_dict: dict, s: str):
        result = {s: 0}
        for vertex in graph_dict.keys():
            if vertex != s:
                result[vertex] = math.inf
        return result
    
    def Kruskal(self):
        answer={}
        check = [column for column in range(self.V)]  
        val = sorted(self.dict)
        for i in val:
            for f,s in self.dict[i]:
                if check[f] == check[s]:
                    pass
                else:
                    check = [check[f] if x==check[s] else x for x in check]
                    answer[str(f)+'-'+str(s)] = i
        return answer
