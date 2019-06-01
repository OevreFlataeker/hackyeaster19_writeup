
from PIL import Image#
import re
import requests
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}

webpage = '''

            Hey my friend, I found this one, on my journey.<br><br>

            <img alt="dontknow" src="../../static/img/ch15/challenges/752f9905-b072-4664-beb8-ddcca365e3f5.gif" height="5" width="5">

            <br>
            Do you know what to do with it?<br>
            <br>
            <form class="d-inline-block">
                <input class="form-control mb-3" type="text" name="code" placeholder="abcdefghijklmn">
                <input type="submit" class="btn btn-primary" value="submit">
            </form>

'''
def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]


regex = "/static/img/ch15/challenges/([a-f0-9]{8}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{12})"

hit = re.findall(regex, webpage)
pic = hit[0]
keks = {}
ans = requests.get("http://whale.hacking-lab.com:5447/static/img/ch15/challenges/{0}.gif".format(pic), proxies=proxies,cookies=keks,
                   allow_redirects=False)

imageObject = Image.open("rabbit.gif")
print(imageObject.is_animated)
print(imageObject.n_frames)

# Display individual frames from the loaded animated GIF file

sequence = []

for frame in range(0, imageObject.n_frames):
    imageObject.seek(frame)
    t = imageObject.convert('RGB')

    if t.getpixel((0,0))[0]==0:
        sequence.append('0')
    else:
        sequence.append('1')
morsecode = "".join(sequence)
print(morsecode)

res = split_len(morsecode,8)
chars = []
for r in res:
    chars.append(chr(int(r,2)))

print("".join(chars))



#print(mtalk.decode("".join(sequence),encoding_type='binary'))
#imageObject.show()




