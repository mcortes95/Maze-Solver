from PIL import Image, ImageDraw
from collections import deque

def maze_to_list(maze):
    height=maze.height
    width=maze.width
    black=(0, 0, 0, 255)
    white=(255, 255, 255, 255)
    #print(height,width)
    largerimage=maze.resize((width*50,height*50))
    largerimage.show()
    maze_list=[]
    for y in range(height):
        maze_width=[]
        for x in range(width):  
            #print(maze.getpixel((x,y)))
            if maze.getpixel((x,y)) == black:
                maze_width.append(1)
            elif maze.getpixel((x,y)) == white:
                maze_width.append(0)
        maze_list.append(maze_width)
    #for x in range(15):
    #    print(maze_list[x])
    return maze_list

def shortest_path(list_maze):
    start_node=[1,0]
    frontier=deque()
    frontier.append(start_node)
    dist={str(start_node):1}
    dist_list=[[start_node,1]]

    while frontier:
        node=frontier.popleft()
        if node ==[len(list_maze)-2,len(list_maze[0])-1]:
            return dist_list
        neighbors=find_neighbors(list_maze,node)
        for x in neighbors:
            if str(x) not in dist.keys():
                dist[str(x)]=dist[str(node)]+1
                frontier.append(x)
                dist_list.append([x,dist[str(node)]+1])



def find_neighbors(maze,node):
    neighbors=[]
    if node[0]>0:
        if maze[node[0]-1][node[1]]==0:
            neighbors.append([node[0]-1,node[1]])
    if node[0]<len(maze)-1:
        if maze[node[0]+1][node[1]]==0:
            neighbors.append([node[0]+1,node[1]])
    if node[1]>0:
        if maze[node[0]][node[1]-1]==0:
            neighbors.append([node[0],node[1]-1])
    if node[1]<len(maze[0])-1:
        if maze[node[0]][node[1]+1]==0:
            neighbors.append([node[0],node[1]+1])
    return neighbors

def reconstruct_quickest_path(path):
    single_path=[path[-1][0]]
    #print(single_path)
    for x in range(len(path)-2,0,-1):
        #print(path[x][0],end=" ")
        #and distance of second index is one
        if single_path[-1][0] == path[x][0][0]:
            if single_path[-1][1]-path[x][0][1] is 1 or single_path[-1][1]-path[x][0][1] is -1:
                single_path.append(path[x][0])
        elif single_path[-1][1] == path[x][0][1]:
            if single_path[-1][0]-path[x][0][0] is 1 or single_path[-1][0]-path[x][0][0] is -1:
                single_path.append(path[x][0])
    single_path.append(path[0][0])
    return single_path

def draw_path(maze_image, path):
    path_drawing=ImageDraw.Draw(maze_image)
    for x in path:
        print(x)
        path_drawing.point([ x[1],x[0] ],(233,0,0,200))
    height=maze_image.height
    width=maze_image.width
    largerimage=maze_image.resize((width*50,height*50))
    largerimage.show()

#maze_name=input("Enter the name of the maze: ")
testmaze=Image.open("testmaze1.png")
rgb=(testmaze.getpixel((1,0)))
list_maze=maze_to_list(testmaze)
path=(shortest_path(list_maze))
print()
quickest_path=reconstruct_quickest_path(path)
#print(quickest_path)
draw_path(testmaze,quickest_path)
