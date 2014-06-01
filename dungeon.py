from random import *
from dungeon_room import *

def generate():
    map = []
    width = randint(32,64)
    height = randint(32,64)
    min_room_size = 6
    max_room_size = 16
    num_x_girders = randint(4,width)
    num_y_girders = randint(4, height) #divide by 4, as that is the min size of the room 
    last_room_x = 0
    last_room_y = 0
    x_girders = [0, width-1]
    y_girders = [0, height-1]

    rooms = []

    #generate the columns of the walls
    for i in range(0, num_x_girders):
        if last_room_x + min_room_size < width:
            x = randint(last_room_x + min_room_size, last_room_x + max_room_size)
            if x not in x_girders and width - x > min_room_size:
                x_girders.append(x)
                last_room_x = x

    #generate the rows of the walls
    for i in range(0, num_y_girders):
        if last_room_y + min_room_size < height:
            y = randint(last_room_y + min_room_size, last_room_y + max_room_size)
            if y not in y_girders and height - y > min_room_size:
                y_girders.append(y)
                last_room_y = y

    x_girders.sort()
    y_girders.sort()

    #calculate each of the rooms, make them an object
    for i in range(0, len(x_girders) - 1):
        room = []
        for j in range(0, len(y_girders) - 1):
            rooms.append(DungeonRoom(x_girders[i], y_girders[j], x_girders[i+1], y_girders[j+1]))

    #decide which rooms to fill in
    for i in rooms:
        if random() < .5: #arbitrary, can be changed
            i.fill = True

    #takes care of the possibility of no rooms
    allFull = True        
    for i in rooms:
        if i.fill == False:
            allFull = False

    if allFull == True:
        rooms[0].fill = False


    #generate the map
    for i in range(0,height):
        tmp_map = []
        for j in range(0,width):
            if j in x_girders or i in y_girders:
                tmp_map.append("@")
            else:
                tmp_map.append(" ")
        map.append(tmp_map)

    #fill in the rooms
    for i in range(0, height):
        for j in range(0, width):
            for k in rooms:
                if k.isIn(j, i) and k.fill == True:
                    map[i][j] = "@"

    #Paint in the corridors
    min_tree = spanning_tree(rooms)
    for edge in min_tree:
        print edge
        direction = edge.get_direction()
        if(direction == NN):
            print "!!! North !!!"
            for i in range(edge.curr.center[1], edge.next.center[1]):
                map[i][edge.curr.center[0]] = " "

        if(direction == WW):
            print "!!! East !!!"
            for i in range(edge.curr.center[0], edge.next.center[0]):
                map[edge.curr.center[1]][i] = " "

        if(direction == SS):
            print "!!! South !!!"
            for i in range(edge.curr.center[1], edge.next.center[1]):
                map[i][edge.curr.center[0]] = " "

        if(direction == EE):
            print "!!! West !!!"
            for i in range(edge.next.center[0], edge.curr.center[0]):
                map[edge.curr.center[1]][i] = " "

        if(direction == NW):
            print "!!! Northwest !!!"
            for i in range(edge.curr.center[1], edge.next.center[1] - 1):
                map[i - 1][edge.curr.center[0]] = " "
            for i in range(edge.next.center[0], edge.curr.center[0] - 1):
                map[edge.curr.center[1]][i - 1] = " "

        if(direction == NE):
            print "!!! Northeast !!!"
            for i in range(edge.curr.center[1], edge.next.center[1] - 1):
                map[i + 1][edge.curr.center[0]] = " "
            for i in range(edge.curr.center[0], edge.next.center[0] - 1):
                map[edge.curr.center[1]][i - 1] = " "

        if(direction == SW):
            print "!!! Southwest !!!"
            for i in range(edge.curr.center[1], edge.next.center[1] - 1):
                map[i - 1][edge.curr.center[0]] = " "
            for i in range(edge.next.center[0], edge.curr.center[0] - 1):
                map[edge.curr.center[1]][i + 1] = " "

        if(direction == SE):
            print "!!! Southeast !!!"
            for i in range(edge.curr.center[1], edge.next.center[1] - 1):
                map[i + 1][edge.curr.center[0]] = " "
            for i in range(edge.curr.center[0], edge.next.center[0] - 1):
                map[edge.curr.center[1]][i - 1] = " "


    print("num x girders: ", num_x_girders)
    print("num y girders: " , num_y_girders)
    print("x_girders: ", x_girders)
    print("y_girders: ", y_girders)

    for i in map:
        for j in i:
            print(j),
        print

def spanning_tree(rooms):
    spanning_tree = []
    edges = []
    placed_edges = []
    has_visited = []
    for room in rooms:
        room.has_visited = False
    start = rooms[0]
    new_edges = start.get_edges(rooms)
    start.has_visited = True
    edges = edges + new_edges
    while(len(edges) != 0):
        min_length = sys.maxsize
        min_edge = None
        min_pos = -1
        for edge in edges:
            if(edge.next.has_visited):
                edges.remove(edge)
                continue
            if(edge.get_distance() < min_length):
                min_edge = edge
                min_length = edge.get_distance()
        if(min_edge != None):
            edges.remove(min_edge)
            min_edge.next.has_visited = True
            new_edges = min_edge.next.get_edges(rooms)
            edges = edges + new_edges
            spanning_tree.append(min_edge)
    return spanning_tree

generate()
