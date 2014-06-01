from random import *
from dungeon_room import *
def generate():
    map = []
    width = randint(4,16)
    height = randint(4,16)
    min_room_size = 4
    max_room_size = width
    num_x_girders = randint(1,width)
    num_y_girders = randint(1, height) #divide by 4, as that is the min size of the room 
    last_room_x = 0
    last_room_y = 0
    x_girders = [0, width-1]
    y_girders = [0, height-1]

    rooms = []

    for i in range(0, num_x_girders):
        if last_room_x + min_room_size < width:
            x = randint(last_room_x + min_room_size, width)
            if x not in x_girders and width - x > min_room_size:
                x_girders.append(x)
                last_room_x = x

    for i in range(0, num_y_girders):
        if last_room_y + min_room_size < height:
            y = randint(last_room_y + min_room_size, height)
            if y not in y_girders and height - y > min_room_size:
                y_girders.append(y)
                last_room_y = y

    x_girders.sort()
    y_girders.sort()
    print(x_girders)
    print(y_girders)

    for i in range(0, len(x_girders) - 1):
        room = []
        for j in range(0, len(y_girders) - 1):
            # print "test", i, j
            print([x_girders[i],y_girders[j]])
            rooms.append(DungeonRoom(x_girders[i], y_girders[j], x_girders[i+1], y_girders[j+1]))

    for i in range(0,height):
        tmp_map = []
        for j in range(0,width):
            if j in x_girders or i in y_girders:
                tmp_map.append("@")
            else:
                tmp_map.append("#")
        map.append(tmp_map)

    # for i in map:
    #     for j in i:

    print("num x girders: ", num_x_girders)
    print("num y girders: " , num_y_girders)
    print("x_girders: ", x_girders)
    print("y_girders: ", y_girders)
    y_pos = 0
    print("", end="   ")
    for i in range(0, len(map[0])):
        print(i % 10, end=" ")
    print("", end="\n")
    print("", end="\n")

    for i in map:
        print(y_pos % 10, end="  ")
        for j in i:
            print(j, end=" ")
        print("", end="\n")
        y_pos += 1
    for room in rooms:
        print(room)
generate()
