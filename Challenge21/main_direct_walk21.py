#!/usr/bin/python
# -*- coding: utf-8 -*-

# Beware: ugly code ahead! I'm sorry! I'm a n00b with Python

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
            # Check for challenge 1
            if "Are you ready for a little warmup to get your most important sin on focus" in ans.content:
                '''
                <div>
                Weeeeelcoooome! <br>Are you ready for a little warmup to get your most important sin on focus?
                <hr>
                <div class="d-flex">
                    <img src="../../static/img/ch11/c11.png">
                    <img src="../../static/img/ch11/challenges/4f108aa0-ca6b-4d35-b1db-7d2276510dd4.png">
                </div>
                <form method="get">
                    <input type="text" class="form-control mt-3" name="pixels" placeholder="[[1,0], [2,4], [8,1], ...]">
                    <input type="submit" class="btn btn-info my-3" value="Send">
                </form>
                </div>
                '''
                # Send "[[1,0],[2,0]]" as as response
                ans = requests.get("{0}?pixels=[[1%2C0]%2C[2%2C0]]".format(URL), cookies=keks, proxies=proxies,
                                   allow_redirects=False)
                keks = ans.cookies
                if "You solved it" in ans.content:
                    print("Solved challenge 1")
                else:
                    print("COULD NOT SOLVE!")
            # Challenge 2
            elif "C0tt0nt4il Ch3ck V2.0 required" in ans.content:

                '''
                <h3><span style="color:red">WARNING!</span><br>
        C0tt0nt4il Ch3ck V2.0 required</h3>
    <img src="/static/img/ch12.jpg">
    <hr>


        <p>You need 10 right answers in time!</p>

        <img id="captcha" src="static/img/ch12/challenges/c5e46545-8f6b-160-b7ed-8adfb87d78ee.png">
        <div class="py-3">
            <form class="d-inline-block">
                <input class="form-control mb-3" type="text" name="result" autofocus>
                <input type="submit" class="btn btn-primary" value="I got it!">
            </form>
        </div>
        <code>0 correct answers.</code>



        </div>
    </div>'''
                # Read the captcha from the URL
                cnt = 0
                for cnt in range(10):
                    regex = '<img id="captcha" src="static/img/ch12/challenges/[0-9a-f]{8}-[0-9a-z]{4}-(.*)-[0-9a-z]{4}-[0-9a-z]{12}.png"'
                    hit = re.findall(regex, ans.content)
                    # print(hit[0])
                    if hit == None or len(hit) == 0:
                        # Send anything
                        ans = requests.get("{0}?result={1}".format(URL, 42), proxies=proxies, cookies=keks,
                                           allow_redirects=False)
                    else:
                        ans = requests.get("{0}?result={1}".format(URL, hit[0]), proxies=proxies, cookies=keks,
                                           allow_redirects=False)
                    keks = ans.cookies
                    cnt += 1
                print("Done?")
            # Challenge 3
            elif "Mathonymous" in ans.content:
                # Solve Mathonymous
                print("There are multiple correct solutions!")
                regex = '<td><code style="font-size: 1em; margin: 10px">(.*)</code></td>'
                hit = re.findall(regex, ans.content)
                if len(hit) != 6:
                    print("Error")
                else:
                    n1 = hit[0]
                    n2 = hit[1]
                    n3 = hit[2]
                    n4 = hit[3]
                    n5 = hit[4]
                    n6 = hit[5]
                    regex = '<td><code style="font-size: 1em">=(.*)</code></td>'
                    hit = re.findall(regex, ans.content)
                    should = hit[0]
                    all_res = mathonymous(n1, n2, n3, n4, n5, n6, should)
                    for val in all_res:
                        print(val)

                        ans = requests.get("{0}?op={1}".format(URL, urllib.quote(
                            "".join([val[x] for x in range(len(val)) if x % 2 == 1]), safe='')), proxies=proxies,
                                           cookies=keks, allow_redirects=False)
                        keks = ans.cookies
                        if "Your navigator says this is right" in ans:
                            print("Solved mathonymous!")
                            break
                pass
                # s = mathonymous(n1,n2,n3,n4,n5,res)
                '''
                <form method="get"
                  oninput="this.op.value=$('#op1').val()+$('#op2').val()+$('#op3').val()+$('#op4').val()+$('#op5').val();">
                <table>
                    <tr>
                        <input type="hidden" value="" name="op">
                        <td><code style="font-size: 1em; margin: 10px">12 </code></td>
                        <td><input class="form-control" id="op1" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 19 </code></td>
                        <td><input class="form-control" id="op2" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 7 </code></td>
                        <td><input class="form-control" id="op3" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 17 </code></td>
                        <td><input class="form-control" id="op4" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 11 </code></td>
                        <td><input class="form-control" id="op5" type="text" maxlength="1" size="1" style="width:40px">
                        </td>
                        <td><code style="font-size: 1em; margin: 10px"> 15</code></td>
                        <td><code style="font-size: 1em">= -149.42857142857144</code></td>
                    </tr>
                </table>
                <hr>

                <div class="form-group">
                    <input type="submit" class="btn btn-primary" value="Submit">
                </div>
            </form>'''
            # Transporter
            elif "Myterious Circle" in ans.content:
                # Teleporter
                '''
                <div style="height: 200px">
                <h5>Navigator says:</h5>
                <p>S̶̡̛̛̰̠̩͇̯̮͌͌̈́̐͜o̷̘̼̘͍̅͊̊m̷̲̼̰̙͓̼̳̺̃̃̐̀̕ẹ̸̘͈̲͕̞̏͌͑͜t̶̠̱̀ͅh̵̨̛͎̘̠̗̥̣̱̠͉̓̂̋̈́́͗̕̚͠į̶̛͈̩͔̮͎͉̥͔́̋̇͊̾͋́̀̕n̶̺̈́̈́͑̅̾͊̕͘̕ĝ̷̩̲͓̥͉̤̯͇̐́̀͠͠ ̴̱̩̏̔̿̆̈́̿̌̌́̚s̶̮̽t̵̨̘̠̹̮̖̎̔̀͗̐̒̕r̴̢͚̠̘̪̤̺͓͒̋͒a̸̜̋̉̑̓͐̆̓̕n̴̡͚͚͉̦̫̻͋̌̇̊̒̔͜g̸͙̳̦̘̅͜e̴̛̮̹̰͔̬̖̞̱͎̭̿͌̋̂͠ ̶̰̮͔̯̩̩̲͇̃͗͌̈́̆̿̕̕h̷̢̨̢̢̞̪͆̎̉̽̆͗a̷̺̍̄̐̔̑͘̕p̷̨̝͙͇͙̫͖̌̌͂͋͛͐̌͘ͅp̵̧͖͈͌͆̔̑̇͂̈́͘e̸͍̫͇͗̈́̚n̵̡̧͎͉̦̫̽͗̔̀̍̋e̸̢̢̦̙̟͍͔̱̾̈͊͊͝d̷̰̺̟͕̝͋́́̈.̶̧̨̛͍̺̱͎͖̖̭̪̋̿̓̀͗̌̃͘ ̶̨̛͚̰̖͕͜Ȳ̶͈̻̤̥̗̔̊̚ò̶̤̩̝̗̘̗̾̒̾̂͠ú̷͍̩̲̯̟ ̷͇͔̰͍͙̖͖̙̈͗́̓̾s̷̡̨͖̩̹͉͜͠ȩ̸̢͙̰̳͌ĕ̵̪͋̔m̵̢̨̼͙̼͓̣̟͒̈̆̽̌̉͆̊̍̚͜ͅ ̶̨̝̭͍̽ͅt̶̡̜̹̬̫̞̳̮̽̏̂ͅơ̴̢̩̖̤̎͆̕͠ ̴̛̝̦͛̊̾̕̚͝b̴̗̂̒͌͐͘͝ĕ̸͕͂̿͂̓̈́̒͒͐͛ ̴̥̪̫̺̫̯͋͒̋̈́͂̔̆̍͌͜ă̶͍̬̳̮͐͊̀͊͜t̵͔͚̤̳͛̈́͛͒̅͐̈́͝͝͠ ̸͔͚̮͉͙͑̀̇̾͗̓͒̀̚͜ạ̶̟̤̺͈͑̋̕ ̶͇̳̤̬̌̔̒ç̴͍͈̠̪̳̹̬̰̜̄͋̈͆̎̈́̇͂̀o̸͚͎̝͖̥̳͔͚̗̍͂m̶̲̗̭̭̟͔͙̍̈́̀́͐p̸̫̱̥̞̈́̃l̴̡͈̹͙̲̠̃e ̷̰̘̝͐̾͝t̷̡͍̫̼̜͚̣͋͌̏̑͋͗̌̔̈́̕ḻ̸͇̙͉̞̲͙̱̌̈́͋̽̄ŷ̴̦̭̪̬ ̶̡̡̱̦̫̑̋͘͜d̷̢̝͉͉͙̺͖̦̜̑̾̆ĩ̷̪̬̹̙͇̲̰͑́̔̓̉̑̚̕͜f̷̨̡̮͙̮͔͓̹̄f̶̥̝̍̎e̵͈̟͖͓̺̩̱̰̓̌̋̌̃̄͛͜͜͝ŕ̶̛̗̳̤͙̼͉͔̫̮͊͆̐͋̂̕e ̵͓͖̠̆̓n̵̬̂̉͗̓̅͜͠t̸̨͇̰̘̘̐͜ ̵̣̳̹͓̫̮͎̻̙̘̈̂͛̏͆p̴̧̨̻̹̻͔̙͙̠̀̾͌̏̈́̾͋̏͘͜͝l̷̮͈̖̯̣̟̋̚ã̴̢̢̑̓͘͝c̸̜̟͙͊̉e̷̻̐ͅ.̵̧̡̘͈̱͆͗͌̊̂̾̑̇̚͘ </p>

            </div>


                <hr>
                <h6>Solved:</h6>
                <div>
                    <ul class="checkmark">

                            <li class="tick">Warmup</li>

                            <li class="tick">C0tt0nt4il Ch3ck</li>

                            <li class="tick">Mathonymous</li>

                    </ul>
                </div>

        </div>
        <div class="col-9">

    <h3>Myterious Circle</h3>
    <img src="/static/img/t01.jpg" alt="logo">
    <hr>


        <h3>
            You feel a heavy rush of energy...
        </h3>
        and in a blink of an eye, you seem to be at a completely different place.






        </div>
    </div>'''
                if "and in a blink of an eye, you seem to be at a completely different place" in ans.content:
                    # Strangely we're hitting this square and see the text in BURP but never make it to this place in the code
                    print("You got transported to a new place! (Press any key to continue)")
                    waitKey()
                    # Reinit everything
                    init_maingame_loop(dimx=40, dimy=20, startx=20, starty=10)
                else:
                    pass
            # Pumple's Puzzle (still unsolved)
            elif "Pumple" in ans.content:
                pass
            elif "Bunny-Teams" in ans.content:
                pass

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


