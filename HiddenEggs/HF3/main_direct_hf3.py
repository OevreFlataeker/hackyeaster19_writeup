#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import cStringIO
import requests
import json
from hashlib import sha512
from itsdangerous import URLSafeTimedSerializer, BadTimeSignature
import base64
import zlib
from cuteprint import PrettyPrinter
from os import system, name
from flask.sessions import session_json_serializer
import re
import urllib
from kanren import *
import random
from PIL import Image
from kanren.core import lall
# def goToUserInput():
#    r.sendline("exit")
#    r.recvuntil(">")
#    r.sendline("1")
#    return r.recvuntil(">")
SLEEPVAL = 0.2
SOUTH = "/0/1"
NORTH = "/0/-1"
EAST = "/1/0"
WEST = "/-1/0"
ans = ""
keks = None
maze = []
checked = None
pois = {}
fibs = {}
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}

#proxies = {
#    'http': 'http://194.145.60.1:9400',
#    'https': 'http://194.145.60.1:9400',
#}

def decode(direc):
    if direc == NORTH:
        return "NORTH"
    elif direc == SOUTH:
        return "SOUTH"
    elif direc == EAST:
        return "EAST"
    else:
        return "WEST"

def solveTimeTravel():
    # Cookie:
    # z.WcGZyPYQuxq2BJ9YlLZD4283qUmytszr0m4UhpBgOSEXBaJy61axripimxjjDkEAGArfztM3qegF7pipXZcM+Y3MWvMWBDKs4wTfSQZB2omL0+wp1PcYojm9VcAlLMrSHhZqg1rW5eN4TWX7h6qo3eIY9b1zyu7tyTGpwcipLpaEckduUOHDKA1rmJyi0Z8TLzeSMqz5r8O8or3ta5OzJcBoPoVZHryoPI32vlE/9r0SlCalKZAJ5F91O7Y/qN9UqjDvURLxwZbTPhqhzUEHPISCVGF1hOkNfoGiBVdyiHk=.EubK5n4sXP26UkioHvd6vQ==.icaoNuuOD0EA63GlXlvCPg==
    '''
    <div>
            Hey my friend, nice to meet you.<br>
            Can you help ma calculate a thing? <br>
            I'm able to teleport through times, but I get lost sometimes.<br>
            <br>
            One trip I plan will be today at 15:56 to Ljubljana. Do you know what time it is
            there?<br>
            Ah and my clock shows 08:25 at the moment.
            <hr>
            <form method="get">
                <div class="form-group row">
                    <label class="col-form-label col-md-2  offset-3">Time</label>
                    <input type="text" class="form-control col-md-2" name="time" placeholder="14:19">
                </div>
                <div class="form-group">
                    <input type="Submit" class="btn btn-primary" value="I know it!">
                </div>
            </form>
        </div>

    '''
    global ans
    global keks
    if "" in ans.content:
        pass
    pass

