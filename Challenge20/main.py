from PIL import Image

#
# The image is 259x256 not 256x256 as usual.
# Carefully looking at a single row and printing every pixel value, one can find that all pixels have alpha of 255 but 3 single pixels
# For these pixels 2 of 3 RGB channel compontents are 0 as well! The third one carries a number identical for all "magic pixels" in that row
# First thing is we reorder the lines according to that row number. For example line 84 of the original image carries the 3rd value 0 so this will be the first line in the
# transposed image.
# Then we split the new image into RGB and only work on the G part (as G holds the most details)
# Looking at only the single channel we see that the lines are shifted horizontally.
# As it turns out, the magic pixel for Green (the 1 in the middle of the pixel tuple (x,1,y,0) can be used as a marker.
# All the pixels should be aligned to column 255. Calculating each delta in each row gives us the number of pixels to shift the pixels in that row to align them
# Doing this for every row gives us a unsharp but nevertheless scannable egg20


'''
im = Image.open("egg.png")
pixel_values = list(im.getdata())
new_bitmap = []
width, height = im.size
lst = []
copied = False
for cnt in range(0,256):

    for y in range(height):
        if copied:
            break
        for x in range(width):
            if copied:
                break
            val = pixel_values[width*y+x]
            if val[3]==0: # Do we have a special pixel?
                special = val
                if special[0]!=0 and special[0]==cnt:
                    for c in range(259):
                        pix_of_col = pixel_values[y * 259 + c]
                        new_bitmap.append(pix_of_col)
                        copied = True
                elif special[1]!=0  and special[1]==cnt:
                    for c in range(259):
                        pix_of_col = pixel_values[y * 259 + c]
                        new_bitmap.append(pix_of_col)
                        copied = True

                elif special[2]!=0 and special[2]==cnt:
                    for c in range(259):
                        pix_of_col = pixel_values[y * 259 + c]
                        new_bitmap.append(pix_of_col)
                        copied = True
                elif special[0]==0 and special[1]==0 and special[2]==0 and cnt==0:
                    for c in range(259):
                        pix_of_col = pixel_values[y * 259 + c]
                        new_bitmap.append(pix_of_col)
                        copied = True
    copied = False


print("Finished creating new bitmap fo size 256x256")
im.putdata(new_bitmap)
im.save("new.png")
exit(1)
#assert(len(new_bitmap)==259*256)
'''
'''
im = Image.open("green.png")
pixel_values = list(im.getdata())

width, height = im.size

new_bitmap = []

saverow=0
for row in range(256):
    # Matrix should be at pixel 257
    # Find the location of our pixel
    fixpoint = None
    temp_row = [(0, 0, 0, 0) for x in range(width)]
    transposed_row = [(0, 0, 0, 0) for x in range(width)]

    for col in range(259):
        temp_row[col] = pixel_values[259 * row + col]
        val = pixel_values[259 * row + col]
        if (val[0]==0 and val[1]==row and val[2]==0 and val[3]==0 and fixpoint is None): # It is this one
            # at col is our pixel
            fixpoint=col
            print("Row {0}, fixpoint at: {1}".format(row, fixpoint))
            saverow=row


    if fixpoint is None:
        print("Haven't found fixpoint in row " + str(row))
        fixpoint = row


    delta = 255-fixpoint
    print("Delta: ", delta)
    # Now shift every pixel
    for col in range(259):
        transposed_row[(col+delta)%259]=temp_row[col]
    new_bitmap.append(transposed_row)

# Save what we've got
new_im=[]
for row in range(saverow):
    for col in range(259):
        new_im.append(new_bitmap[row][col])
im.putdata(new_im)
im.save("shifted_green.png")

'''

###

im = Image.open("blue.png")
pixel_values = list(im.getdata())

width, height = im.size

new_bitmap = []

saverow=0
for row in range(256):
    # Matrix should be at pixel 257
    # Find the location of our pixel
    fixpoint = None
    temp_row = [(0, 0, 0, 0) for x in range(width)]
    transposed_row = [(0, 0, 0, 0) for x in range(width)]

    for col in range(259):
        temp_row[col] = pixel_values[259 * row + col]
        val = pixel_values[259 * row + col]
        if (val[0]==0 and val[1]==0 and val[2]==row and val[3]==0 and fixpoint is None): # It is this one
            # at col is our pixel
            fixpoint=col
            print("Row {0}, fixpoint at: {1}".format(row, fixpoint))
            saverow=row


    if fixpoint is None:
        print("Haven't found fixpoint in row " + str(row))
        fixpoint = row


    delta = 258-fixpoint
    print("Delta: ", delta)
    # Now shift every pixel
    for col in range(259):
        transposed_row[(col+delta)%259]=temp_row[col]
    transposed_row.remove((0,0,row,0))
    transposed_row.remove((0,0,0,0))
    transposed_row.remove((0, 0, 0, 0))
    new_bitmap.append(transposed_row)

# Save what we've got
new_im=[]
for row in range(saverow):
    for col in range(256):
        new_im.append(new_bitmap[row][col])
im.putdata(new_im)
im.save("shifted_blue.png")

'''


im = Image.open("red.png")
pixel_values = list(im.getdata())

width, height = im.size

new_bitmap = []

saverow=0
for row in range(256):
    # Matrix should be at pixel 257
    # Find the location of our pixel
    fixpoint = None
    temp_row = [(0, 0, 0, 0) for x in range(width)]
    transposed_row = [(0, 0, 0, 0) for x in range(width)]

    for col in range(259):
        temp_row[col] = pixel_values[259 * row + col]
        val = pixel_values[259 * row + col]
        if (val[0]==row and val[1]==0 and val[2]==0 and val[3]==0 and fixpoint is None): # It is this one
            # at col is our pixel
            fixpoint=col
            print("Row {0}, fixpoint at: {1}".format(row, fixpoint))
            saverow=row


    if fixpoint is None:
        print("Haven't found fixpoint in row " + str(row))
        fixpoint = row


    delta = 256-fixpoint
    print("Delta: ", delta)
    # Now shift every pixel
    for col in range(259):
        transposed_row[(col+delta)%259]=temp_row[col]
    new_bitmap.append(transposed_row)

# Save what we've got
new_im=[]
for row in range(saverow):
    for col in range(259):
        new_im.append(new_bitmap[row][col])
im.putdata(new_im)
im.save("shifted_red.png")
'''