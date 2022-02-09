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

    # Set parent of start vertex to itself
    start_vertex.parent = start_vertex

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
    if(lineOfSight(curr_vertex.parent, successor)):
        ## PATH 2
        if(curr_vertex.getParent().g + dist2(curr_vertex.getParent(), successor) < successor.g):
            successor.g = curr_vertex.getParent().g + dist2(curr_vertex.getParent(), successor)
            successor.parent = curr_vertex.parent
            if(successor in fringe):
                removeVertexFromFringe(successor)
            successor.h = h(successor, goal_vertex)
            successor.f = successor.g + successor.h
            heapq.heappush(fringe, successor)
    else:
        ## PATH 1
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

def dist2(v1: Vertex, v2: Vertex):

    # Coordinates of vertex1 depending on how many digits
    if(len(v1.getKey()) == 3):
        x0 = int(v1.getKey()[0])
        y0 = int(v1.getKey()[2])
    elif (len(v1.getKey()) == 4 and v1.getKey()[1] == '|'):
        x0 = int(v1.getKey()[0])
        y0 = int(v1.getKey()[2:4])
    elif (len(v1.getKey()) == 4 and v1.getKey()[2] == '|'):
        x0 = int(v1.getKey()[0:2])
        y0 = int(v1.getKey()[3])
    elif (len(v1.getKey()) == 5 and v1.getKey()[2] == '|'):
        x0 = int(v1.getKey()[0:2])
        y0 = int(v1.getKey()[3:5])
    elif(len(v1.getKey()) == 5 and v1.getKey()[3] == '|'):
        x0 = int(v1.getKey()[0:3])
        y0 = int(v1.getKey()[4])
    elif(len(v1.getKey()) == 6 and v1.getKey()[3] == '|'):
        x0 = int(v1.getKey()[0:3])
        y0 = int(v1.getKey()[4:6])
        
    # Coordinates of vertex2 depending on how many digits
    if(len(v2.getKey()) == 3):
        x1 = int(v2.getKey()[0])
        y1 = int(v2.getKey()[2])
    elif (len(v2.getKey()) == 4 and v2.getKey()[1] == '|'):
        x1 = int(v2.getKey()[0])
        y1 = int(v2.getKey()[2:4])
    elif (len(v2.getKey()) == 4 and v2.getKey()[2] == '|'):
        x1 = int(v2.getKey()[0:2])
        y1 = int(v2.getKey()[3])
    elif (len(v2.getKey()) == 5 and v2.getKey()[2] == '|'):
        x1 = int(v2.getKey()[0:2])
        y1 = int(v2.getKey()[3:5])
    elif(len(v2.getKey()) == 5 and v2.getKey()[3] == '|'):
        x1 = int(v2.getKey()[0:3])
        y1 = int(v2.getKey()[4])
    elif(len(v2.getKey()) == 6 and v2.getKey()[3] == '|'):
        x1 = int(v2.getKey()[0:3])
        y1 = int(v2.getKey()[4:6])

    return math.sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2))

def h(start_node: Vertex, goal_node: Vertex):
    s = start_node.getKeyCoordinates()
    g = goal_node.getKeyCoordinates()
    return math.sqrt(2) * min(abs(s[0] - g[0]), abs(s[1] - g[1])) + max(abs(s[0] - g[0]), abs(s[1] - g[1])) - min(
        abs(s[0] - g[0]), abs(s[1] - g[1]))