def solveMathonymous():
    # Cookie:
    # z.TvBs8IBOw/C6Drxj4MQFLgst3bPNuhq/YtQPLmq8BVMV4A0xiQNjXl0KYL2qdFi36B/Lm7s+ZKu2kGuZayPpP7V9KevD6Y0qiB3984IVQH8ZB0jd3TNyInZe30zT84hk2S/ZeFMkhjBPuPe0YnIeuvSO/VU9tYenOBZSmhWmXbOG8bMJSS7IekEfr+WfK1f3lf8aTkuAnmlkuoSNc1oZ1+bjlA0SVyJ8Od+N+QmRnwvq/oN5Ru4UmzUs5c1CIEawhUuBW3e5S01hbuKL8g+jwmXE2n5VwO3/6oP5+7FdjEuvC7juBOtBPITOdGCT5uOD9IoKqpdjkmP8A8XgKL0H6og++AtR9wCw+9ORpD2FkWXWEtImmuslb4vto6IOu3ZAfbX0QbpbKxHFt4ItkTDr/Led7ymy3Fxy2tQbS8Dake2vUXA8xv8ScBzNnUiHu1dTQ3lbirtOiIZa5ZQQre/TTBeVtRwL9hF54Ix1Li4abxLUGWjV+ttnY2mC7Ft7XHBXy/zn+0bG79/wfOcbRxYdTDoj01XF6P8+la8PFDwMqEQfjRsqJD6z8Uj48bv8dDOpNU2RZjIDrxshRPc2Ksm9Rfx/8WGJuocGfayuhDPj/+Nw2itCe8pGQgbsz+vaAYdngkUKgxcFyJ+uhaSZ+mkC4yJ8paatW2d9y20VqXYiYA33II0WoWjAcH3QEEpQgehGTxyzvIC3/tR9ESIlBJ7s/jX2cB9CQ5IsD8dC9Egh+TgXCqV9zTk0tHRTGxREZ6LiPLCPcJFHhMjPNEhW6K+ydl1lt4iOITLWexF/pbnU8f/xgpQuSiFydc7gWcv2firo5ppD9xeqhwTIN33Hlr+Pd0weGpHsLNEumEgAsc1kgEDLN7F8yCL+rmvDiDmGOcXQd1e+U1XvAF43ZFzpLGtqzLZCesflzpc77oj/d03PkMAb8CxfvP5hllKww5RhhkXBXiPqV4dNlxUfIico/UY+BI243j4MDFCbaPzyv1wPJjdrQJMBlVGuGlQknJNAMfKp6qagjkqFg8LfblTyRZOi940tPak8JQ9VKeNM6YMFSibfB7SDazm0KAtHXFcSX7cm3Ce/Jfij3maPt/jiccIHEp8OvzUCAn7/z9CIpk7rfsWxetyauIt0AzTS7FsEGaLSJLaCgiCYl7LeVt8JCjvOVVaYFsd7NcQW54OYGboiVx5TncGgbXhfkCHhyFyOmfMQSyVzVoXGe85rmmIQ/U4z5x/eS46+oJacoCrnFkj/PhZ26+Xa+Qu/LBmL6bdTEuiPxi2g6iIx9TAS+RvBRkVCcCcGmfSu4Hg5/jNXLK+6414Bld7v7g==.cG+CtTWuXop+V1KHsC1n8w==.Qhh9yYUSGW8L3F6zDGmWzQ==

    '''
    <div>

            Hmmmm.... <br>one in mind .... <br>plus ... <br>minus .... <br>WAAAAAH.<br>
            Oh hey you came just right. Could you solve this until I search for my calculator?
            <br>
            Who I am you ask? I think that would be a bit embarrassing because I can not solve this simple
            equation.
            <hr>

            <form method="get">
                <table>
                    <tr>
                        <th></th>
                        <th style="padding-left: 20px">Solution</th>
                    </tr>
                    <tr>
                        <td><code style="font-size: 1em">80+54+51-61 = </code></td>
                        <td width="200px" style="padding-left: 20px"><input type="number" class="form-control"
                                                                            name="result" placeholder="1337"></td>
                    </tr>
                </table>
                <hr>
                <div class="form-group">
                    <input type="submit" class="btn btn-primary" value="I got it!">
                </div>
            </form>
        </div>
    :return:
    '''
    global ans
    global keks
    regex = '<td><code style="font-size: 1em">(.*)= </code></td>'
    hit = re.findall(regex, ans.content)
    equation = hit[0]
    sol = eval(equation)
    ans = requests.get(
        "http://whale.hacking-lab.com:5337/?result={0}".format(sol),
        proxies=proxies, cookies=keks,
        allow_redirects=False)
    keks = ans.cookies
    if "solved" in ans.content:
        print("Solved!")
        return
    else:
        print("Failed.")
        exit(1)
    pass

'''
Checks which directions are possible to walk from the current position
Caches the found information.
Clumsy implementation but it works
'''