def mathonymous(n1, n2, n3, n4, n5, n6, res):
    s = [str(float(n1.strip())), '', str(float(n2.strip())), '', str(float(n3.strip())), '', str(float(n4.strip())), '',
         str(float(n5.strip())), '', str(float(n6.strip()))]
    should = res

    for op1 in ['+', '-', '/', '*']:
        s[1] = op1
        for op2 in ['+', '-', '/', '*']:
            s[3] = op2
            for op3 in ['+', '-', '/', '*']:
                s[5] = op3
                for op4 in ['+', '-', '/', '*']:
                    s[7] = op4
                    for op5 in ['+', '-', '/', '*']:
                        s[9] = op5
                        v = "".join(s)
                        # print(v)
                        res = eval(v)
                        if should is None:
                            print(v, res)
                        else:
                            if abs(float(should) - res) <= 0.01:
                                print(v, res, should)
                                yield s


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
            if c in ['A', 'B', 'C', 'D', 'E','F','G','H','S','L']:  # Challenge 1 '2 Hasen'
                pois[c] = (currow, curcol)
                cur.append(c)
            else:
                cur.append(int(c))
        maze.append(cur)

    f.close()
 #   print(maze)
 #   print(pois)

def solveMathonymous():
    global ans
    global keks
    global proxies
    if "Mathonymous" in ans.content:
        # Solve Mathonymous
        while True:
            print("There are multiple correct solutions!")
            regex = '<td><code style="font-size: 1em; margin: 10px">(.*)</code></td>'
            hit = re.findall(regex, ans.content)
            if len(hit) != 6:
                print("Error")
            else:
                n1 = hit[0]
                n2 = hit[1]
                n3 = hit[2]
                n4 = hit[3]
                n5 = hit[4]
                n6 = hit[5]
                regex = '<td><code style="font-size: 1em">=(.*)</code></td>'
                hit = re.findall(regex, ans.content)
                should = hit[0]

            ###########################
                all_res = mathonymous(n1, n2, n3, n4, n5, n6, should)

            ###########################
                # solutions = []
                #for val in all_res:
                #    new_list = val[:]
                #    solutions.append(new_list)

                for val in mathonymous(n1, n2, n3, n4, n5, n6, should):
                    print(val)
                    ##p = urllib.quote("".join([val[x] for x in range(len(val)) if x % 2 == 1]), safe='')
                    ##print(p)
                    ##ans = requests.get("{0}?op={1}".format(URL, p), proxies=proxies,
                    ##                   cookies=keks, allow_redirects=False)
                    ans = requests.get("{0}?op={1}".format(URL, urllib.quote(
                        "".join([val[x] for x in range(len(val)) if x % 2 == 1]), safe='')), proxies=proxies, cookies=keks,
                                       allow_redirects=False)

                    keks = ans.cookies
                    if "You solved it!" in ans.content:
                        print("Solved mathonymous!")
                        return
            print("Something went wrong :-(")

        # s = mathonymous(n1,n2,n3,n4,n5,res)
        '''
        <form method="get"
          oninput="this.op.value=$('#op1').val()+$('#op2').val()+$('#op3').val()+$('#op4').val()+$('#op5').val();">
        <table>
            <tr>
                <input type="hidden" value="" name="op">
                <td><code style="font-size: 1em; margin: 10px">12 </code></td>
                <td><input class="form-control" id="op1" type="text" maxlength="1" size="1" style="width:40px">
                </td>
                <td><code style="font-size: 1em; margin: 10px"> 19 </code></td>
                <td><input class="form-control" id="op2" type="text" maxlength="1" size="1" style="width:40px">
                </td>
                <td><code style="font-size: 1em; margin: 10px"> 7 </code></td>
                <td><input class="form-control" id="op3" type="text" maxlength="1" size="1" style="width:40px">
                </td>
                <td><code style="font-size: 1em; margin: 10px"> 17 </code></td>
                <td><input class="form-control" id="op4" type="text" maxlength="1" size="1" style="width:40px">
                </td>
                <td><code style="font-size: 1em; margin: 10px"> 11 </code></td>
                <td><input class="form-control" id="op5" type="text" maxlength="1" size="1" style="width:40px">
                </td>
                <td><code style="font-size: 1em; margin: 10px"> 15</code></td>
                <td><code style="font-size: 1em">= -149.42857142857144</code></td>
            </tr>
        </table>
        <hr>
    
        <div class="form-group">
            <input type="submit" class="btn btn-primary" value="Submit">
        </div>
    </form>'''

