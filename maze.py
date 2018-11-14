from PIL import Image
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
    for x in range(15):
        print(maze_list[x])
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
    print(single_path)
    for x in range(len(path)-2,0,-1):
        #print(path[x][0],end=" ")
        #and distance of second index is one
        if single_path[-1][0] == path[x][0][0]:
            single_path.append(path[x][0])
        elif single_path[-1][1] == path[x][0][1]:
            single_path.append(path[x][0])
    return single_path

#maze_name=input("Enter the name of the maze: ")
testmaze=Image.open("testmaze1.png")
rgb=(testmaze.getpixel((1,0)))
print(rgb)
list_maze=maze_to_list(testmaze)
path=(shortest_path(list_maze))
#testmaze.show()
#path_list=list(path.keys())
#for x in range(len(path)-1,-1,-1):
    #print(path[x][0],end="")
print()
quickest_path=reconstruct_quickest_path(path)
print(quickest_path)
#print(path_list)

