from PIL import Image

def shortpathmaze(maze):
    largerimage=maze.resize((1500,1500))
    largerimage.show()
    height=maze.height
    width=maze.width
    print(height,width)
    for x in height:
        print(x)

maze_name=input("Enter the name of the maze: ")
testmaze=Image.open(maze_name)
rgb=(testmaze.getpixel((1,0)))
print(rgb)
shortpathmaze(testmaze)
#testmaze.show()