def solveWarmup():
    global ans
    global keks
    # Check for challenge 1
    if "Are you ready for a little warmup to get your most important sin on focus" in ans.content:
        '''
        <div>
        Weeeeelcoooome! <br>Are you ready for a little warmup to get your most important sin on focus?
        <hr>
        <div class="d-flex">
            <img src="../../static/img/ch11/c11.png">
            <img src="../../static/img/ch11/challenges/4f108aa0-ca6b-4d35-b1db-7d2276510dd4.png">
        </div>
        <form method="get">
            <input type="text" class="form-control mt-3" name="pixels" placeholder="[[1,0], [2,4], [8,1], ...]">
            <input type="submit" class="btn btn-info my-3" value="Send">
        </form>
        </div>
        '''
        # Send "[[1,0],[2,0]]" as as response
        ans = requests.get("{0}?pixels=[[1%2C0]%2C[2%2C0]]".format(URL), cookies=keks, proxies=proxies,
                           allow_redirects=False)
        keks = ans.cookies
        if "You solved it" in ans.content:
            print("Solved challenge 1")
        else:
            print("COULD NOT SOLVE!")


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

def solveEinstein():
    global keks
    global ans
    if "Pumple" in ans.content:
        bunnies = var()
        tuple_list = []
        statements = []

        regex = '<pre class="mb-2">(.*)</pre>'
        hit = re.findall(regex, ans.content)
        for h in hit:
            statements.append(h)
        while len(statements) > 0:
            s = statements.pop()
            # Check which rule we're dealing with
            if "There are five bunnies." in s:
                tuple_list.append((eq, (var(), var(), var(), var(), var()), bunnies))
            elif "The backpack of the " in s:
                # Regex it out
                regex = 'The backpack of the (.*) bunny is (.*)\.'
                hit = re.findall(regex, s)
                tuple_list.append((membero, (var(), var(), hit[0][0], var(), hit[0][1]), bunnies))
            elif "sits next to the bunny with a" in s:
                regex = '(.*) sits next to the bunny with a (.*) backpack'
                hit = re.findall(regex, s)
                tuple_list.append(
                    (nexto, (hit[0][0], var(), var(), var(), var()), (var(), hit[0][1], var(), var(), var()), bunnies))
            elif ", on the left." in s:
                regex = 'The bunny with the (.*) backpack sits next to the bunny with the (.*) backpack, on the left'
                hit = re.findall(regex, s)
                tuple_list.append(
                    (lefto, (var(), hit[0][0], var(), var(), var()), (var(), hit[0][1], var(), var(), var()), bunnies))
            elif "star sign is" in s:
                regex = "(.*)&#39;s star sign is (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append((membero, (hit[0][0], var(), var(), hit[0][1], var()), bunnies))
            elif "sits also next to the" in s:
                regex = "The (.*) bunny sits also next to the (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append(
                    (nexto, (var(), var(), hit[0][0], var(), var()), (var(), var(), var(), hit[0][1], var()), bunnies))
            elif "sits in the middle" in s:
                regex = "The bunny with the (.*) backpack sits in the middle"
                hit = re.findall(regex, s)
                tuple_list.append((eq, (var(), var(), (var(), var(), var(), var(), hit[0]), var(), var()), bunnies))
            elif "the first bunny" in s:
                regex = "(.*) is the first bunny"
                hit = re.findall(regex, s)
                tuple_list.append((eq, ((hit[0], var(), var(), var(), var()), var(), var(), var(), var()), bunnies))
            elif "The bunny with a" in s:
                regex = "The bunny with a (.*) backpack sits next to the (.*) bunny"
                hit = re.findall(regex, s)
                tuple_list.append(
                    (nexto, (var(), var(), hit[0][1], var(), var()), (var(), var(), var(), var(), hit[0][0]), bunnies))
            elif "was expensive" in s:
                regex = "The (.*) backpack by (.*) was expensive"
                hit = re.findall(regex, s)
                tuple_list.append((membero, (hit[0][1], var(), var(), var(), hit[0][0]), bunnies))
            elif "backpack is also" in s:
                regex = "The (.*) backpack is also (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append((membero, (var(), hit[0][1], var(), var(), hit[0][0]), bunnies))
            elif "sits next to the" in s:  # Warning! Less generic than another rule
                regex = "The (.*) bunny sits next to the (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append(
                    (nexto, (var(), var(), hit[0][0], var(), var()), (var(), var(), var(), hit[0][1], var()), bunnies))
            elif "The backpack of" in s:  # Warning! Less generic than another rule
                regex = "The backpack of (.*) is (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append((membero, (hit[0][0], hit[0][1], var(), var(), var()), bunnies))
            elif "bunny has a" in s:  # Warning! Less generic than another rule
                regex = "The (.*) bunny has a (.*) backpack"
                hit = re.findall(regex, s)
                tuple_list.append((membero, (var(), hit[0][1], hit[0][0], var(), var()), bunnies))
            elif "is also" in s:
                regex = "The (.*) is also (.*)\."
                hit = re.findall(regex, s)
                tuple_list.append((membero, (var(), var(), hit[0][1], hit[0][0], var()), bunnies))
            else:
                regex = "(.*) is a (.*) bunny"
                hit = re.findall(regex, s)
                tuple_list.append((membero, (hit[0][0], var(), hit[0][1], var(), var()), bunnies))

        # Auto add all zodiacs
        tuple_list.append((membero, (var(), var(), var(), 'taurus', var()), bunnies))
        tuple_list.append((membero, (var(), var(), var(), 'capricorn', var()), bunnies))
        tuple_list.append((membero, (var(), var(), var(), 'pisces', var()), bunnies))
        tuple_list.append((membero, (var(), var(), var(), 'aquarius', var()), bunnies))
        tuple_list.append((membero, (var(), var(), var(), 'virgo', var()), bunnies))

        autobunnyRules = lall(*tuple(tuple_list))
        print("Solving Einstein - this could take up to one minute!")
        solutions = run(0, bunnies, autobunnyRules)
        # IN my solution "Taurus" was missing from the list - it wasnt even mentioned in the rules!
        # The missing rule is of type "var" and throws an exception during param building!
        for line in solutions[0]:
            print str(line)
        # Build answer string:
        # Name,Bunny#1,Bunny#2,Bunny#5,Color,Blue,Yellow,..,..,Characteristic,Funny
        # Example: Name,Angel,Bunny,Snowball,Midnight,Thumper,Color,Blue,Yellow,Yellow,Yellow,Red,Characteristic,Funny,Lovely,Handsome,Scared,Attractive,Starsign,Taurus,Pisces,Capricorn,Virgo,Aquarius,Mask,Camouflaged,Striped,One-coloured,Dotted,Chequered"
        # My display:
        '''
        ('Angel', 'white', 'lovely', 'virgo', 'chequered')
        ('Bunny', 'red', 'scared', 'aquarius', 'striped')
        ('Snowball', 'blue', 'attractive', 'pisces', 'camouflaged')
        ('Midnight', 'yellow', 'funny', ~_11, 'dotted')
        ('Thumper', 'green', 'handsome', 'taurus.', 'one-coloured')
        '''
        param = ""

        for attrib in xrange(5):
            if attrib==0:
                param += "Name,"
            elif attrib==1:
                param += "Color,"
            elif attrib==2:
                param += "Characteristic,"
            elif attrib == 3:
                param += "Starsign,"
            elif attrib == 4:
                param += "Mask,"
            for hase in xrange(5):
                param += "{0},".format(solutions[0][hase][attrib].capitalize())

        ans = requests.get("{0}?solution={1}".format(URL,param[:-1]), cookies=keks, proxies=proxies,
                           allow_redirects=False)
        keks = ans.cookies
        if "Your solution is wrong!" in ans.content:
            print("Solution wrong")
        else:
            print("Solution correct!!")
        return

