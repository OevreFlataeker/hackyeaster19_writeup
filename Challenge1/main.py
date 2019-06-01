from skimage import io
from skimage.transform import swirl

image = io.imread("twisted.png")

swirled = swirl(image, rotation=0, strength=3, radius = 430)

io.imsave("untwisted.png", swirled)

#
# Image can be unswirled using
# https://www142.lunapic.com/editor/ -> Swirl, Swirl Amount 115