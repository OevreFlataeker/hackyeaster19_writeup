import av
from PIL import Image

filename = 'he2019_teaser.mp4'
container = av.open  (filename)
img = Image.new  ('RGB',(480,480), "black")
pixels = img.load()
row = 0
col = 0
for packet in container.demux():
        for frame in packet.decode():
#               if frame.type == 'video':
                i = frame.to_image()
                px = i.load()[0,0]
                pixels[col,row] = (px[0],px[1],px[2])
                col+=1
                if col==480:
                        col=0
                        row+=1
img.save  ("output.png");