def lefto(q, p, list):
    # give me q such that q is left of p in list
    # zip(list, list[1:]) gives a list of 2-tuples of neighboring combinations
    # which can then be pattern-matched against the query
    return membero((q, p), zip(list, list[1:]))

def nexto(q, p, list):
    # give me q such that q is next to p in list
    # match lefto(q, p) OR lefto(p, q)
    # requirement of vector args instead of tuples doesn't seem to be documented
    return conde([lefto(q, p, list)], [lefto(p, q, list)])


def solveCaptchas():
    global keks
    global ans
    if "C0tt0nt4il Ch3ck V2.0 required" in ans.content:
        cnt = 0
        # First one always fails. Don't know yet why, but never mind.
        for cnt in range(11):
            regex = '<img id="captcha" src="static/img/ch12/challenges/[0-9a-f]{8}-[0-9a-z]{4}-(.*)-[0-9a-z]{4}-[0-9a-z]{12}.png"'
            hit = re.findall(regex, ans.content)
            # print(hit[0])
            if hit is None or len(hit) == 0:
                # Send anything
                ans = requests.get("{0}?result={1}".format(URL, 42), proxies=proxies, cookies=keks,
                                   allow_redirects=False)
            else:
                ans = requests.get("{0}?result={1}".format(URL, hit[0]), proxies=proxies, cookies=keks,
                                   allow_redirects=False)
            keks = ans.cookies
            cnt += 1
        if "Good job" in ans.content:
            return
        else:
            print("Fail :-(")
            exit(1)

