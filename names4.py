# In this section we will be going over the "PIL" module. This module allows to perform operations 
#on image files.
# In the example below we will be creating an animated gif.
# We will also be using a ".save()" in this code, which is appended to an images location and the ".save()"
#is pass multiple parameters. ("images[0.save(......, ........., .........)]")
# To run this code we must enter the image names after .py in the terminal. 
#("python names4.py costume1.gif costume2.gif"). Then run "code costumes.gif". (We run code costumes.gif because
#that is the files images name.)
import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
        "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
    )