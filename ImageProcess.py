'''
Author: Matteo Tempo
Date: April 16th, 2019
'''

from Mapping import Mapping
from PIL import Image
from PIL import ImageDraw

map_obj = Mapping()
map_obj.create_map(3)
map_obj.set_element(-2, -2, 'r')
map_obj.set_element(2, 2, 'r')
map_obj.set_element(-2, 2, 'r')
map_obj.set_element(9, -2, 'g')

for i in range(len(map_obj.grid)):
    print(map_obj.grid[i])

x = len(map_obj.grid[0])
y = len(map_obj.grid)

img = Image.new('RGB', (x*50, y*50), color=(255, 255, 255))
draw = ImageDraw.Draw(img)

fillColour = ""
for row in range(x):
    for col in range(y):
        print(col, row)
        if map_obj.grid[col][row] == "R":
            fillColour = "black"
        elif map_obj.grid[col][row] == "r":
            fillColour = "red"
        elif map_obj.grid[col][row] == "g":
            fillColour = "green"
        else:
            fillColour = "white"
        draw.rectangle([(row * 50, col * 50), (row * 50 + 49, col * 50 + 49)], fill=fillColour, outline="black")

img.save("rectangle.png")