def solveBattleship():
    global keks
    global ans
    print("The current 'session' cookie to set in BURP is:")
    print(keks['session'])
    print("Please solve the game using the lua solver and enter the cookie here again")
    k = raw_input("Cookie value: ")
    keks = {'session': k}
    return

'''
def solveLife():
    global keks
    global ans
    query = '{ In { Out{see hear taste smell touch} see hear taste smell touch }}'
    json = { 'query' : query}

    counter=0
    compareString = ""
    compareString2 = ""
    while True:
        ans = requests.post('http://whale.hacking-lab.com:5337/live/a/life', json=json, proxies=proxies, cookies=keks)
        keks = ans.cookies
        data = ans.json()
        compareString = data["data"]["In"]["Out"]["see"] + \
                        data["data"]["In"]["Out"]["hear"] + \
                        data["data"]["In"]["Out"]["taste"] + \
                        data["data"]["In"]["Out"]["smell"] + \
                        data["data"]["In"]["Out"]["touch"]

        compareString2 = data["data"]["In"]["see"] + \
                        data["data"]["In"]["hear"] + \
                        data["data"]["In"]["taste"] + \
                        data["data"]["In"]["smell"] + \
                        data["data"]["In"]["touch"]

        for key in ["hear", "taste", "smell", "see", "touch"]:
            c=compareString.count(data["data"]["In"]["Out"][key])
            c2 = compareString2.count(data["data"]["In"][key])
            if c >= 3:
                #print data["data"]["In"]["Out"]
                print("Out: ", compareString)
            if c2 >= 3:
                #print data["data"]["In"]
                print("In: ", compareString2)

'''

