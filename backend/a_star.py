import readin
import heapq
import math
from graph import Graph
from vertex import Vertex

fringe = []
closed_list = []

def main():

    test_graph = readin.read_in_graph("backend/tests/test.txt")

    # Add neighbors for each vertex 
    for vertex in test_graph:
        print(f"vertex is: {vertex}")
        print(f"vertex key is: {vertex.getKey()}")
        print(f"vertex F-value is: {vertex.getFval()}, vertex G-value is: {vertex.getGval()}, vertex H-value is: {vertex.getHval()}")
        print(f"vertex neighbors are: {vertex.getNeighbors()}") 
        print("----------------")


    start_vertex = Vertex("0|0")
    goal_vertex = Vertex("0|0")

    ### GET START AND END VERTICES 
    line_num = 0    
    with open("backend/tests/test.txt", "r") as text_file:
        for line in text_file:
            if line_num < 2:
                curr_line = line.strip()
                vertex_key = curr_line.replace(" ", "")
                if line_num == 0:
                    start_vertex = Vertex(vertex_key)
                    # print(f"start vertex key is: {start_vertex.getKey()}")
                elif line_num == 1:
                    goal_vertex = Vertex(vertex_key)   
                line_num += 1

    number: int = 5
    
    # Make fringe a minheap
    heapq.heapify(fringe)

    # Add start node to the fringe
    heapq.heappush(fringe,start_vertex)

    # Loop while the fringe isn't empty
    while len(fringe) > 0:   ## check if it's greater or equal to zero
        curr_vertex:Vertex = heapq.heappop(fringe)
        if(curr_vertex == goal_vertex):
            print('Found goal node!')
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
            removeVertexFromFringe()
        successor.f = successor.g + successor.h
        heapq.heappush(fringe,successor)
            
def removeVertexFromFringe(vertex: Vertex):
    vertex_idx = 0
    for v in fringe:
        if (v == vertex):
            break
        vertex_idx += 1

    # Once we know the index of the vertex we want to remove,
    # we use the heap properties to remove it 
    fringe[vertex_idx] = fringe[-1]
    heapq.heappop()
    heapq.heapify(fringe)

def dist(v1: Vertex, v2: Vertex):
    return v1.getWeight(v2)

# def calculateHval():

# def calculateGvalue():
#     # 1) start at node n
#     # 2) iterate through parents adding edge costs,
#     ###  loop condition:


# def calculateFvalue():


    
if __name__ == "__main__":
    main()
