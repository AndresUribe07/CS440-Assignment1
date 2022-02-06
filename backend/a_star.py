import readin
import heapq
import math
from graph import Graph
from vertex import Vertex

fringe = []
closed_list = []
start_vertex = Vertex("0|0")
goal_vertex = Vertex("0|0")

def main():

    test_graph = readin.read_in_graph("automated_tests/test0")

    ### GET START AND END VERTICES 
    line_num = 0
    exit_flag = False    
    with open("automated_tests/test0", "r") as text_file:
        for line in text_file:
            if line_num < 2:
                curr_line = line.strip()
                vertex_key = curr_line.replace(" ", "|")
                if line_num == 0:
                    # Get the start vertex
                    for v in test_graph:
                        if v.getKey() == vertex_key:
                            start_vertex = v
                elif line_num == 1:
                    # Get the goal vertex
                    for v in test_graph:
                        if v.getKey() == vertex_key:
                            goal_vertex = v
                            exit_flag = True
                            break 
                line_num += 1    
            if exit_flag == True:
                break

    # Make fringe a minheap
    heapq.heapify(fringe)

    # Add start node to the fringe
    heapq.heappush(fringe,start_vertex)

    # Loop while the fringe isn't empty
    while len(fringe) > 0:
        curr_vertex:Vertex = heapq.heappop(fringe)
        if(curr_vertex == goal_vertex):
            print('Found goal node!')
            shortest_path = []
            while(curr_vertex.getParent() is not None):
                if(curr_vertex == start_vertex):
                    break
                shortest_path.append(curr_vertex)
                curr_vertex = curr_vertex.getParent()
            shortest_path.append(start_vertex)
            print(f"Shortest path is: {shortest_path[::-1]}")
            return
        closed_list.append(curr_vertex)
        for successor in curr_vertex.getNeighbors():
            if (successor not in closed_list):
                if(successor not in fringe):
                    successor.g = math.inf
                    successor.parent = None
                updateVertex(curr_vertex, successor)
 
def updateVertex(curr_vertex: Vertex, successor: Vertex):
    if(curr_vertex.g + dist(curr_vertex,successor) < successor.g):
        successor.g = curr_vertex.g + dist(curr_vertex, successor)
        successor.parent = curr_vertex
        if(successor in fringe):
            removeVertexFromFringe(successor)
        successor.h = h(successor, goal_vertex)
        successor.f = successor.g + successor.h
        heapq.heappush(fringe,successor)
            
def removeVertexFromFringe(vertex: Vertex):
    vertex_idx = 0
    for v in fringe:
        if (v == vertex):
            break
        vertex_idx += 1 
    fringe[vertex_idx] = fringe[-1]
    heapq.heappop(fringe)
    heapq.heapify(fringe)

def dist(v1: Vertex, v2: Vertex):
    return v1.getWeight(v2)

def h(start_node: Vertex, goal_node: Vertex):
    s = start_node.getKeyCoordinates()
    g = goal_node.getKeyCoordinates()
    return math.sqrt(2) * min(abs(s[0] - g[0]), abs(s[1] - g[1])) + max(abs(s[0] - g[0]), abs(s[1] - g[1])) - min(
        abs(s[0] - g[0]), abs(s[1] - g[1]))
    
if __name__ == "__main__":
    main()