def solveLife():
    global keks
    global ans
    cnt = 0

    bins = {}
    while cnt<10:
        ans = requests.get("http://whale.hacking-lab.com:5337/?new=life", proxies=proxies, cookies=keks,
                                   allow_redirects=False)
        keks=ans.cookies
        GotIt = False
        sentence = ""
        sentence2 = ""
        lstIn = []
        lstOut = []
        numQueries = 0
        while GotIt==False:
            numQueries+=1
            ans = requests.get("http://whale.hacking-lab.com:5337/live/a/life?query=%7BIn%7Bsee%20hear%20taste%20touch%20smell%20Out%7Bsee%20hear%20taste%20touch%20smell%7D%7D%7D", proxies=proxies, cookies=keks,
                           allow_redirects=False)
            keks = ans.cookies
            resp = json.loads(ans.content)
            v = ""
            needOut=True
            print("{0} - Raw JSON: {1}".format(numQueries, str(resp)))
            # rearrange the Out sub dict to root
            resp["data"]["Out"]=resp["data"]["In"]["Out"]
            del (resp["data"]["In"]["Out"])

            for k in resp["data"]["In"].keys():
                v = resp["data"]["In"][k]
                if bins.has_key(v):
                    bins[v]+=1
                    if bins[v]==3:
                        print("Found in 'in': " +v)
                        lstIn.append(v)
                        sentence2+=v
                        break
                else:
                    bins[v]=1
            bins.clear()
            for k in resp["data"]["Out"].keys():
                v = resp["data"]["Out"][k]
                if bins.has_key(v):
                    bins[v]+=1
                    if bins[v]==3:
                        print("Found in 'out': " + v)
                        lstOut.append(v)
                        sentence2 += v
                        break
                else:
                    bins[v]=1
            if 'd' in bins.keys() and 'e' in bins.keys() and 'a' in bins.keys() and 't' in bins.keys() and 'h' in bins.keys():
                print("Oh oh! Dead! Reset!")

                bins.clear()
                cnt+=1
                reset = True
                break
            bins.clear()
            if len(lstIn)+len(lstOut) == 4:
                print("Content of inqueue: " + "".join(lstIn))
                print("Content of outqueue: " + "".join(lstOut))
                print("In order: " + sentence2)
                GotIt=True
                sentence="".join(lstIn)+"".join(lstOut)
                print("Sending: ", sentence)
                #sentence=sentence2

        # We have solved it
        # Send it as "/?checksum=ABCDE"
        if GotIt == True:
            ans = requests.get(
                "http://whale.hacking-lab.com:5337/?checksum={0}".format(sentence),
                proxies=proxies, cookies=keks,
                allow_redirects=False)
            keks = ans.cookies
            if "solved" in ans.content:
                print("Solved!")
                return
            else:
                print("Failed.")
                exit(1)



