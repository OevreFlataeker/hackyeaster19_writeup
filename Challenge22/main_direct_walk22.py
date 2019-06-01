#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import cStringIO
import requests
import json
from os import system, name
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
    # session=z.22hF5o6j4RgI62tgExamwCuhQVWO9x/d3efhu0xSBjbJHhctY9XWnGaUW2TduRrxy7RHyYDGA7DIGIg558eAe/dNi5b28apn+OJpDuTeqqdKwfmBRAWF6wqSULCuj1/BvzqvfAghl2iQ+Hkr+6e9gordqVBgTqnhwMFu86ecp0uxtKlWPaC5Jwn9wzCdDmutlOEi5TC+CJ+xYmxfXza+jzxQy1PuD61ybHWEfVwqPBuZib8tRv0+ZKKA5vtTDQ9tBLg0RUVtAPsc3a3kuivF6KgkexWfpgztsJVtAD+BAs0HUErh93VKa5hoyDeRpfYdrgESYGOJDjXXwGlnR9De25n1Mxb4mygTtOuu0XSxZ9ZxKDTQMjMBWv3etXY/9BY2T+sEVV/X3BkB5U+o03rRF3EWu8SKf09Ux2Bk1qb6Kg3kCt9SBCsJ5jY7PNC4H2QMLIrI2qnsSlVFDyUAMRiudyv8rexSh7UurKLRg1mXrKQTvFTG87bKIcczhfhBetxNrb3GOSOVNsx7qhWg2h+m+/oW8PQ/77dLAqYv9TkiiUdW+aiQrALaJX6Z+VJApW4ZZ9s7F3jgxas9Kx/65daWLgTzHsRtwQqzmdGsugvkcbuIAnQrJPlnzgmwZ8l6sx1FreUNbwp7CUESPsQqBtjdlAdXhu3EdYcL9uFlZJdP+1yWIPPypEMNJgCJo/l2JMNyKm7bbaAKSLuYWWDu05WRpr7tvD4GSbgBo7gxa/6mWdXn6bLc4KwA+eSLe5IDxA0r4bJoNN3t/myafDshmimEZ/nOP5nJMqT6aGWo+6fRaY9/DKmvvygtaR1vC1nmWhadJtv8aSj8LDJfi1xKcA3jgtrgegdoPdEZ/kNtJGbJGs2r/enpNOulnw3jiN8+29FRrnZ8l9LOA7n16a3Oefj8IIqtCBFfMPP20ov7QbuEI9giEitKjT4QilrVGSfEhdjsyZK+bJUsTsBAf2Aq2bRvKCRA3eUZvGC6GDoGQ8c3PYEwmBo2Zexu4AeU0EwIZbyKdtkGDJ2MMGgNfYE5Lw38sPOSC115jPUHIu3FgBQ085CCMtmoKhegFxItoe4ZukpkRkr/QR5wo30hprSjX1mcW1vpKcpCF6QSitEEhFE28hNEXg5gxzwBDiKUYaR3F0aJMxVh2mk6aNUsO2JzjuN7BsDaDh1ew0EikDqP820n++hO8cAES1sbmAKd5QXQLFgyvVCShTebtcd7IeJNvoiAyL0OWCTBPQMESW8J4g42FVXmk0gEBzM0u1ggjTeFTsKJsENRF8JHvHdoRA2tZkFbUfA4f0clLHWLYtHcIh4cELrMCclLTLXSLZCaov03+FMLMVmSEtcmQl1whBZXFHalhDhwhQPG/PQm2wlcsX9IJmvZGTf+9Kr57Nw15ic+yfiwH9mZ5visp+4J8zVtdAgCBkywMAekJ+d5j1OyR3MrD2Pd9fR5ss5jxNqJ9dOl4bYZ5fKGGZQTae5UiMmYvbhoSO0TD96MDOUOnv9N24sIkChketHujNH+Zzp3PiSc1GLBDK98Nh7RqUrZPVTXSoGCqAMVa3OyMTXEWkaRA3j+kJDeoMFsVz7h2r+ILiMemGy30riAqhEkUMa3xzP9WGoPoqlJjHtqRzj+j4DHE0JUd23N8m9KXOIOqM6Opf6vaBtuHywaqMFLzBcv3/ZJjuHA8GQ+aYZR6yc6KEBPrYpeeh5pSV66x+yGUUXMeh+ULhEPUick+jFrwHcqoEaQvUpUlQBSX0gajoEJoAFzq/JmiwhCtRvjtypsKPlnrwrCzAoVGQerzburSujsVN+T8dYNKsjco1AxCZI7rdZYXXHqFmvviRAc64u69fOy7lOw5LjzEIrugvzqdneVfQsSRyCsGwKPm/6krHxFOB7hP3G5EBJOkRVczwx5LYAA9Akniytn/NSo8A20OQaneQiH0vlrR5+eTz++YHR9bPe71kK3iKmP06+Ux6RHBjdi515RMB+0F/JrcKWyVt1OOGZcbCNpH6F4IG9ANftKr6Dq0ZU/ULQdN9vvLDEsyHbQdfhvGuBQitsZA+ceBrjydlDjqCTQEm1JeeftEP3azwJRwUGPf4pZAoz5c5bdDHdzOoKtmKJozJAJhiD6cCID8mb8uH8cdCFk/MK6ZqX6r0cId2YX6SM5TyiGykxf3Ny8qt49S2Pl3xtljlrieTVDca/radKGh7ShtQuClNvw9XT3DJEaSfqu9rPb6ojySJkuQt9DzQuziSkIrMRulxhxomiIjKUFVwsilm9mx19Ng2TffRfKpAzeQK9uPoWU0nggIV8osATX/FTkVk35/kFA+RL5uGNPPGsh1r1h3qYYyYFySasn5p2NSZGlk8VAKadbJ829MpyT/dTcRRyTGu1PZTp0MkLkx8qGXT0LJ8QIisD2sVhxkH4GGpwottstTIwassr6qva4FHC+59FASeg1PEvh4GCaEsXtLHivRMPyuQ2qBxl2KQOdF8oPTbh8LFQLXBdOKwA7J4SWYkiS42R4jnB/FyqQHDC6H+QHrKYSDi99fWRw5hzrDP40Me7sdeAdRuhdCVXcAAsPPgSgJO/S1C7bcTSm9vTUP9JWXR9vttNONQapifos1+M+tlkZAEVTLb5/aSmtUWnZOzaLB5NekmauzePnL4nkSMEg5DKppy2/eKfIdp0jh8xjhbnUcSXsNLf0x+L0cOXU5vKu+eEWOQsj4K80TpRxhZC82GMzgDWMxwgUOR/4LB4glyV44k0am4iSVlUpS78RQ+2GDrqHtW2lSu4sYL2X7v6tt09EVyJBSAkzR8AYXtt0.tzAFn2js+S9gDTQ4llWB3Q==.H6dGVxPPSSV5UvXmfbi1SQ==;
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
    #printmaze(maze)
    #replay("llluurrruullluurrruulllllddddd")
    #FROM_S_TO_TimeTravel = "llluurrruullluurrruulllllddddddd"
    FROM_TimeTravel2ShowThePath = "dddrrrrrrrrrruuuuuurr"
    FROM_TimeTravel2Fibonacci = "dddrrrrrrrrrrddlllldddr"
    #replay(FROM_S_TO_TimeTravel)
    #solveTimeTravel()
    '''
    Start:
    First chall: Simon's eyes
    session=u.NVMthW3UvLBHvsyvOCA0iIpkpAizdMAbXUrI/2L82eWtGoGqHIENY/KQwLZQJtUPMD6EmBYzZmwguKnNR5sPCbUzuAJI/ijaxqM3uZ0NmckXrbikA8l5GB3U9LV1PTxZZTiLUyqywiOEPQMzbCuifdanwmNrieOrwtaSxQiOnPkd+LyAN6SeI47HChzrZy+KbrcGa3XgDcuYcxICuIS2j5ru6Sjvz6eGk3icq6T7n5nRpBTQ5z4e9b+fYmDIPCdHBXNvrXd7ShK4sC+Fla0Z1P6jU9i9kgGFSBqnzgdYf8Aefn6yZ8UtNaJeYHytiJJ6OXwJGn1oSBHvol03jkhLaad1OUylRlWSVbU6PK5LyHZanQ7pmZui5aUN0XiGKOX7NFUoh3kvIyA9aZfU4A4LMnaa8jCnkylNHxaf02Mydm38oNLJK1fvg+gyt1Csu4wZJmIhe1ty6eS+HvWtsbCEZhpSiz9WhWyz4mhxrM83UT/+YNipKl6Wvtzah8bgkL4sU6wH+yAjFs1Z60BNI3rYM5ONPljkG/WKUQvMNauJdsajbhzgXJjPMyitjKSn4n8dm/EVsXFNNBLvZjNWSLZrqoetcuLKRHXsQD2kUMdAc/Y749/NSUGxrpHM9/mKYORT4aEGGqSsvfMgYi4plA5EU7Dbye4PF5mDXaSFaZsG5kKW8I5eCLgCm67xgecv5L8dqeoELMVbg5rZ2CaeqWuoE0YIw9E17gE/mQPRWge7Ym+l0hj3ChHb5eITf7p5HSz1O4ejS8uVLbvKve0KP2Im3DeDVEEHHn3d4w1KTzZKEyT2Jet8Yc1IYhn5zoij4500NvpTD2Du/RrfWAyIG3r3A4OOiVqmdQdEMXLO0peAgyd2KsiUia2yoN9bYQauzFs+DLoy4q9Nm4B1pPE/WMwFFXF+4xa3sL03OSo8i55zFYyVxHeAFLkvGjA4k/eUoIHlVBvt1m/CLbnqM8FskHuseF3h8nPvFC5J0nkdz7v2Hvj4BY9cMJQ4N8kFcJ8+Zy3cu5UzFS4OQfaXV1BViJCdcyxoDG2T9A0iNXNjwwz90yPeP17y3bCIBnWpJoeun25uqYu6CMGDEiY6sbKuuFGoncSkj4qcrVg89tfR33JPit1umKIQk/TCLVYYpA9YsJbjDGjIIXuspIqxUS3RsBQE2qcwsmrni35aSnwlWfVUvI9H9aOaGr/ygf6cS+lKizbWQvjphLho3QVgiMKWYqiy14Hpwf90VjPpbjgHV0/dJWewrJdl2V0j4Q5HnsH5HaW8ClvTRSipTiDwtJe63/yRR9PK9w==.5DtZGE2T7n8pqrhHHBEzvQ==.fpGqSchBtivHvldpdQisNg==;
    
    This cookie is one step to the left:
    u.tzmL9nJEggvUhZ5Hb3VCeOsiMN2pLYA0+t43fZgTeljwA7OVHJhE0+6J4lDugv14fVs3HtrLbcAk6mD57ssfxYBFJ+MV/ZwLFAkifdUUf7WygKA/zVeA3FSiPN0tTIfoO8ntS8YAZ2BFhZPTdeLsprNKhLamxWOpVbQ4V45k3PZiETdyTunkulIEWohz61x1gaPJfZqvt8aQ7fR23/+VYlGQ2hHX8rUySt+pwywv/uvUdlklMfbpqLzxuEyIOSQFtPxTg2u6htgq7oaEPVCgBvCu7PzCxZyobYNPv8XqLwVwDYP55sHpLBuqDgxA6ihCHDGKUm/HTD8cD7CmiUje2t10EUY8AJSPOGMERquQ2MvN95fZ0S7LyXltzRAS8jyYHNskyZtLYbw8LOit01EVf8bniQOzNZRYjNUNl+duSjwAnBx2Fv1qRCRp0JxYRyNnAr83KqB4VtRsXy5U8RMUqusDNK6KHz5cJWY/LEft+29+/1L3S7auftjygfLSBOkGS/Gn/dsddPPCQo87AaSNAqRiyCcTIaEFr9TOPD1Ny4Omd1uBF/y6cfSlfxhwXY6Y87cSGeed+z9LSBqe7yH0Bjrqe9gdtH4P1dvs9Uq7l9CvThR/RHMdhXtETLETTkDVzA8EJozzgTwrnslGz4vVmGUIu8G7F7EBHuA5Re6EpIaWCkbVCZmSp02xrB6YDS4LGcamWxS46H/N9KtqwglWO13dxptazbJZyzSwuvyhTWMiP4riQ8er9jx8Tb/Wg63wz17B4SGy+dnxf2JhGz0+tRsjU8PHH2YDdpnFeW/ZfVroIPuxDGwCwxKhcTDDZkvaqJMB4ZQCibiqd8YKHSzp4ruO1y0WOx2IHbQlcd8mtA285TZq5SZyRRlbW3nFYDsl0Q6pmiKkNHddwf8SnHLMRH8vEmKI+YVJm+X+wvqMzwiuIEBxiA6obQugw/PP2HINlB75erGAUGmlw7M/FUTgnHV8SzXUtdK5sekrGZ7Dmckw2J/sIKpTO+2ffl+uaeeN0I63tggFObCVJuY9xn6P+6NI6NEcDEFvIleKZGR4jlND7FiSQ1up14tDSEjs5lg1++ajoSgxTJJ7VbK4oQdp4gc86h2Ar51WDnq05Azf+tgor3sDZPQYTgwA4nb9mmt+Zipb107iOkOcCizNxByK2loUGMUBiCYd1LcQSsCJPchsMe2KHzgADo6lNILheHRPIsv2M3T8dkR+2TOaMF/c.ubIk1uQNskfPTlEfFZe5Ww==.911+BpjwYr88s9eswXJwUQ==
    
    '''
    keks['session'] = None
    keks['session'] = 'u.tzmL9nJEggvUhZ5Hb3VCeOsiMN2pLYA0+t43fZgTeljwA7OVHJhE0+6J4lDugv14fVs3HtrLbcAk6mD57ssfxYBFJ+MV/ZwLFAkifdUUf7WygKA/zVeA3FSiPN0tTIfoO8ntS8YAZ2BFhZPTdeLsprNKhLamxWOpVbQ4V45k3PZiETdyTunkulIEWohz61x1gaPJfZqvt8aQ7fR23/+VYlGQ2hHX8rUySt+pwywv/uvUdlklMfbpqLzxuEyIOSQFtPxTg2u6htgq7oaEPVCgBvCu7PzCxZyobYNPv8XqLwVwDYP55sHpLBuqDgxA6ihCHDGKUm/HTD8cD7CmiUje2t10EUY8AJSPOGMERquQ2MvN95fZ0S7LyXltzRAS8jyYHNskyZtLYbw8LOit01EVf8bniQOzNZRYjNUNl+duSjwAnBx2Fv1qRCRp0JxYRyNnAr83KqB4VtRsXy5U8RMUqusDNK6KHz5cJWY/LEft+29+/1L3S7auftjygfLSBOkGS/Gn/dsddPPCQo87AaSNAqRiyCcTIaEFr9TOPD1Ny4Omd1uBF/y6cfSlfxhwXY6Y87cSGeed+z9LSBqe7yH0Bjrqe9gdtH4P1dvs9Uq7l9CvThR/RHMdhXtETLETTkDVzA8EJozzgTwrnslGz4vVmGUIu8G7F7EBHuA5Re6EpIaWCkbVCZmSp02xrB6YDS4LGcamWxS46H/N9KtqwglWO13dxptazbJZyzSwuvyhTWMiP4riQ8er9jx8Tb/Wg63wz17B4SGy+dnxf2JhGz0+tRsjU8PHH2YDdpnFeW/ZfVroIPuxDGwCwxKhcTDDZkvaqJMB4ZQCibiqd8YKHSzp4ruO1y0WOx2IHbQlcd8mtA285TZq5SZyRRlbW3nFYDsl0Q6pmiKkNHddwf8SnHLMRH8vEmKI+YVJm+X+wvqMzwiuIEBxiA6obQugw/PP2HINlB75erGAUGmlw7M/FUTgnHV8SzXUtdK5sekrGZ7Dmckw2J/sIKpTO+2ffl+uaeeN0I63tggFObCVJuY9xn6P+6NI6NEcDEFvIleKZGR4jlND7FiSQ1up14tDSEjs5lg1++ajoSgxTJJ7VbK4oQdp4gc86h2Ar51WDnq05Azf+tgor3sDZPQYTgwA4nb9mmt+Zipb107iOkOcCizNxByK2loUGMUBiCYd1LcQSsCJPchsMe2KHzgADo6lNILheHRPIsv2M3T8dkR+2TOaMF/c.ubIk1uQNskfPTlEfFZe5Ww==.911+BpjwYr88s9eswXJwUQ==;'

    posx = 35
    posy = 12
    printmaze(maze)


    ''' Solved it with this cookie:
    session=u.PHCbVEcbwD3pdiBJf4MpdrBsH+Nk9kp2WrMOnu4XcABgJGJ5S2ORa+f4qDZ9BOQlmcukEBIpFrhxmGvatJtm+jj/9OX4sqDyMDRpBjEgm5UijxT9OgXkc2PPC88mZQgdCCQdiaxqMq+XvSMLFSluDXJ3Fj/jFNKkaSdPAMCh5ti+tsaKD1RmzhTBDkHavGg7rFGXWyTFVDUdwA9zA4BNdZJdx7201x5v6u81tGE0uI5NWj+vJ6FUMngZ6FpwdDWuP3Ff/Y2O7ouwpCmxhBq0FDDQp0WvxnJY+6KSoMj0xTBqlht/RwX87fJHnxJMtA5JtwR9ecRLQHeZCLtv/FjdliLtl0yeuIil2hbY5yNV0kZdzXZ8z9q4CHH9Nk5/9O0v7FZYZ3vNmxR1imQlXAGXq3dqnNLWtdlMh77QgbzaZjiZ819qaIMEAXhp/LDi0MkgicNXoQtV2h/5Yl1LbRyh7zGaRr70ZqJoN2BYT9vLr96WVTS1MwTSlhoThsufXSPJznpvX4uoc5EhRh4N7lXeOb0oDHJGIqZ1Eu8qMpxkZb7VcPdLbTT9/G7pOqWD0/c8VYf+oJfhaLvbHqwnwEGa/SL/LEQ/VXx84ASFkQql4bgCaXXyQLsHvyqHWEfhhBwyL3qhoHmUwp4gjXhHMk+V0wVsKvrhYFP+wHTdHXYq8F/iRN9Br4JWlqrIjtxBTUdbr9670C6kHUb8FfsAyDpiY+ernCckLiKhuNNtc+WFtrCoQ+qmecPHaOSd9icbe9d/FgnatxzKeekqp1V1iLw4KY/CX2Rbvy/q/jN7Jic2Cw2zmFXAAFE2S2T0q37yg5cJoKzFgZ4ZDfRSBfYkRFPdI6V1Rx+fa6hu62lcLEcfGar+uytLk7o8ZyilxhXBTQwIHIXwS55smN9f9Vge2UA+HbgZRAxjtvqLSyE6tac6dkEuQRWrSAvkPtEfqQ4tiGAlz2M+PcolbmVUMEeyAS3xVhzTBVylWcvAWmq85WN/r/6iqxG3Jn8uHg==.BsRopIPJXGLeD15A+OrZ0Q==.vIZtgCGHtwmAXg1vDLuniw==;
    Position after solve: X = 33, Y=12
    '''
    keks['session']=None
    keks['session']='u.PHCbVEcbwD3pdiBJf4MpdrBsH+Nk9kp2WrMOnu4XcABgJGJ5S2ORa+f4qDZ9BOQlmcukEBIpFrhxmGvatJtm+jj/9OX4sqDyMDRpBjEgm5UijxT9OgXkc2PPC88mZQgdCCQdiaxqMq+XvSMLFSluDXJ3Fj/jFNKkaSdPAMCh5ti+tsaKD1RmzhTBDkHavGg7rFGXWyTFVDUdwA9zA4BNdZJdx7201x5v6u81tGE0uI5NWj+vJ6FUMngZ6FpwdDWuP3Ff/Y2O7ouwpCmxhBq0FDDQp0WvxnJY+6KSoMj0xTBqlht/RwX87fJHnxJMtA5JtwR9ecRLQHeZCLtv/FjdliLtl0yeuIil2hbY5yNV0kZdzXZ8z9q4CHH9Nk5/9O0v7FZYZ3vNmxR1imQlXAGXq3dqnNLWtdlMh77QgbzaZjiZ819qaIMEAXhp/LDi0MkgicNXoQtV2h/5Yl1LbRyh7zGaRr70ZqJoN2BYT9vLr96WVTS1MwTSlhoThsufXSPJznpvX4uoc5EhRh4N7lXeOb0oDHJGIqZ1Eu8qMpxkZb7VcPdLbTT9/G7pOqWD0/c8VYf+oJfhaLvbHqwnwEGa/SL/LEQ/VXx84ASFkQql4bgCaXXyQLsHvyqHWEfhhBwyL3qhoHmUwp4gjXhHMk+V0wVsKvrhYFP+wHTdHXYq8F/iRN9Br4JWlqrIjtxBTUdbr9670C6kHUb8FfsAyDpiY+ernCckLiKhuNNtc+WFtrCoQ+qmecPHaOSd9icbe9d/FgnatxzKeekqp1V1iLw4KY/CX2Rbvy/q/jN7Jic2Cw2zmFXAAFE2S2T0q37yg5cJoKzFgZ4ZDfRSBfYkRFPdI6V1Rx+fa6hu62lcLEcfGar+uytLk7o8ZyilxhXBTQwIHIXwS55smN9f9Vge2UA+HbgZRAxjtvqLSyE6tac6dkEuQRWrSAvkPtEfqQ4tiGAlz2M+PcolbmVUMEeyAS3xVhzTBVylWcvAWmq85WN/r/6iqxG3Jn8uHg==.BsRopIPJXGLeD15A+OrZ0Q==.vIZtgCGHtwmAXg1vDLuniw==;'
    posx=46
    posy=9
    printmaze(maze)

    ####
    ####
    # Start from here!
    ####
    ####

    # Got Simon eyes and cotton check

    #keks['session']=None
    #keks['session']='session=z.J4TOy6C5abzak9Z9IuAyhIWWf065FoVQsxEJsz3fwKkY05vA74Y0oKAAph3tpSmJQBdGBrct3RuQ/cYpzecLFAOMXXBF+3jXnNUhutwdeMd0IIlEc1I0j26GW/CStuaPz91dIGanu2R3czE5GWdwoDoyUikAJaaDEMjtbDK2wd7BCF4+E6Tj4IEtz4frJscWRd/XjUkd/Yy3xcQtnx51PBj2ZBP11eSBcSP8ruxc6Xzl6K+CMkLxSpcIuC/Xvql6qODXndUIBit56o/BCRuAEySSeBa81/cayXVckin7rJmtutFrZxmmYA==.eCr7f+jKFUHvksAAAv5hkA==.rlB65FO/Xb+H+GhsEovpaQ==;'
    #posx = 57
    #posy = 7
    #printmaze(maze)

    # Got Simone eyes, cotton check and Old Rumpy, stehe bei "Old Rumpy"
    # session=z.z0AjCt9XwjnHIIYNtWEu4Sy6yLnDOSQnjDK03/W8E5df905Oe95nHMVEVpdBvlmN8c9L+EUi8OkwkvhhNwN1fnm9T67flRYoolO1GnmYaYJ7Mg6CiTrKIMf+sU9Yfo3r53jw/wB9H0MLDb9hIWjnydSRJLzThS2YpHJqfrQxq3KNY80g36TZN42AbsO6qXHxb2wl72Qk4a7bEheOkai50NJQRv4Y174LtqXmIe2xnp1lAyQXjDKL6v6QueFK64jhB+3UnKXnTDPiQKhtFX5+CrHbhtBLB8Q6KjV1/KundBfrxdjWTedTwr31wQoB2llJJifOrAmxI855uc1GF4AtZlQTdroHMe7mzni41skvFBwethX38VrOnU3W.9ay/ke74LDSnzm+ErcXxjw==.rFHFwgTs9DCDQ6RnJMiK7Q==; Expires=Tue,
    #keks['session']=None
    #keks['session']='z.z0AjCt9XwjnHIIYNtWEu4Sy6yLnDOSQnjDK03/W8E5df905Oe95nHMVEVpdBvlmN8c9L+EUi8OkwkvhhNwN1fnm9T67flRYoolO1GnmYaYJ7Mg6CiTrKIMf+sU9Yfo3r53jw/wB9H0MLDb9hIWjnydSRJLzThS2YpHJqfrQxq3KNY80g36TZN42AbsO6qXHxb2wl72Qk4a7bEheOkai50NJQRv4Y174LtqXmIe2xnp1lAyQXjDKL6v6QueFK64jhB+3UnKXnTDPiQKhtFX5+CrHbhtBLB8Q6KjV1/KundBfrxdjWTedTwr31wQoB2llJJifOrAmxI855uc1GF4AtZlQTdroHMe7mzni41skvFBwethX38VrOnU3W.9ay/ke74LDSnzm+ErcXxjw==.rFHFwgTs9DCDQ6RnJMiK7Q==;'
    #posx = 35
    #posy = 10
    #printmaze(maze)

    # Got Simon says, cotton check, Old Rumpy, Mathonymous, stehe bei Mathonymous (unten links)
    # session=session=z.HZjnLsuVx8oBeLZoNIB2U0waveH2kOPzrxNeR8UHDCrJksAmD9bJg8EiFG4iQ2UKX/rQ605tzuym4Znwx09IE35yPfzsdXsRCyQh62Um3QAUsDoY6yNH20t+iz/wppI4uIPymCHVcOnGPM3JU/BbmYH3o2SlnXOEO16BhJBgIOd/6CWTTGEHCIRIYkfltVBWdMfpVEB62i1aEbYotrn+TQrOgj5mXMyAs/F8TsCVhvsdaWvrvCdojCIJwWQltMwVKF3/g5Wpo/PZi1HtciqVawFJWwK0bsa+2skl0iSzrYPDlAKMekLHl34MziR7afI6KR27iQcx+BdByl6VfPo/Wm5vleQMRX3pu+PKfOJfm8VHzrLiLhBJ/CTqmmG9aJrdseiR57KdNtpb3AdPofh+QMEG52e17P267TbR.gtzNt2TXu4+1unT4ehH1hQ==.8Y9fxaq9pcbjxTUSqbRmoA==; Expires=Tue, 11-Jun-2019 17:50:42 GMT; HttpOnly; Path=/
    #keks['session']=None
    #keks['session']='z.HZjnLsuVx8oBeLZoNIB2U0waveH2kOPzrxNeR8UHDCrJksAmD9bJg8EiFG4iQ2UKX/rQ605tzuym4Znwx09IE35yPfzsdXsRCyQh62Um3QAUsDoY6yNH20t+iz/wppI4uIPymCHVcOnGPM3JU/BbmYH3o2SlnXOEO16BhJBgIOd/6CWTTGEHCIRIYkfltVBWdMfpVEB62i1aEbYotrn+TQrOgj5mXMyAs/F8TsCVhvsdaWvrvCdojCIJwWQltMwVKF3/g5Wpo/PZi1HtciqVawFJWwK0bsa+2skl0iSzrYPDlAKMekLHl34MziR7afI6KR27iQcx+BdByl6VfPo/Wm5vleQMRX3pu+PKfOJfm8VHzrLiLhBJ/CTqmmG9aJrdseiR57KdNtpb3AdPofh+QMEG52e17P267TbR.gtzNt2TXu4+1unT4ehH1hQ==.8Y9fxaq9pcbjxTUSqbRmoA==;'
    #posx= 42
    #posy= 18
    #printmaze(maze)

    # Got Simon says, cotton check, Old Rumpy, Mathonymous, Randonacci, stehe bei Randonacci (zick zack letzte zeile rechts)
    # session: session=z.pntnoC4/0crZAWhxXzHBA/MEDewORS3U+gr5995BS7BCqlK9uAy5vPCCsBMnEFvq/+neuvjVEyaFUMhoFZwxzpJErJpyrTqq0pcnJj0ZzpT565TT9gW5MxzxXb+p2iCJmjN/T5tHYQymowF9ABMZ/b3/YyTX/adtvmo+F5j1tLZzeqQqUkC1DS2wOHuODls6O9+Yiol8Jxw9KEO/8R+334Uj+CXkAMsB71DawFuXtIzspavP24G/HgR+C+cKN/2YxBFtOLIrUi7JwKoNyHuFaYD+LZbehww1FQNT2Dl5hFoMmJHUSNe+QiC1UV6h2qz75pPOoYe6UsPll2YFEiizpuzkds7VBvHnMh9e2YHZlprEAybSKbglHpJ0oOwKXqzk//1W0MzaeegqyN33648Aq+ng1Jr7PiRk35UWSa5teHYHwn3GWQeR/PUoEg==.Lo9ivUXEOsK8Ovq3t8GmzA==.pUVi6MrbfZnmR410Sdl6OA==; Expires=Tue, 11-Jun-2019 17:54:08 GMT; HttpOnly; Path=/
    keks['session'] = None
    keks['session'] = 'z.pntnoC4/0crZAWhxXzHBA/MEDewORS3U+gr5995BS7BCqlK9uAy5vPCCsBMnEFvq/+neuvjVEyaFUMhoFZwxzpJErJpyrTqq0pcnJj0ZzpT565TT9gW5MxzxXb+p2iCJmjN/T5tHYQymowF9ABMZ/b3/YyTX/adtvmo+F5j1tLZzeqQqUkC1DS2wOHuODls6O9+Yiol8Jxw9KEO/8R+334Uj+CXkAMsB71DawFuXtIzspavP24G/HgR+C+cKN/2YxBFtOLIrUi7JwKoNyHuFaYD+LZbehww1FQNT2Dl5hFoMmJHUSNe+QiC1UV6h2qz75pPOoYe6UsPll2YFEiizpuzkds7VBvHnMh9e2YHZlprEAybSKbglHpJ0oOwKXqzk//1W0MzaeegqyN33648Aq+ng1Jr7PiRk35UWSa5teHYHwn3GWQeR/PUoEg==.Lo9ivUXEOsK8Ovq3t8GmzA==.pUVi6MrbfZnmR410Sdl6OA==;'
    posx = 53
    posy = 19
    printmaze(maze)

    # Got Simon says, cotton check, Old Rumpy, Mathonymous, Randonacci, stehe bei grüner pfeil
    # Green arrow in map, everything explored lft of it
    # session=z.EtpKVB6IHasxDavlpgvV290VCK8h4nfa2rOrZp8tNaY4coG/xCzIPkdvAV0pG1mVFa8+RNn+WM54I6Uf/7t3+McHSNO+nAk10xyi1u0ccfDPnysDtR1LAZRjyLgTK6NSigwFNOWMbRLaoY31Ww54ta6ETk0EKQ5Hn6LZ7d7bl1SBQ0QiKSonWYIbxh2sIwD5pXdVGj4V/yli3DN99spybA5zkZdbvufDl568R0Oi9qclgggQ+b2UHp//m1QWgZpeij8S221SvJtr5M3qUPywY7T8sKcH7VwAycRwddDHHjtC6oh1hbOCgIA2fxy5hMK1UkBg/Wqu/JQfjGlj+Vkcl4tLv886CTyIrVkWsfkQYY0sNnvZA9Yr7c2zKCmMB/gtusv5ShG3QvAMplZFyV+VhPtTyubfIJGwiUq5oi4LYh24UAsj6sulxODOM3F1m2qbGsc3dgYk3HOBMoPlndHtwc3d8pOaC5e9WtMu/3dMNtexi9NAL76EtVu+RuIGYV+vg0VwR81+GLBrWK6o0T5yh8YOL1iTVB2ovycuKvFESYGqLMEm4SXgtJXAIaSqelZJJuezt9eSm8/svf3eIuY7v6CRT3PpLTbFT9FcWxHCCaOK1huREXLRRHDJQY9P64GEihARoDJu7cnnTPClcenwSlE9TSzl/SyJC1wn/jMTev1kKPkU4Np9+byFaBQy/w7R0hrR83kkARAqGNS0mtEHmnjZQvNU5aPerRWR1SMP.vnTs6yb2tZF4Eks7w8bM1g==.lCplL7c+9oznMrYA3kfVyg==; Expires=Tue, 11-Jun-2019 18:09:26 GMT; HttpOnly; Path=/

    # Got Simon says, cotton check, Old Rumpy, Mathonymous, Randonacci, stehe bei grüner pfeil
    # Direkt unter dem Hasengesicht in der ecke
    # session=z.W8LqJWLtr4cvkyFjII+vH2Sh2We4/Q+c5QwmMo6mYYjtcToONqG085Sjto4xzjeM9bRLIt4gJ3Yl6Lcsf7J7CotyNOSWIZotLu6ZM5z+MJOHubQ9zDMrd1ymu1bE/L00K3MnnQkF8rNUZeLN2S7m0nozHkdHwhsTpEN8wVY4GFPMoi8xXbGD3XBYwWsI9ujZnQU1/eN7LU+vgNzSfPBJi1Ilp6uJY6F3Q3/uvTTq4+It5sZcHNIlpvjWOCmTb7QDq0Gu8tFQYr6ckHOxYK8rcUjr1EaghTyuEOY2LH/4lcIuplN4EbHNhXM7sFABC4dRO8Hr7f94vLx5lrQqOfkMb6AULTPd4tYvWBOBc3csc5PIRH88vnho3EjZdJJOrzU0ugpd00PsjnsNJflmhfF/OlJewW8N/gr0bkAa1gzAb+osV3G9qkl+XMXP7ln+G7O+ZnjtQMqPo6wBqWflYM4Wsgu5x22+uOj+0kNw0JZddLIxiPmnTOrkqcfIy9iNtggUi8uhIcD7iRxvaHovvjE6tCawkHc6rfgnwDda7l54Bq6W6So2pLAFGt3wOL5cLqah98qL2SWbjgL/PlybgJB9IiENLxNa038pYXJTfIlu/2Q2ottlBnAqJ5BXJD0lznt7PljLxhGLqMoewzKAnheZbQPc77mEAhUhUt2DpyoKN/vV1vBB8Yp4H/6DIOyZSqS+YIMoS6L7LjXkV4+MCZiw0nJeIrsBBkIcqs/0iQ0nODBrWe0zv0qdW6oMVmk1aVZxNqrgz9Y=.w/ekekfOcORuSRcOSUTOTw==.R8oakd1QsCLWn0MYXgoTQg==; Expires=Tue, 11-Jun-2019 18:11:47 GMT; HttpOnly; Path=/

    # Got Simon says, cotton check, Old Rumpy, Mathonymous, Randonacci
    # Ganz oben rechts in der Ecke:
    # session=z.AVkvJnvUFo0c15DYabksLUXHrs7oRI88Mz6R+qTCQet5XX+bflMbD/T21ioI9lOKJsI1Ia1rzqjRSpjTXp6R6VUad9G/Vuo1yVyzBjMlvnM9vH5XClvFm37zZYcxoZeL98s3AjVGIEQMbnPsoLs5cCzk+uynNSnWXtr4EcJ2A1HZBd/6KNwtTc2OoK6noBhAhEDdeETcoSTeGn2N8IR8IDGnpv7TaxbH/XVBV2Cw7eOIIQchUMD+jig4yRVD0t2UNoFPtZbXodByQWpf/uaHSANwnrTLPJmfICS5uopr3+kEePq8JykzjsH3C624q4NX6HjnmTmtjm71baV5C2o4V0HvT0RhtgcnlhCdHT6x9QM++wHuBOeUf0beHaXooHf0ijwB+o41pr0jzHyjrfHA18bonWQ68nTaNycbZx1Mref7Xo/w9Hfh7OnIck9tWLPo371SSgidzx80cchL3Y8EUMjMpdfjdj5A+LQUGoI/tkNbXu+jVnZuL8IJXH9+QPrbyBcsEuG7zh3PMCjBs2YUZIQmtTtj9baUVm1a4VpxS6fnnB7u/6CLVYpmG0anHhOfxYnff3yHh4Oqr3IP+sA7/XGYaeEoO27F6aHSJET23vnv7FK0ViR3xDG5IXrpfKfqqBbobtTpl6bsC8e0xmUVM7sLVzBnNBOBZ4lgEGZ4CfLO+9nK1GAsMNOAb2B6FsCXKqGkKkZxm/LxuyKD7WRh98hNodQSY6fkEMGJgUtPnN9AL7KFSytYg1gw2n1EfsSKfH4Xu/LBD7WSpOf5uNK0MB9zfA28WXbjooO9MoKXzYPvQStXj2IsLe5QdgLVhuR0xoVrLOmrBBiLxhgfnW6767oBJ4lswroF2sCmLlC5dSq9uMHXRWaZlXW0fD8dx6nayINFAGvE7XNRnF6Zvv3z4eZ9DCILu4YnuE28Z+gZhmhJP/1NEC/udx4j+u60FqvXx+g0fuiDlUeCBnyEgvhdf/xGE68/LHETAD+tCMNQoijXFczSbT2QNML0i1a0PVxysPAFLBZrVoA5lLe83axRk3X2KbsWl1Zc1mOpcrUB03SMWaP57HJ/NekMosN+zWLgrUr74jhC8TkyY78Cak7UBejNZ36QoPIqT8E1dOgsQHId/oS6RZ+15Y6lD6aDeYyX6DqV4+uQLxxAmWddpqvynQaHn6vwaFY2fWq02lwxSVatPCNRD3FEjN9ToT2rwaJNQG6bllfevWNeu4aNUbFajNS8tP3aBEZHylvdisVOe5WJXr/hdr20MrJArC6vz9aA+hldIDwiomhP/Es/YEIIOGjYsyv8QqYGGJ9b4y+aZt42aHQgknVgYdqVvgLiVj9kmld9De4Lf0bWxgz9zTquvn0Ahk8nHno4AmK5ZXWoNyOjXvc4cSi6zdWpDIGUc9DDt4mZg/NSuaqgJS4HbO0zz3HOci57iGHU6ioxsfb7+rM9O2+4GiG0HcTnS8vsbR3fU90kNEsRRWxYDmHl+3t9+vEP0GdJ0FtPX7lEcwZFTb2vWKHzFeApGE8rD/67IzvXqCksv5mgrRXhkSwdDTXxWTl+vAkeTcGscNyIG/rgsHGR11tu6TQwVZkTXIrUuZkLYjfcOPWf46R9liAGz5JlO6Zug/d/pAV8E+rohsQaSfTqILYEY7bNhOxZuVWqVZ0cqWpEUdQ=.CoFnke6i+tDRBcVEFajFjg==.dO7/XK/nLKSoJ7oiQ2e8nQ==; Expires=Tue, 11-Jun-2019 18:19:01 GMT; HttpOnly; Path=/

    # Got Simon says, cotton check, Old Rumpy, Mathonymous, Randonacci, RSA
    # Unten bei RSA Challenge
    # session=z.dNft3fAhiBwTFdpr7tTfx6uLQQh43VLvnkapH4yyc0SttsmHfKhLxPoVDv6J8IdYDs6utaR5rgzbkvcfHE9VpasMK/4mxI5nq+oy0e8eLzvN3C8dRbuEtPJTcjxEG55hkWlf3v3UXmPajzJ3YokIeMasxp6cUD18U9i2jWVm4mtHfZMZYGhpXORPq5LEQAsjpso/EB2qo6X7uwVNU5SaG7kublzTrSJgBYt1s2BuNJQXFRjlbIyEbExMujGJWjf67b4UwX3Ccvl2L6FbepXMgEZey2iTqWGC7pjQhQC12orKSsHcPN2H7Gf80BDrSKDdD2XYRR8IlG2uuD4ju6DyRRNQfEdVWPdsvkuAHyfexsD25nhf7zhekRAwOo8b1sY8og4JOp7Tr2FeFb2UV2i/RXtIUFj9NT1ngRS6Xxa8jZQj7wz2LdHX5saoI1U7ScMWba7apW+rszGutsEGXNwT5M+gldkgOqFn2l1jEpx+QSdN8zO0AtvCq0HLxymagtqeuas1sbRkkctkRFyehPwQfiWyGmAtc5e0mTxE9uPnFkNUsdxpvBan6SJGg+cTnbCYNZ6OVcgvmvSvjtxDX/u1pV7qh3WUCFCtkibVPisgSFLLE9jwlQE95Zlkt4O4/zJAHNdb4jmm7dsbpHCz+fzsAnCEvXHuGu8YNy70NKHl7/SBM4QvCyG1PWjQHU3meSK325dmo6OtwGz9XmTe.8mDretYkBKbX5FV4ulz6Qw==.v5kehePJCfJFKosLsztzdg==; Expires=Tue, 11-Jun-2019 20:44:48 GMT; HttpOnly; Path=/

    # Got Simon says, cotton check, Old Rumpy, Mathonymous, Randonacci, RSA
    # Direkt bei John Sailor
    # session=z.WE/tcpn6Q70k6A7sGTbHDpZDLBEsWJeaf5fqre4X0R6INqLJvO3wdv5FDXx2VR+Zlqv0Wt9l6xjS+MTivzHJmImsJeAYYRw5+4jTrbT2b9pTelZrptj+MIoH3w/B2sxJLFCVvpunTjwXPmr1X6/eU5P2I5yGHow167VpV7O2MNdFEgh9lNCL6Etj5MUawzxbVLQSrOBy6ob7jcjgPgk39mWSs486rlF6N0i475BB/CMWvI1Et8BxZRwV4YKf3k+/kbmEItSmDEcLgm7/ao6LmG5ZHfZAIcykJl88NkfXJwmMlS1zxkiVBGCsdrKdPDBZLu0Iq4yqeE4Zqz4b0GtFB3n87VKbGCPYHdWHrm26wlyFpFG3M+thWqkxpCvowQ178lFHHMeodN2iB/yCrW0Sn+g8t0cKQ2keJGg4bQf94Qg/H0yJvEsYHSFY/igM7fqRSEAnLKxkfjFjk4jQc9GOF0gje4V1vcuX2FNOP8+uVmn7BBu/ApSf0d7e11Lc16W7I9buJEoj172TO+KkAJrXQ0j2syc14VIoUp2m9yUJm2HVxCZ4RBrbmtoz5LqGFZr6lAQaANhQ8tm5Z446PD/L77UziCsvgWmDyrZjId5O25Q5x9xxgJqQsm24ZXfjf2ufL5L6OPmCn8LyZxPnf+15hwcFg55jw8JJBrVPfS8dwwF3epMGApUCOOK30Nk4pYOMOIdxu/5YBPF8X6eMVZ5jxD74t7TVsoU=.H4AOnd62k0LpHmMKR5kKAA==./sfFItlB9lxKsp9yRqARew==; Expires=Tue, 11-Jun-2019 21:02:11 GMT; HttpOnly; Path=/

    # Got Simon says, cotton check, Old Rumpy, Mathonymous, Randonacci, RSA, Sailor John
    # PW = b4ByG14N7 / GET /?secret=b4ByG14N7 HTTP/1.1
    # Direkt bei John Sailor
    # session=z.+2/dPDEGxVjeYkl9jaafYcSXAKoXh7apVxAcvFutBeBcOWrlKZnWDtDNKJx6TNVJ996ws8HmtoVCPLUkbeYsp+xQt7T6mWP1lb0SUMeuyKs1t0bCPcKi8H+2kwSQQFVv/V3/LFGqzZnXAMo1PLLDyXPAa9OwiaBSS65RdTtSwDn7h6gTq8xGhW/+8FI6iyrw/fFE5WQlxwSNAMI4xkK/V707GwFsDBOTSFZP4PTsa9cFYXvod6s4hs/cpSZmJssJzkHPlDx2NgcuIcOUfNXARyb/FZLwIwRiXJ0zonSwPbgbbUxD92/oMqViYOyR47p149f7q4UlZrykM1EjLU68dyMGGAWj39Nxtn3QEuT+tSLMdHa3x7D38TwIhn0PQfOoihJDuY8eMCLuW5ecfNe9B+Yx+l9q2Gpb8FJQmfr52JgurzP9wQ/ITxCpMLQX5UvM18UgqzyECFi2l3KBAkP5soqX+Zx/tdNEDAg9MwyjUBnStVqwEWtCxrI41J7LxA0bdp5A/rGuF3Jo3SDq4CLZCX3R2XvniDcnVcJKmMuoCL0RkFDgzUtHj1u/MM7mxl88HR+EjuEtsYi2DTi+vy7uZH5mLLTFUMw6iX4Ib0Fz0Fia46a15tyIddZVjFwOtauwr6PbDpu9EHxrjlzGxqNSPdfBkB7Bj2i+E91F8HDHVw3jFQjrDGmSFduVXgChawz92B/eVyTVhmAGXWuBZ38Ja0XtFvaSFxtdNnQco554cJgVTbyF.2MydHCzOde8PjYBt21EPLg==.Rmvahz9LANnppR3cBE5Qjg==; Expires=Tue, 11-Jun-2019 21:39:47 GMT; HttpOnly; Path=/

    '''
    John Sailor
    
https://www.alpertron.com.ar/DILOG.HTM

erstes zahlenpaar:
-------------------
base= 71140253671
Power=419785298
modulus=17635204117

Find exp such that 71140 253671exp ≡ 419 785298 (mod 17635 204117)

exp = 1647592057 + 4408 801029k

print(hex(1647592057))
x1=0x62344279

zweites zahlenpaar:
-------------------
base= 9125723306591
power=611096952820
modulus= 1956033275219

Find exp such that 9 125723 306591exp ≡ 611096 952820 (mod 1 956033 275219)

exp = 305768189495 + 978016 637609k

print(hex(305768189495))
x2=0x4731344e37

concat 
0x623442794731344e37 -> b4ByG14N7


    '''

    ## at bun bun
    ## with Simon says, cotton check, Old Rumpy, Mathonymous, Randonacci, RSA, Sailor John
    ## session=z.wfNj7SW4H0pML18QD4eI6OVrqctLcgHxW4Z1VC9Qag0ZOIR65+LiU6+ajBFY+5v7q2DEwmx/tq/Zs+JjpnLqoh47ymMjEMPkBmZ6ya6y30uxHvzLfa4RILftRqYHOkXSO2224Py3cuf/oUk8e7PskKNlolNgfGAR+Q6SYOZJzhU9suWUERiW/rmgLJvIURSSssRVHodpB3WIx9HuwS7HY9bZLY7Q0VUHVFVAzgrn1cAssMUc+vpCxaK5AMhMuthQrCjjpmxYdz0JWWslc1EOYEKPZIBnGnEzvyaJ+v7OGaZ8/D10WWaKf/f7K0WR/4dMALs5/FIcv2+xYVVm4X8B35twdnLR+iVRlPAOw6+3y3ZBUNa7eJNJ0nuYu4K17zS4wZXoLFeEjXhlNSHkh+oN6ToGtHYx5iT5xX4WcmhoFa4Zu3jxSfn9Q0eBnB2l+fqJO/8p7b71wSzAS0NpHqBhwsg57lmoi8dr7Gx8nr/La/HctOpfkS62BNUvstryiScNumD9uRPkxhnXS+GVst6jAb6kALhXkrNQNwaa6oz7xyn4PyZXW1vYAcNSK3N+eFyxiMXdnICjiPB0uPyrlSMVZjTZKDKfqMkcvncFF0d7NtDb/fIDyaabjc7XGnivFr+ptiq2kyFHsMBfgK3B7Q64y2A5jEhIMu++zp1LJKuv5/Dw//MJkTAZ69DqgyG6L6ywHnaKiOZLXtnR0VxzZaKdMP7c+hjmjh8we/+M28ykBu8BJ7qM1+X9l1co5oBN6PFluNEPmGVOqhcBZLBr/e+Z648lH14lzqwQ7Ox9v8j4Ycjp4rNG8gi4G1dVkNJ2Gjdlno4dMqHJ8D58rRA7hjLrlGrCNDaSRwTgr8noE5vkfLWc4nkfx1IMU17S5OepZYsc5djx59cQls8GPzMEFZToP+pBbYfh06sZ/c0VTiUzIYQi8NdtcM30sz/b2Zi1y88f2bIFZtcjCbaxLkV3.L8VPl2Pn5iDdvU080wgSxA==.rOXmxMwuPg5j4OeqRnoBRA==; Expires=Tue, 11-Jun-2019 21:47:31 GMT; HttpOnly; Path=/


    ## bun bun goods. es muss ein teabag (buy something for madamee pottine) gekauft werden
    ## action?watch macht mehree 302er man sieht im header was es ist. immer wieder cookie schicken
    ## sobald der "teabag" kommt mit dem cookie action=buy aufrufen
    ## with Simon says, cotton check, Old Rumpy, Mathonymous, Randonacci, RSA, Sailor John, bun bun goods
    ## session=z.u0M8Ggev+04OQN/7k51q7zX89Kto//HFjetwtLYqEnXk0nC8hEJZBjj5bQNh6HOEZY8kO282BwUK5xMM2FPxzLnVEPnP2udMAgXL61s9uO9cVo+WHGw57kTlsYiWHbxdo/fvYCmaTCEQet6oFWayDk67Jd8pLpfwlM+c1VoshkK8mAZCZrKb4W/8G4gEIET00Io/buuqfYHFgDb1p3C1zCuewlnOua7sHW97yUJwV09t+DwesHYZaI/Dm5S36Kk5gY1Gr3A7Vj0fICWhBRy4PdO8hKd9ExNt+EwD8rptsIhkhrb1hhqTcbTkztOHq0sii+e6pgWKr03DO+TPAvM7DjF/WNMEpkpZ10G8Nr7sj1EsMUeOwMvPNXn3q1xOT166B3iPreVGKMqed71hTdk1ddhNOBRhnGMpUADB8Y8S8BtlhrVBUrnfy0uvNSYJyKxTHWK8jH7QWMoRBJpcUThmd5nZ/wE0QtyidXsVGVCGKTji6pMTXyubgcoR2Osww8IcMEy+o4CMca5NVQy5iPtBiUzg8nfmiN3mm31tI9mTNkE/opPSOM4zLfNZY38jBTKlwllwE/qwne3aYKiNZpEmxqxlZ8z0LxX4r2mZZZBCp4jw4q34yj9gJe50hUsdZmBYf0+X07bMSEZf1VDlldqzaUAJRcifp9yAhxrDRkA33dmoLANGsvJvijrJJNgqWK5ZzuByhNIF1067wUn6+p+PfpcNyRt6Qb911z2gjUwv577BVtY8hX+ViK7VuP2MOWC1eeXH49QmZl4QyVRRJb9h+A==.g7ZWV9gf5h18My1tHKFQLQ==.DS4IIepIfDf7AO2kf7XcQw==; Expires=Tue, 11-Jun-2019 21:53:50 GMT; HttpOnly; Path=/


    ## am ziel
    ## session= session=z.jq9MEoDqemPhFsQHEuT6kLfz1lndXofDScKlIhHylakkCDkgGyrnSriamtwnbY2Vik/vH57O6ddmIfnU+MF8pHzrnB5BpAEJ8nF5FM5lRK/gR05QPFU4ayCbhZavBYJWsdirFI7Vy0xGFEPJZn3zu8I/aHFnEZ+L9zLMl9+97qe2gDik8/HBU5ylrANGH+QzHncPhWBKiqxSh+phZkhuWijbshYIYEYrQQWvDRnNpnUG+Nxwimkdf5PqP3sZwgKLIq0ubAKbgD3McybVIFqGNIH47OM/dEUAQEEvvPOZzJJsNaeqa+jfPJ4MFbs0fXXpWM0RyY0suvOuEniP/7z+P+1zlWlbnNAIjcvYrjSTF7WE/AbDTxrhEs8rdN3jqGSt1eLhmdtbOwUdT5VsT9T6PDtTeWscUU8ZWXUDAzwIBe+HsHHw7F5vhx5IW68jnda9OR9Utt3B0lsLWbZ6clnlDdoORljXxVU8z0Ri2RzKcrtKqdFxv0mLfRDp6QQmLXQiFDTfQmt2P0RSRT9iw82OyTiqDrRTeznqQhWvIWy+emQPM3W6qlht10I60pZcS4iClgDF5czl7P1gYzFGdN1FNvc5pkfuo+ml2Lju0RjD+28BZob0Vsl+cPPn6BiWurPnsDD/HLCROOp29IOo0TDoKOusGFqzzFL5pgUo6f86OWdNwhQroRXNngeJFdCkf5q8Yt7gA2EJ9e9txyZ4kdt53z3Bruf2Q2z3pIFNDkog8pKLvWMhAwzt0JD8jOJA6e1Xw4+WiHzpmxM5M+7d0M7PUKAiu0vkJ2dfm+a6guoRlVyWkO9p1fT4Mf213Ek=.JvNXZWA4r+hhdhHdOTqMMw==.6q2EaLxk4dR7G/ySxMCAeA==; Expires=Tue, 11-Jun-2019 22:01:41 GMT; HttpOnly;
    ## Javascript bruteforcer: Code is: -9 2  4 8 6 6 3 1
    ## other code: -8 -6 4 2 -4 2 8 -6
    ## final flag 22: he19-zKZr-YqJO-4OWb-auss
    ## final flag 21: he19-JfsM-ywiw-mSxE-yfYa
    ## hf3: http://whale.hacking-lab.com:5337/bf42fa858de6db17c6daa54c4d912230




    #replay(FROM_TimeTravel2ShowThePath)
    #
    #At Randonaccci: X:52, 21
    #keks['session'] = None
    #keks['session'] = 'z.pNuF4+Rp9ZWYfEoBd/cWAbPs2aWbqESDS8SwsWeKDlZFh1vdXVVdYAmjRM9j/fDYN950tdHA0X4HP8GxRyGDh7G+rwRSBwnVOeTPg3M5C9m2d1O+txg4VkHeoxHHg2YFfe+c353xK7yQ5HKbyZqWykx5aOAy2F3i28FSrEoJPUz1TjOjrMvMvy/69o0nnyHz25GL8t2WO2FiSZl6iXhmi9vkh3o1WqW/Ks7DL6htfcr2fG9mOi/AWrwDqqK3M7tkpStI3DCMHVNjawZFbhCCNKI1tA7IjtnbJwZzgVwHJNxn612HBWwrAim+OEZJuCv3l/tVzj2YV0mgn0Dxy+meNIvFe/Sx+RXFxaJt/H3nlysvegPBu+KAvadt4r3BFxFURtic0PQ74R9BBXK7KCG/hJunBP4Sw3inqkWaRt5toinWystmyHGCDj8j454Tw4zUtjM8i8LOWOcSf5rVFn5WuoJhecGU7rY508fRUUapdEGm+OgZsFA/Rl7t8Q5oEJ/zG8mg4I0XpCEk/UxW03RSVulElDJiP6KTPghGLut8wgKhKmjbWBoB9a54r8PC90RVxkrGY6QEqsESqKjOIDA1QMR8rHZR/GEBQUJgqNbeftWkiC0sR/XlLZodw43sD/6a4nN8Gq3hvdgyAyz982+7EoQskFQwCKmdpMeulUTTAEZ85u00+UddnCVVnkS0faDITv/5uWqZSYO/G0/K125H6Xy7y7kx81skOtexFLaGv2jqZjKpZokObAUoaSRIHwVlSQLb/0ZO9fu9CeFyE1fBSX2SfUE0puTatjYBUOdn10F+PRBBFKurn71sQiyr2dEgK8/niMNbnXi1Ec5JBoeh4/bs8/NrDJIPKu0Q0Pcur4mDo+O8C5zNF931tyM7OYjx8LIfOWXG6paiF9tk6QueK8d1XJbZYP0Wn/sdipFDX7jXG3ZdCjVq7oBbgsltJTLzRs7mhwU8bG2wZj4PwfpPB/nDFfDHPFhV6Wl2qI1T6lOLyJMl5Xy0TsyIWCRnGL3cKg+6b1r2MxasbXKXmPxHoCthVVK+Ivpn8WLis9j2jLiO77bmbQo5bJrIv6z3lXC6MmG6FVsLENmXLFx1F5qEZldJFcsG95AphAwGzAY0UkjnkNKGpczaTNwbXBeaBBijENYo/86I1M3S+SBsVpUApjE0ZghtYLrjgphr4IFhFqt6L+9zmIfXhb/5JfH8mjZ5Ff7GHkLUIdzSfqOdnq73KMln7UWYyL9chtc=.DRJvIfkuFb84kya3NrcNBA==.92B3etMAcsCdYdtl+KqD7g==;'
    #Expires=Tue, 11-Jun-2019 11:23:09 GMT; HttpOnly; Path=/


    #replay("lr")
    #solveRandonacci()
    ''' Solved it with this cookie:
    session='z.NwQhWmh5Kbl4VNVsIzx4YD6xrrLPjVq3FOCk9CFnqOv7LSWLSaP4wrOjnvPyvFD1DySvQ+35PBzY6LAs/4UGUEkyuww22aWRkhZvSPJBm41kpd5zZBHWBHmQrp/FMAgjxA7cngirr0OJ0B7gdw0RBWmja3WJwup29qsN+XtV5XYcv39ZO/9GJk4VDIjDeKCeVt9vARHRbIwTt0wRt0X+pKSFjyARr732kbw/gjpfVfD3ZCydVIjPOtOYIwxIVp/JW1P8EIuR4w8CBbNcT87UJhxDgvyCPt6cGXBs7M95oD2j05Fu+ZSaVF/zCXoCbiO4c9ar5BiS/JyCUxV2qMnKd0Qqx9EiDSU7mMSfZiQM3gUA9B+wqvLnkRflA+coOnvE1YSb9TJXM0d24CdiDY3eoq28RSEXADyHbzcj.JtrGUXoxLhDUvRXHPDWPJg==.C8pCM/vAcJYDkre97MdB8g==' #; Expires=Tue, 11-Jun-2019 15:23:26 GMT; HttpOnly; Path=/
    Position after solve: X = , Y=
    '''
    #keks['session']=None
    #keks['session']='z.NwQhWmh5Kbl4VNVsIzx4YD6xrrLPjVq3FOCk9CFnqOv7LSWLSaP4wrOjnvPyvFD1DySvQ+35PBzY6LAs/4UGUEkyuww22aWRkhZvSPJBm41kpd5zZBHWBHmQrp/FMAgjxA7cngirr0OJ0B7gdw0RBWmja3WJwup29qsN+XtV5XYcv39ZO/9GJk4VDIjDeKCeVt9vARHRbIwTt0wRt0X+pKSFjyARr732kbw/gjpfVfD3ZCydVIjPOtOYIwxIVp/JW1P8EIuR4w8CBbNcT87UJhxDgvyCPt6cGXBs7M95oD2j05Fu+ZSaVF/zCXoCbiO4c9ar5BiS/JyCUxV2qMnKd0Qqx9EiDSU7mMSfZiQM3gUA9B+wqvLnkRflA+coOnvE1YSb9TJXM0d24CdiDY3eoq28RSEXADyHbzcj.JtrGUXoxLhDUvRXHPDWPJg==.C8pCM/vAcJYDkre97MdB8g==;'
    #posx = 52
    #posy = 21
    printmaze(maze)
    # At Mathonymous
    #posy = 21 #ca
    #posy = 43 #ca
    #keks['session']=None
   # keks['session']='z.ymPcp9yWNkpMvv5vFLbnYRwOO+8xHZRAaFHkrpV4LUTGrsH3ZlcSG+lNBzGZSsKvHKad9kbq89LS7VNjI4GmFHAR7awFlbMdG+FIr2/KH4DFj99XvtBtqT8uJ0y7kbEnPEcic4YxRMTiePo8B0SMKUNwV/uv/Blp5myE/5TWPYIGPpvMZ6kHGpQLLERBdbjzVxdByhWYEfNLuPBDYmMBsi2uboROVR1AaL/3y+Dv4WULigbUMI+I6RlUebwDpz+h4hepHmMlBZmQtYkHmE9R6zqL+Nctak8R0V3OBJzGzZf6ShFaUgAlljPwMURXXJuj7hLS17bZNEMI0vqcmaLxjNPKkq5Ocx8HOAXSow+mFAXRY8jXr5ls5mvTw3Y70HsKYnzVcaiseUGufWKZZZFOeJniSIATh9eXhALgxK0aX/U0N10CsZ9+bwEE3MeF.aAzt82fV4B0RcpLQzJsnPw==.Ga++Y0jEw/xnLFpRdZoZoA=='
    #
    #
    #
    # At cottontail: C
    # session=z.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.tzAFn2js+S9gDTQ4llWB3Q==.H6dGVxPPSSV5UvXmfbi1SQ==;
    #solveCottontail()
    # solved cottontail:
    # session=z.yeDGjgqgXvmJRc0uDANQp2dRqGe7G5Paxvq3juHn2MZW4cmq3vXSuQTMTMgNVih/nZxPUDzkeLFSwTraL+Qp2gSfeueleYh/+4Hju7nUXIP3T5UUF0S1lOQ736RtTqMtUKVwwto8xaAMfBKniXXYivPbZEvjpF9i0JvRlSf7Wou5Z3+lBvgkXvHeP6aF3qPMOV4k4hhMHHRVYxYo7lwY45wqDLKZmKRBMWFKwledU8auxLix8WgG2VPrLL1x7R4ELT2Rpyfe4gYKgHlETqFBkNc3YVw4w5g2HIpU4EuZobR4Y3Hn6Yy3aFM0Pm7KFUJJLZRlp48OMG0bR3t0UOB+ETSmQ+1kA7AOSBhLoVnREwP8K4qXhgJBlacFjEXObepJgwGqqaT1i0jofK5RIZ0zjYIL8YaQ/v8nAiu6Yc0u5Cfi/tSW3bLSsvlR3uouTDMb7sngAH1LL0w5fk7nJBT5SqSSm8GVjxPM448MP/8v0GCKfhmmoX68+yYqzscvDYsU0f7z7vwcpDwqy45OHjZm/AD8Zl3ew2Q6ioTLx20nBU82dpCYh+fs9AN/NabOcqyv.a3BPtZdOmWJ+HC/ZuZ790w==.uj2/VGc4CO4UWrTf2V33Zw==;
    # oben im langen turm
    #
    # D: "Bun bun's goods & gadgets
    # cookie:
    # session=z.sGnwyG3EpYC4iF3yz8/mKqas5cWeKUrY8bzvmPgOsBDF6D0tXcnO5Jw7pkeGhBeIugOuW1FAN111O0vIM3QBQrY+MvrIADdY8Cl8n82VAPdhuVYxICd5pXF/VlXfBqS/daW4FU8C7TIQkD2FeLDjlN43PNKI4QQjw5B9+kXGNbUTnhQk2MjgKR3BtHsaIiWmkj3jAlOkLZZrvbg/YNZusnQWZ/23XuX4vUsFDq4zQ8GmEwHbxXEBKAX0QSr5M6aiAnzbWImI8BqiJgAHQJHe5M21jlmriO0mGurz/yFgbwAcuRo6rQpVVk2cUe6HoskmV8ZyaE5eIKMwFgPKFm91Hc7zQTBQoUynFSoNaCAXoeLnBQW/yTCb60PDSuQMV/cBYJix/YI5IQFQ41Ek9nbjydkCM2QL90sc6Wv3hfo94jUe4bkORXJ1iXvV9TNRnqosx/LtzXv18wa4H1oXW45AY2ZnliDvJYXrXoVkI9EQXovnsgbUhTY48T2FwPFso0gRiE9St+JJulxeiux3Wrm7qOjItEWKnEUr2NQo7EhT8I9gD/Iv+tYC6xap6pVhMgR29Sk+4QsTO2JMKCEbF5zwj7FIolHe5VnIodynmCWxPYSDwe6cdjj6Qj+nU3vHKjZpWX6OuPKHgkkjsmGJrahiabNz6MiLfk2WXMvC4eUxzzt/Tbz5KTzpTC0LNnvLwgNYe4Q6n9gTCq6zinWCwQ+1YXaqXdnstqDVpCq7bJqNNL/kunOlARDVn4Wc8z0RvqL8.vvckZQYNGiwvKJaficNmCg==.hyfnQ6mUfh1RwTU9gAIJOg==;
    # on map "D"
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
r = requests.get("{0}/7fde33818c41a1089088aa35b301afd9".format(URL), proxies=proxies, allow_redirects=False)

keks = r.cookies

# Send format string exploit in username

print("Starting game")
#init_maingame_loop(dimx=80, dimy=50, startx=2, starty=35)

init_maingame_loop()

# Orbit mode: URL = /<md5(p4th3)>


