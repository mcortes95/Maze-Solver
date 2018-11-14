from PIL import Image

def shortpathmaze(maze):
    largerimage=maze.resize((1500,1500))
    largerimage.show()


testmaze=Image.open('maze0.png')
rgb=(testmaze.getpixel((1,0)))
print(rgb)
shortpathmaze(testmaze)
#testmaze.show()