def solveRandom():
    global ans
    global keks
    if "You just entered the matrix" in ans.content:
        regex="<code>([\-\d]+)</code>"
        hit = re.findall(regex, ans.content)
        initial_seed = int(hit[0])
        print("Initial seed: ", initial_seed)
        random.seed(initial_seed)

        for cnt in range(1337):
            val = random.randint(-(1337**42),1337**42)
            random.seed(val)

        ans = requests.get(
            "http://whale.hacking-lab.com:5337/?guess={0}".format(val), proxies=proxies, cookies=keks, allow_redirects=False)
        keks = ans.cookies
        if "Your solution is wrong!" in ans.content:
            print("Fail!")
            exit(1)

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def solveBlink():
    global ans
    global keks
    # Download blinking gif
    # <img alt="dontknow" src="../../static/img/ch15/challenges/752f9905-b072-4664-beb8-ddcca365e3f5.gif" height="5" width="5">
    # -> http://whale.hacking-lab.com:5337/static/img/ch15/challenges/752f9905-b072-4664-beb8-ddcca365e3f5.gif
    regex = "/static/img/ch15/challenges/([a-f0-9]{8}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{4}\-[a-f0-9]{12})"

    hit = re.findall(regex, ans.content)
    pic = hit[0]
    ans = requests.get("http://whale.hacking-lab.com:5337/static/img/ch15/challenges/{0}.gif".format(pic),
                       proxies=proxies, cookies=keks,     allow_redirects = False)

    imageObject = Image.open(cStringIO.StringIO(ans.content))
    # Display individual frames from the loaded animated GIF file

    sequence = []

    for frame in range(0, imageObject.n_frames):
        imageObject.seek(frame)
        t = imageObject.convert('RGB')

        if t.getpixel((0, 0))[0] == 0:
            sequence.append('0')
        else:
            sequence.append('1')
    morsecode = "".join(sequence)
    print(morsecode)

    res = split_len(morsecode, 8)
    chars = []
    for r in res:
        chars.append(chr(int(r, 2)))

    print("".join(chars))
    solution= "".join(chars)
    ans = requests.get("http://whale.hacking-lab.com:5337/?code={0}".format(solution), proxies=proxies, cookies=keks, allow_redirects=False)
    keks = ans.cookies
    if "You solved it" in ans.content:
        print("Solved!")
    else:
        print("Fail :-(")
        exit(1)

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

    FROM_S_TO_A = "uuuuuuu"
    FROM_A_TO_B = "urrrrrruuuurrurrdrruru"
    FROM_B_TO_C = "drdrrurrdrrurrrrrur"
    FROM_C_TO_D = "ddddl" # From Mathonymouos past the teleporter"

    FROM_E_TO_F = "ddddddrruuuuuurrddddddrruuu"
    FROM_F_TO_INTER = "uuurrrrr"
    FROM_INTER_TO_CASTLE="ddullldrdldrdldrrrrruu"

    # G = Teleporter in der Mitte der Schnecke
    # Battleship ist in der schleife rechts oben am ende
    FROM_INTER_TO_BATTLESHIP = "rrrrrrddddddrrrrrrrrrrrrruuuuuuuullld"
    FROM_BATTLESHIP_TO_STRANGEONE = "urrrddddddllllllllllluuuuurrrrdddllu"
    FROM_INTER_TO_CHIMNEY="rrrrruuuu"
    FROM_CHIMNEY_TO_SOMEWHERE="dddrdddddddrrrrrrrruuuuuu"
    FROM_BATTLESHIP_TO_VERTICAL="urrrddddddllllluuuuu"
    FROM_CASTLE_TO_CHIMNEY="ddrrrruuuuuuuluuu"
    FROM_CHIMNEY_TO_SCHNEGGE="dddrdddddddrrrrrrrruulllllluuuuurrrrdddllu"
    FROM_SCHNEGGE_TO_BATTLESHIP="drruuulllldddddrrrrrrrrrrruuuuuullld"
    replay(FROM_S_TO_A)
    solveWarmup()
    replay(FROM_A_TO_B)
    solveCaptchas()
    replay(FROM_B_TO_C)
    solveMathonymous()
    replay(FROM_C_TO_D)
    # Activate teleporter here

    #print(posx,posy)  #27,11
    # We will now reset!

    posx=30
    posy=7
    maze[posy][posx] = 0
    replay(FROM_E_TO_F)
    #print("Skipping Einstein for now")
    solveEinstein()
    replay(FROM_F_TO_INTER)
    replay(FROM_INTER_TO_CASTLE)
    solveBlink()
    replay(FROM_CASTLE_TO_CHIMNEY)
    solveRandom()
    replay(FROM_CHIMNEY_TO_SCHNEGGE)
    solveLife()
    replay(FROM_SCHNEGGE_TO_BATTLESHIP)
    solveBattleship()
    #replay(FROM_INTER_TO_CHIMNEY)
    replay("dddr")
    #replay(FROM_CHIMNEY_TO_SOMEWHERE)
    # Will be done later
    #replay(FROM_INTER_TO_BATTLESHIP)
    #solveBattleship()
    #replay(FROM_BATTLESHIP_TO_VERTICAL)
    #replay(FROM_BATTLESHIP_TO_STRANGEONE)


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
Helper function to wait for a key press of the user
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
r = requests.get("{0}/1804161a0dabfdcd26f7370136e0f766".format(URL), proxies=proxies, allow_redirects=False)

keks = r.cookies

# Send format string exploit in username

print("Starting game")
#init_maingame_loop(dimx=80, dimy=50, startx=2, starty=35)

init_maingame_loop()