def checkDir(r, maze, posy, posx):
    global ans
    global keks
    global proxies
    if checked[posy][posx] == 1:
        return ""
    possible = {}
    got302 = False
    l = None
    # print("I am at ", posy, posx)
    for d in [WEST, NORTH, EAST, SOUTH]:
        # print("trying ", decode(d))
        # Send step
        # r.sendline("go {0}".format(d))
        # r.sendline("go {0}".format(d))
        ans = requests.get("{0}/move{1}".format(URL, d), cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        response = ans.content
        if ans.status_code == 302:
            print("Got 302!")
            got302 = True
            l = ans.headers['Location']
        if ans.status_code == 500:
            print("Uh oh we got a 500! This seems to be a bug in the game! :-(")
            waitKey()
            exit()
        # If ansower has not alert
        possible[d] = (not "alert" in response)
        # Undo move
        # When we were able to walk one step in a certain direction
        # i.e. no "You hit a wall" message, we'll have to UNDO the step again
        # to end up on the same position where we checked the possibilities from

        # We need to check what to do here... we probably have to play the game

        if got302:
            # Solve the 302

            ans = requests.get(l, cookies=keks, proxies=proxies, allow_redirects=False)

            keks = ans.cookies


            got302 = False
        if not "alert" in response or "alert-success" in response:
            # print("Stepped ok, undoing")
            if d == NORTH:

                ans = requests.get("{0}/move{1}".format(URL, SOUTH), cookies=keks, proxies=proxies,
                                   allow_redirects=False)
                keks = ans.cookies
                # go SOUTH

            elif d == SOUTH:
                # go NORTH
                ans = requests.get("{0}/move{1}".format(URL, NORTH), cookies=keks, proxies=proxies,
                                   allow_redirects=False)
                keks = ans.cookies

            elif d == EAST:
                # go WEST
                ans = requests.get("{0}/move{1}".format(URL, WEST), cookies=keks, proxies=proxies,
                                   allow_redirects=False)
                keks = ans.cookies

            else:
                # go EAST
                ans = requests.get("{0}/move{1}".format(URL, EAST), cookies=keks, proxies=proxies,
                                   allow_redirects=False)
                keks = ans.cookies

    # Updates the in-memory copy of the maze with the
    # information which steps are possible (0 = there is a path in that direction)
    # If we have already seen that particular place before (value == 3), we do not
    # overwrite the value

    # print("Setting values, relative to ",posy,posx)
    if possible[NORTH]:
        # print("Opened north")
        if maze[posy - 1][posx] != 3:
            maze[posy - 1][posx] = 0
    if possible[EAST]:
        # print("Opened east")
        if maze[posy][posx + 1] != 3:
            maze[posy][posx + 1] = 0
    if possible[SOUTH]:
        # print("Opened south")
        if maze[posy + 1][posx] != 3:
            maze[posy + 1][posx] = 0
    if possible[WEST]:
        # print("Opened west")
        if maze[posy][posx - 1] != 3:
            maze[posy][posx - 1] = 0
    #       print(possible)
    # Mark the current square as resolved
    checked[posy][posx] = 1
    return ans

def solveRandonacci():
    # THIS ONE NEEDS PYTHON3!!! PYTHON2 PRNG DIFFERS!

    # Cookie:
    # z.uQzUMVEpePwqj3cuSQbwD5VUHjvkBTM57B+5HiGRs4yLe+udA7/1mBd7u52tYwI/AbqoTEnOgtUbPmYihh0Zsv5+arogP781GcvnNipz7LKvFvCzkOEdu4EWSAdqEqYVUwmxUOip2MJ4/M+w4FXwRGgD9MtAkC3wYXTzU/eyO668cY8xD+Ld9up7Hull1pYqGLEVu/d/dg2i8hx3MQS1to9E62A/4L8D/fKeiPl/QCDrLQgCXuf3MBljFUOCaYUigOsJ2+iyhj0/O4xcvt5AbfviLgUgH8XuqyoKkL68YmIlXZxyn64V8tQTwj2pdOqyJ7vr31FPBQEKFsD/7cabzRduSMupqrn18yXEVz9cg2WH4LkAcWjCzJ0Ri02gWTgpAQWKVMsxm/qFvboYfLUexkPmcQfMZ/0weGChm4dtKub95O6u4t/XWwUWG9JYRquULrXtoIm+6X5vZTkE.YqozklwbuI7pJfyKmRP1oQ==.zKqUhHe3/13LHTbUpGNTpw==
    '''
    <div>

            What a beautiful chain, <br>but the last piece is missing. <br><br>
            Do you know what we need?
            <br>
            <b>HINT</b>
            <p>
                random.seed(1337)
                <br>
                sequence.append(1 % random.randint(1, 1))
                <br>
                sequence.append(1 % random.randint(1, 1))
                <br>
                sequence.append(2 % random.randint(1, 2))
                <br>
                Greetz, Leonardo F.
            </p>
            <hr>
            The chain has a row of elements with following numbers printed on:<br>
            <code>
                [0, 0, 0, 1, 2, 3, 6, 0, 10, 6, 34, 41, 2, 3, 92, 271, 228, 1158, 874, 155, 760, 161, 1377, 76, 12877, 561, 2654, 48507, 97042, 174104, 78347, 260851, 993674, 1259337, 2483645, 5740505, 1575587, 3826257, 21727529, 24850563, 673343, 15828943, 214735647, 338253, 94471517, 385474364, 26496473, 2080231810, 162912664, 348797635, 117488414, 10524736889, 12805435028, 19348307706, 8178002329, 25897469511, 24880839358, 187779182313, 378924045099, 330018976494, 57572802365, 1755769600244, 1787962449615, 1399589890939, 4699103264099, 5537088097592, 799491845133, 10875107129731, 41609657911621, 47938445436267, 6044678688289, 76354192309034, 20146302444405, 50538003336545, 169286736998843, 140463926976638, 1372753687833637, 2090937796081262, 3208841539011769, 223403826756170, 18890057209817362, 15098281334975233, 1101146015708157, 47550101433457787, 12050597934415257, 128657844735176285, 169277061937864378, 330510651947427135, 340288707202349036, 11709533245952345, 302127549822334661, 2559809026849192761, 1568191551607991366, 3600013976164019953, 7680536423553600728, 17111575771294704535, 29807283816584340074, 53397101317854812084, 16641745710990072136, 1079100819585860413, 125341458820724802472, 33195859417603166742, ??????????????????????????????????????]
            </code>
            <form>
                <input class="form-control mt-3" type="text" name="next">
                <input type="submit" value="Send" class="btn btn-info mt-3">
            </form>
        </div>
    '''

    return
    random.seed(1337)
    sequence = []
    for n in range(1, 104):
        y = fib(n)
        x = y % random.randint(1, y)
        print(x)
        sequence.append(x)
    # 117780214897213996119
    # GET /?next=117780214897213996119 HTTP/1.1
    # Success == cookie : session=z.NwQhWmh5Kbl4VNVsIzx4YD6xrrLPjVq3FOCk9CFnqOv7LSWLSaP4wrOjnvPyvFD1DySvQ+35PBzY6LAs/4UGUEkyuww22aWRkhZvSPJBm41kpd5zZBHWBHmQrp/FMAgjxA7cngirr0OJ0B7gdw0RBWmja3WJwup29qsN+XtV5XYcv39ZO/9GJk4VDIjDeKCeVt9vARHRbIwTt0wRt0X+pKSFjyARr732kbw/gjpfVfD3ZCydVIjPOtOYIwxIVp/JW1P8EIuR4w8CBbNcT87UJhxDgvyCPt6cGXBs7M95oD2j05Fu+ZSaVF/zCXoCbiO4c9ar5BiS/JyCUxV2qMnKd0Qqx9EiDSU7mMSfZiQM3gUA9B+wqvLnkRflA+coOnvE1YSb9TJXM0d24CdiDY3eoq28RSEXADyHbzcj.JtrGUXoxLhDUvRXHPDWPJg==.C8pCM/vAcJYDkre97MdB8g==; Expires=Tue, 11-Jun-2019 15:23:26 GMT; HttpOnly; Path=/
    pass

def fib(n):
    if n in fibs:
        return fibs[n]

    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    x = fib(n - 1) + fib(n - 2)
    fibs[n] = x
    return x


'''
Draws an ASCII art variant of the maze
based on the local in-memory copy
'''


def printmaze(maze):
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    print("\n")
    # print("Current character pos: ", posy, posx)
    row = -1
    col = -1
    for y in maze:
        row += 1
        s = u""
        col = -1
        for x in y:
            col += 1
            # Draw a wall
            if x == 1:
                xp = u"\u2588"
            # Draw an open path
            elif x == 0:
                xp = u"\u2591"  # " "
            # Draw an already seen path
            else:
                xp = u"\u2592"  # .
            # Draw the player
            if col == posx and row == posy:
                xp = u"\u25c9"  # @
            s += xp
        print(s)
    print("\n\nX: {0} Y: {1}".format(posx, posy))




'''
Main game loop
Walk one step in the given direction and search that square
If the search returns the key, we pick it up and store it in variable key.
If the search returns a chest, we open it if we have already found the key

'''


def godirect(direct):
    global posx
    global posy
    global keks
    global ans

    if direct == NORTH:
        # r.sendline("go north")
        time.sleep(SLEEPVAL)
        ans = requests.get("{0}/move{1}".format(URL, NORTH), cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        posy -= 1
        if ans.status_code == 302:
            print("Got 302!")
            time.sleep(SLEEPVAL)
            ans = requests.get(ans.headers['Location'], cookies=keks, proxies=proxies, allow_redirects=False)
            keks = ans.cookies
    elif direct == SOUTH:
        time.sleep(SLEEPVAL)
        # go /0/1
        ans = requests.get("{0}/move{1}".format(URL, SOUTH), cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        posy += 1
        if ans.status_code == 302:
            print("Got 302!")
            time.sleep(SLEEPVAL)
            ans = requests.get(ans.headers['Location'], cookies=keks, proxies=proxies, allow_redirects=False)
            keks = ans.cookies
    elif direct == EAST:
        time.sleep(SLEEPVAL)
        # go /1/0
        ans = requests.get("{0}/move{1}".format(URL, EAST), cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        posx += 1
        if ans.status_code == 302:
            print("Got 302!")
            time.sleep(SLEEPVAL)
            ans = requests.get(ans.headers['Location'], cookies=keks, proxies=proxies, allow_redirects=False)
            keks = ans.cookies
    else:  # WEST
        # go /-1/0
        time.sleep(SLEEPVAL)
        ans = requests.get("{0}/move{1}".format(URL, WEST), cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        posx -= 1
        if ans.status_code == 302:
            print("Got 302!")
            time.sleep(SLEEPVAL)
            ans = requests.get(ans.headers['Location'], cookies=keks, proxies=proxies, allow_redirects=False)
            keks = ans.cookies
    # print(ans)
    # Send search command
    # r.sendline("search")
    # ans = r.recvuntil(">")
    # print(ans)
    # Have we found a key?
    printmaze(maze)

def load_map():

    del maze[:]
    pois.clear()

    f = open("map.txt")

    currow = -1

    for line in f:
        currow += 1
        print line.rstrip()
        cur = []
        curcol = -1
        for c in line:
            curcol += 1
            if c == '\n':
                continue

            #if c == '1':
            #    c = '1'
            #if c == '0':
            #    c = '0'
            if c in ['A', 'B', 'C', 'D', 'E','F','G','H','S','L','X']:  # Challenge 1 '2 Hasen'
                pois[c] = (currow, curcol)
                cur.append(c)
            else:
                cur.append(int(c))
        maze.append(cur)

    f.close()
 #   print(maze)
 #   print(pois)



def replay(steps):
    # Replaying
    for c in steps:
        if c=='u':
            godirect(NORTH)
        elif c=='d':
            godirect(SOUTH)
        elif c=='l':
            godirect(WEST)
        else:
            godirect(EAST)
        if ans.status_code==500:
            print("Error 500!!")
            exit(1)



def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def solveCottontail():
    global keks
    global ans
    # Cookie:
    # session=z.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.tzAFn2js+S9gDTQ4llWB3Q==.H6dGVxPPSSV5UvXmfbi1SQ==;
    # You need to download the image at
    '''
    <div class="text-center">
                We require you to prove your rabbitbility.<br>
                Prove that you know the c0tt0nt4il alphabet.
                <br>
                <img id="check" alt="tick" style="position:relative; left:200px"
                     src="data:image/gif;base64,iVBORw0KGgoAAAANSUhEUgAAAD8AAAAPCAIAAADcR4AlAAAEmElEQVR4nNVWa0xTZxh+z2l7egUKlPudrmChYCnQykUdUBRmkG2oDPgx1G3GLQvGZVPcEmOIWZRs04lTl7jEqWOZM9HJFjYuIiggo9yqYikgN7nXQqF3zjn7cRZGUKuGmWXPr/d7v+d98pzv8n4HyfzwCPxvgf7XBlYE+mKUGt8mCnh4rSFxdMr9cZ6APxsZOtA34jsy6QEAbKZVGt6L0RfaNSKDkbOMzGbaVof1Mhl2AOjUCmfmeCs3iqLEellnkM/42LSgpkW2gNP+ds93mt+Tf0keeR8AmtSRT3S/KnhoX+EPZ69sGqn1AIA0edv7W68AwN4vPzAYA5eRZWLNpzsuUPH+E7tW7h5FiZLd38WEa3ECpaFESlxbcdl7JImgALAz+zeh/1h5ZZqD+i6t8ONju+tUq6nhrzfXfHFh29PItzqi3j5Y7IDwong1tjMmXHvq5+zsvYfPXN4cLepXSLqBWvuyn97AcTQidDAvo2ZZGcaw56TVO3NMi5nfm+MHRr1JEllc0bgITUy4FkHILq2wWR1BJaf0/Cm961IpFmbLSavnsc2PDE7ikMHrrTEuPGOsWKPqDq9oSPBy02cmNRMkercvOF2hQlHihkp6q1NC1caKNbpZl4qGBJJEfqlP3KKsU0i6m9URdACw2hhP+2gWZkuLV7nwjACAogSbaevqDR0Y9V7KeTO1XhrWa7UxmJh90f3jcHWe25TcxHeat9oYM/O8NVH3FnDa2LSbQtI9POHJxGxZ65pYmA3SYXjCk8OyJEvVh74tvH1HTNWO61xJEgEAkkQmdG4erjOw9NY+EQYj952ST6g41G+0bN/xZYS3NtRKw3pb7oiPnMszW5kOpMam3c9VbCzKu7z/xC46DS/dc+rr8pyWu+IfPz8U7DN+9UZSTYssI7Hl4Ont7RoRnYafLzmskNyj3NNQgiD+aY84gTLoC7DyjimXdM/M8UrP5zq2vhS6WWecQAFAP8fDCQQAEISkpkwWZrtGBAALOG3OxOGwrFTeaGYxMduiAguzUedlpe7/aI7nsi1Hi864u8yuUMoBHk4JArwm2UwrAHDZlgDvSapxowAgET7Iz6hWKloBQKlozc+oDgsccSznI9CtjVEDQGWj/LNvdob4jn310cncDbXe7o8AYGNCS0Fm1aJgQWZVanw7xrBHi/oBQC7ppkRkq7QIAgAQGToQ5DMh9B9lYfZkqRoAxCGDzlyTv9eUj0AHAFXNcSzMfmDHxXWyzuLtF5kMe+2fMqDOfZJUvXldI7V9SrmKJBEu29Iz5O/AvShwJCWunYqHxr0MRq6AP1uQWa03OE3q+VuVdb4eOmpWKVcBwOiU4P5AAPWkZK1tPF6+BQBS4tqv1ScCgEzcox32Dw8aRlFiW/r1mx1R62M7nTgmDssSLeofm3YfGvc6e/W1wqzKWLHGamOcvPR677AfACDP/58jET44WnT6QNm7HT2vPGfJvwsex+zpqh/XuZksLCrzjJ7DxOyZibe5bDODjidL1QYjVzvsaE9eKuZN7HkTe2nmGe75vPn8jGoex7yA0/pG/Eq/zzWaWS/T4YvhL0pG0PZwmSh0AAAAAElFTkSuQmCC">
            </div>
            <script>
                $(document).ready(function () {

                    window.setInterval(function () {
                        var el = $("#check");
                        var random = Math.random() * el.parent().width();
                        el.animate({left: "+=" + random}, 500);
                        el.animate({left: "-=" + random}, 500);
                    }, 0);

                });
            </script>

            <hr>
            <form method="get">
                <div class="form-group row">
                    <label class="col-form-label col-md-2  offset-3">Answer</label>
                    <input type="text" class="form-control form-control-sm col-md-2" name="input" placeholder="Letter"
                           maxlength="1">
                </div>
                <div class="form-group">
                    <input type="submit" class="btn btn-primary" value="Submit">
                </div>
            </form>
            '''
    # and perform some tesseract on it, solution is the next letter which follows
    #e.g. 1klmn0 --> "p"
    pass



#def init_maingame_loop(dimx, dimy, startx, starty):
def init_maingame_loop():
    # Send "Play"
    global maze
    global checked
    global posx
    global posy
    global ans
    global keks
    # Build an in-memory variant of the maze
    # dimx = 40
    # dimy = 20

    #maze = [[1] * dimx for x in range(dimy)]

    # Build a "cache table" which flags which squares already have been discovered
    # This is probably unnecessary and we could do w/o.

    #checked = [[0] * dimx for x in range(dimy)]

    load_map()
    checked = [[0] * len(maze[0]) for x in range(len(maze))]



    # Start position (arbitrary, right in the middle so we have enough space no matter where the maze grows to
    startPos = pois['S']
    posx = startPos[1]
    posy = startPos[0]

    # Initialize current pos as "path"
    maze[posy][posx] = 0

    # Print the starting position on server

    # Print local in-memory copy
    printmaze(maze)
    keks['session'] = None
    keks['session'] = 'u.tWsJKOPDC47SSLdM/lmr5V8LM63jqUhLIqGUB7bx0pd2pYmLxfrZsSVFOc98H+tkEjFpY3BQbENRTYgiGndJke9HVM5EK8bJ9cJ/EMZMlr85X+lB9gldqcG2VipGP991GXgr+jzwOcouu+YPziwTHYAktr8GcB7ihryr0eZhnrlIXi47/4jcZoS4oEVSQsEnyW5iSDOdC4PyIj6HiCAXvSo/+qef9ga2X5PXjzpXMv0450nOL9H1NJ2/qGM6WEJoCL1a0GLL+r3fZiHt6AYOA99DLOQLC0sVzux98tBZ9z6tlOmBypDnwZgX3plpIJGd5/Tu68f39XcoJYxX/AZk4/XgqzhfQxXYBSi1io7D7czXZkuNMLIaIQspdMkI+egHy4Pu1DcNstfYmIuzuwF6xfhaL9NbH9vIn3rBsLGH7+FPjD4zpQKk4JY6mcNn3Hwe4OFasOEECXz3GerPLOoCE5++dPN55PIf3vO4UZ8fEFgUYm1gzyoAcgUImk5gpWS5bWl0C+witQiWtNG2MF38RuCgZKjD5NR36illCd4eKjJ0xA5+zvlYdkwsnBUUHpNh88v3YKSKuG5j5A==.H8mIMd5dgOcNbzc9v3lGrQ==.W9PJcwgy1P0Jnvd8sLx+Ig==;'

    ## final flag 22: he19-zKZr-YqJO-4OWb-auss
    ## final flag 21: he19-JfsM-ywiw-mSxE-yfYa
    ## hf3: http://whale.hacking-lab.com:5337/bf42fa858de6db17c6daa54c4d912230



    ##
    '''
    <h2>Placeholder</h2>
    <code>[DEBUG]: app.crypto_key: timetoguessalasttime</code><br>
    <code>[ERROR]: Traceback (most recent call last): UnicodeDecodeError: 'utf-8' codec can't decode byte in
        position 1: invalid continuation byte</code>
    <br>
    <code>[DEBUG]: Flag added to session</code>
    '''

    '''
    session=u.B+wsjdtJ9AvDOX9YS3fHhPhlTg1HmZlQ3ADO+uBq7IQyQjqEXV/GtE4U/xLRVbSt/IDPlMvOgXuLzThKsHWVR9QznSU7xg50b1WnK+P/JXBB75xi0pyVWA+EzQFTPsVd1xCvUSdPoeE7TfjM7W2scr+P9fgTDwwXgCjQvKVjLYFnxNhheZqMZ+XYLJ5nt9u0FVvNGXPi4NaFaxbjG96LDA0U1XVAJGDNQGqSt0UCAX64lRWr3S6XNvzd3rboxch+Ck5YvFQ9A2qjY6wp7ujuA9M7sUMp8c5kvvknm0vHqFEYW6iFAR0d52It7Uxi8NTzaHbxp8Fr1qwGHHSu16xfYeV7iJm0ZA+ihOoTcj2HyL2dZXePm5NdeASY4VOcXg12nVv32ovfzYwx3uQoAtKzac9qtYyQWHYyj/+fX00VrEgUAFCuOHs8s6FESpVbIzYq4f5qSDvbtWTsKkOokp0hW+PIS078uyU09dOEDO6Ef0vQcBvPH79n5k9Bjf3KP4w7TF9KjbIqukA9CKX7Gpza9vEACBvZCeZ5Iq/Z0YVNmYBxcbzbZDd4IM6GHe/DpYhYO8mDxi5Zys+lR8d4bEId8psPX8GD/6/pY20zkSsD1WFVeERg+KVF9nzrXgKsA9Z758syArVcOoww017g209PEU4AKZjLWEzN3Jw0JGVfs6o8LkSey8BKQQ==.n7n5qF4jM63YG7+2TZMGqQ==.B2OnQIR1ur6PAucLXUHtXQ==; HttpOnly; Path=/
Server: Werkzeug/0.15.2 Python/3.6.7
    '''
    while True:
        # Find the directions possible from the starting square
        checkDir(r, maze, posy, posx)
        # printMaze(maze)
        # First step and recurse
        if maze[posy][posx + 1] == 0:
            search(r, maze, posy, posx + 1, EAST)
        elif maze[posy - 1][posx] == 0:
            search(r, maze, posy - 1, posx, NORTH)
        elif maze[posy][posx - 1] == 0:
            search(r, maze, posy, posx - 1, WEST)
        else:
            search(r, maze, posy + 1, posx, SOUTH)

        # It can happen that the chest is discovered first in one branch
        # and the key is in another branch. In this constellation, we will never
        # visit again the branch with the chest and thus cannot solve
        # Therefore, if we return to the start, we run once again and forget about
        # already visited fields

        #print("Restarting the recursive walk!")
        #waitKey()
        # Reset maze
        # We also need to reset the checked maze unfortunately :-(
        #newmaze = [[1] * dimx for x in range(dimy)]
        #for y_ in xrange(len(maze)):
        #    for x_ in xrange(len(maze[0])):
        #        newmaze[y_][x_] = 0 if maze[y_][x_] == 3 else maze[y_][x_]
        #        checked[y_][x_] = 0

        #maze = newmaze


'''
Helper function to wiat for a key press of the user
'''


def waitKey():
    # raw_input("Press a key to continue")
    pass


def search(r, maze, y, x, direct):
    global posy
    global posx
    # print("Trying ", y, x)
    #        sys.stdin.read(1)
    print(checkDir(r, maze, posy, posx))
    if maze[y][x] == 1:
        return False
    if maze[y][x] == 3:
        return False
    maze[y][x] = 3
    godirect(direct)
    oldposy = posy
    oldposx = posx
    posy = y
    posx = x
    # printMaze(maze)
    if search(r, maze, y, x + 1, EAST) or search(r, maze, y + 1, x, SOUTH) or search(r, maze, y, x - 1,
                                                                                     WEST) or search(r, maze,
                                                                                                     y - 1, x,
                                                                                                     NORTH):
        print("Did one step")
        return True
    # print("Did not find a step,need to backtrack")
    if direct == NORTH:
        godirect(SOUTH)
    elif direct == SOUTH:
        godirect(NORTH)
    elif direct == EAST:
        godirect(WEST)
    elif direct == WEST:
        godirect(EAST)

    return False


# Set run_local to true to play with a local instance
# Tested with Ubuntu 18.04.2 LTS 64 Bit with libc6_2.27-3ubuntu1_amd64.so
# sha1sum(libc6)=18292bd12d37bfaf58e8dded9db7f1f5da1192cb
#


URL = "http://whale.hacking-lab.com:5337"

# The chest key


# Connect to game server
r = requests.get("{0}/".format(URL), proxies=proxies, allow_redirects=False)

keks = r.cookies

# Send format string exploit in username

print("Starting game")
#init_maingame_loop(dimx=80, dimy=50, startx=2, starty=35)

init_maingame_loop()

# Orbit mode: URL = /<md5(p4th3)>


