from collections import defaultdict

class Graph:
    def _init_(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
        
    def BFS(self, s):
        pass
        
    
