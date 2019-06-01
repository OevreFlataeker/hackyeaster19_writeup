from zipfile import ZipFile
from PIL import Image
import PIL.ImageOps

'''
In this challenge we have to correct a zip file, extract a file, mirror correct the file header and
manipulate the image as well

First we notice that we're apparently dealing with a zip file ("evihcra.piz" -> reverse -> "archive.zip")
So we check it in the hex editor and quickly see that the file seems to be upside down.

So we reverse the byte order and then unzip the contents

The extracted file is apparently a PNG, but the file magic bytes 0x89 0x50, 0x4e, 0x47 which identify a zip file
are also somewhat mixed up so we correct these as well

Finally we have a PNG file in front of us, but it needs a little bit more work. It again is mirrored so we unmirror it and
the colors are inverted. So we invert it again

Alternative way to flip the original file:
Copy the hex content into "cyberchef"  and use the recipe:
https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')Reverse('Character')To_Hex('Space')
'''

import io
# open file as byte stream and reverse it
with open("evihcra.piz", mode='rb') as file:
        #fileContent = file.read()
        byte_array = bytearray(file.read())
        byte_array.reverse()
        file.close()

# unzip the contents on the fly from memory stream
with ZipFile(io.BytesIO(byte_array), 'r') as zip:
    byte_array = bytearray(zip.read("90gge.gnp"))
    zip.close()

# Patch PNG file header
byte_array[1:4] = 0x50, 0x4e, 0x47

# Mirror image and invert colors
png = Image.open(io.BytesIO(byte_array))
png = PIL.ImageOps.mirror(png)
r,g,b,a = png.split()
rgb_image = Image.merge('RGB', (r,g,b))
inverted = PIL.ImageOps.invert(rgb_image)
r2,g2,b2 = inverted.split()
final = Image.merge('RGBA', (r2,g2,b2,a))
final.save("egg09.png")
final.show()