def lineOfSight(curr_vertex: Vertex, successor: Vertex):

    # Coordinates of curr_vertex depending on how many digits
    if(len(curr_vertex.getKey()) == 3):
        x0 = int(curr_vertex.getKey()[0])
        y0 = int(curr_vertex.getKey()[2])
    elif (len(curr_vertex.getKey()) == 4 and curr_vertex.getKey()[1] == '|'):
        x0 = int(curr_vertex.getKey()[0])
        y0 = int(curr_vertex.getKey()[2:4])
    elif (len(curr_vertex.getKey()) == 4 and curr_vertex.getKey()[2] == '|'):
        x0 = int(curr_vertex.getKey()[0:2])
        y0 = int(curr_vertex.getKey()[3])
    elif (len(curr_vertex.getKey()) == 5 and curr_vertex.getKey()[2] == '|'):
        x0 = int(curr_vertex.getKey()[0:2])
        y0 = int(curr_vertex.getKey()[3:5])
    elif(len(curr_vertex.getKey()) == 5 and curr_vertex.getKey()[3] == '|'):
        x0 = int(curr_vertex.getKey()[0:3])
        y0 = int(curr_vertex.getKey()[4])
    elif(len(curr_vertex.getKey()) == 6 and curr_vertex.getKey()[3] == '|'):
        x0 = int(curr_vertex.getKey()[0:3])
        y0 = int(curr_vertex.getKey()[4:6])

    # Coordinates of successor depending on how many digits
    if(len(successor.getKey()) == 3):
        x1 = int(successor.getKey()[0])
        y1 = int(successor.getKey()[2])
    elif (len(successor.getKey()) == 4 and successor.getKey()[1] == '|'):
        x1 = int(successor.getKey()[0])
        y1 = int(successor.getKey()[2:4])
    elif (len(successor.getKey()) == 4 and successor.getKey()[2] == '|'):
        x1 = int(successor.getKey()[0:2])
        y1 = int(successor.getKey()[3])
    elif (len(successor.getKey()) == 5 and successor.getKey()[2] == '|'):
        x1 = int(successor.getKey()[0:2])
        y1 = int(successor.getKey()[3:5])
    elif(len(successor.getKey()) == 5 and successor.getKey()[3] == '|'):
        x1 = int(successor.getKey()[0:3])
        y1 = int(successor.getKey()[4])
    elif(len(successor.getKey()) == 6 and successor.getKey()[3] == '|'):
        x1 = int(successor.getKey()[0:3])
        y1 = int(successor.getKey()[4:6])

    f = 0
    dy = y1 - y0
    dx = x1 - x0

    if(dy < 0):
        dy = -dy
        sy = -1
    else:
        sy = 1

    if(dx < 0):
        dx = -dx
        sx = -1
    else:
        sx = 1
    
    if(dx >= dy):
        while(x0 != x1):
            f = f + dy
            if(f >= dx):
                if(cellIsBlocked(x0 + ((sx-1)/2), y0 + ((sy-1)/2))):
                    return False
                y0 = y0 + sy
                f = f - dx
            if((f != 0) and cellIsBlocked(x0 + ((sx-1)/2), y0 + ((sy-1)/2))):
                return False
            if((dy == 0) and cellIsBlocked(x0 + ((sx-1)/2), y0) and cellIsBlocked(x0 + ((sx-1)/2), y0 - 1)):
                return False
            x0 = x0 + sx
    else:
        while(y0 != y1):
            f = f + dx
            if(f >= dy):
                if(cellIsBlocked(x0 + ((sx-1)/2), y0 + ((sy-1)/2))):
                    return False
                x0 = x0 + sx
                f = f - dy
            if(f != 0 and cellIsBlocked(x0 + ((sx-1)/2), y0 + ((sy-1)/2))):
                return False
            if(dx == 0 and cellIsBlocked(x0, y0 + ((sy-1)/2)) and cellIsBlocked(x0 - 1, y0 + ((sy-1)/2))):
                return False
            y0 = y0 + sy
    return True

def cellIsBlocked(x: int,y: int):
    x = math.floor(x)
    y = math.floor(y)
    x_coord = str(x)
    y_coord = str(y)
    
    line_num = 0
    if(len(x_coord) == 1 and len(y_coord) == 1):
        with open("automated_tests/test0", "r") as text_file:
            for line in text_file:
                if line_num > 2:
                    curr_line = line.strip()
                    curr_line = curr_line.replace(" ", "")
                    if(len(curr_line) == 3):
                        if(curr_line[0] ==  x_coord and curr_line[1] == y_coord and curr_line[2] == '1'):
                            return True
                        elif (curr_line[0] ==  x_coord and curr_line[1] == y_coord and curr_line[2] == '0'):
                            return False
                line_num += 1
        return False

    
    elif(len(x_coord) == 1 and len(y_coord) == 2):
        with open("automated_tests/test0", "r") as text_file:
            for line in text_file:
                if line_num > 2:
                    curr_line = line.strip()
                    curr_line = curr_line.replace(" ", "")
                    if(len(curr_line) == 4):
                        if(curr_line[0] ==  x_coord and curr_line[1:3] == y_coord and curr_line[3] == '1'):
                            return True
                        elif (curr_line[0] ==  x_coord and curr_line[1:3] == y_coord and curr_line[3] == '0'):
                            return False
                line_num += 1
        return False

    elif(len(x_coord) == 2 and len(y_coord) == 1):
        with open("automated_tests/test0", "r") as text_file:
            for line in text_file:
                if line_num > 2:
                    curr_line = line.strip()
                    curr_line = curr_line.replace(" ", "")
                    if(len(curr_line) == 4):
                        if(curr_line[0:2] ==  x_coord and curr_line[2] == y_coord and curr_line[3] == '1'):
                            return True
                        elif (curr_line[0:2] ==  x_coord and curr_line[2] == y_coord and curr_line[3] == '0'):
                            return False
                line_num += 1
        return False

    elif(len(x_coord) == 2 and len(y_coord) == 2):
        with open("automated_tests/test0", "r") as text_file:
            for line in text_file:
                if line_num > 2:
                    curr_line = line.strip()
                    curr_line = curr_line.replace(" ", "")
                    if(len(curr_line) == 5):
                        if(curr_line[0:2] ==  x_coord and curr_line[2:4] == y_coord and curr_line[3] == '1'):
                            return True
                        elif (curr_line[0:2] ==  x_coord and curr_line[2:4] == y_coord and curr_line[3] == '0'):
                            return False
                line_num += 1
        return False

if __name__ == "__main__":
    main()