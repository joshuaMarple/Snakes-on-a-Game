from random import *

def generate():
    map = []
    width = randint(4,64)
    height = randint(4,64)
#    width = 16
#    height = 16
    min_room_size = 3
    max_room_size = width
    num_x_girders = randint(1,width/4) 
    num_y_girders = randint(1, height/4) #divide by 4, as that is the min size of the room 
    last_room_x = 0
    last_room_y = 0
    x_girders = [0, width-1]
    y_girders = [0, height-1]
    for i in range(0, num_x_girders):
        x = randint(last_room_x, width)
        if x not in x_girders:
            x_girders.append(x)
    for i in range(0, num_y_girders):
        y = randint(last_room_y, height)
        if y not in y_girders:
            y_girders.append(y)
    for i in range(0,height):
        tmp_map = []
        for j in range(0,width):
            if j in x_girders or i in y_girders:
          #      for q in y_girders:
                tmp_map.append("@")
                    #elif i == q:
                    #    tmp_map.append("$")
            else:
                tmp_map.append("#")
        map.append(tmp_map)
    print "num x girders: ", num_x_girders
    print " num y girders: " , num_y_girders
    print "x_girders: ", x_girders
    print " y_girders: ", y_girders
    for i in map:
        for j in i:
            print(j),
        print
generate()
