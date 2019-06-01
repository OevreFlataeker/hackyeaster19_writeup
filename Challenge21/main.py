'''
Please use main_direct_Walk21.py. This code is not up to date!
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from os import system, name
import re
import urllib

#def goToUserInput():
#    r.sendline("exit")
#    r.recvuntil(">")
#    r.sendline("1")
#    return r.recvuntil(">")

SOUTH = "/0/1"
NORTH = "/0/-1"
EAST = "/1/0"
WEST = "/-1/0"
keks = None
maze = None
checked = None

proxies = {
               'http': 'http://127.0.0.1:8080',
               'https': 'http://127.0.0.1:8080',
           }

def decode(direc):
    if direc==NORTH:
        return "NORTH"
    elif direc==SOUTH:
        return "SOUTH"
    elif direc==EAST:
        return "EAST"
    else:
        return "WEST"
'''
Checks which directions are possible to walk from the current position
Caches the found information.
Clumsy implementation but it works
'''
def checkDir(r, maze, posy, posx):
    global keks
    global proxies
    if checked[posy][posx] == 1:
        return ""
    possible = {}
    got302 = False
    l = None
    # print("I am at ", posy, posx)
    for d in [WEST, NORTH, EAST, SOUTH]:
        #print("trying ", decode(d))
        # Send step
        # r.sendline("go {0}".format(d))
        # r.sendline("go {0}".format(d))
        ans = requests.get("{0}/move{1}".format(URL,d),cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        response = ans.content
        if ans.status_code==302:
            print("Got 302!")
            got302 = True
            l = ans.headers['Location']
        if ans.status_code==500:
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
                ans = requests.get("{0}?pixels=[[1%2C0]%2C[2%2C0]]".format(URL),cookies=keks,proxies=proxies, allow_redirects=False)
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
                    hit = re.findall(regex,ans.content)
                    #print(hit[0])
                    if hit==None or len(hit)==0:
                        # Send anything
                        ans = requests.get("{0}?result={1}".format(URL, 42), proxies=proxies, cookies=keks,
                                           allow_redirects=False)
                    else:
                        ans = requests.get("{0}?result={1}".format(URL, hit[0]), proxies=proxies,cookies=keks,allow_redirects=False)
                    keks = ans.cookies
                    cnt+=1
                print("Done?")
            # Challenge 3
            elif "Mathonymous" in ans.content:
                # Solve Mathonymous
                print("There are multiple correct solutions!")
                regex = '<td><code style="font-size: 1em; margin: 10px">(.*)</code></td>'
                hit = re.findall(regex, ans.content)
                if len(hit)!=6:
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
                    all_res = mathonymous(n1,n2,n3,n4,n5,n6,should)
                    for val in all_res:
                        print(val)

                        ans = requests.get("{0}?op={1}".format(URL, urllib.quote("".join([val[x] for x in range(len(val)) if x % 2 == 1]),safe='')), proxies=proxies,cookies=keks,allow_redirects=False)
                        keks = ans.cookies
                        if "Your navigator says this is right" in ans:
                            print("Solved mathonymous!")
                            break
                pass
                #s = mathonymous(n1,n2,n3,n4,n5,res)
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
            #print("Stepped ok, undoing")
            if d == NORTH:

                ans = requests.get("{0}/move{1}".format(URL, SOUTH),cookies=keks, proxies=proxies, allow_redirects=False)
                keks = ans.cookies
                # go SOUTH

            elif d == SOUTH:
                # go NORTH
                ans = requests.get("{0}/move{1}".format(URL, NORTH), cookies=keks, proxies=proxies, allow_redirects=False)
                keks = ans.cookies

            elif d == EAST:
                #go WEST
                ans = requests.get("{0}/move{1}".format(URL, WEST), cookies=keks, proxies=proxies, allow_redirects=False)
                keks = ans.cookies

            else:
                # go EAST
                ans = requests.get("{0}/move{1}".format(URL, EAST), cookies=keks, proxies=proxies, allow_redirects=False)
                keks = ans.cookies



    # Updates the in-memory copy of the maze with the
    # information which steps are possible (0 = there is a path in that direction)
    # If we have already seen that particular place before (value == 3), we do not
    # overwrite the value

    # print("Setting values, relative to ",posy,posx)
    if possible[NORTH]:
        #print("Opened north")
        if maze[posy - 1][posx] != 3:
            maze[posy - 1][posx] = 0
    if possible[EAST]:
        #print("Opened east")
        if maze[posy][posx + 1] != 3:
            maze[posy][posx + 1] = 0
    if possible[SOUTH]:
        #print("Opened south")
        if maze[posy + 1][posx] != 3:
            maze[posy + 1][posx] = 0
    if possible[WEST]:
        #print("Opened west")
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
                xp = u"\u2592" # .
            # Draw the player
            if col == posx and row == posy:
                xp = u"\u25c9" # @
            s += xp
        print(s)


def mathonymous(n1,n2,n3,n4,n5,n6,res):
    s = [str(float(n1.strip())),'',str(float(n2.strip())),'',str(float(n3.strip())),'',str(float(n4.strip())),'',str(float(n5.strip())),'',str(float(n6.strip()))]
    should = res

    for op1 in ['+','-','/','*']:
        s[1] = op1
        for op2 in ['+','-','/','*']:
            s[3] = op2
            for op3 in ['+','-','/','*']:
                s[5] = op3
                for op4 in ['+','-','/','*']:
                    s[7] = op4
                    for op5 in ['+','-','/','*']:
                        s[9] = op5
                        v = "".join(s)
                        #print(v)
                        res = eval(v)
                        if should==None:
                            print(v,res)
                        else:
                            if abs(float(should)-res) <= 0.01:
                                print(v,res,should)
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

    if direct == NORTH:
        # r.sendline("go north")
        ans = requests.get("{0}/move{1}".format(URL, NORTH), cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        posy -= 1
        if ans.status_code==302:
            print("Got 302!")
            ans = requests.get(ans.headers['Location'], cookies=keks, proxies=proxies, allow_redirects=False)

    elif direct == SOUTH:

        # go /0/1
        ans = requests.get("{0}/move{1}".format(URL, SOUTH), cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        posy += 1
        if ans.status_code==302:
            print("Got 302!")
            ans = requests.get(ans.headers['Location'], cookies=keks, proxies=proxies, allow_redirects=False)
    elif direct == EAST:

        # go /1/0
        ans = requests.get("{0}/move{1}".format(URL, EAST), cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        posx += 1
        if ans.status_code==302:
            print("Got 302!")
            ans = requests.get(ans.headers['Location'], cookies=keks, proxies=proxies, allow_redirects=False)
    else: # WEST
        # go /-1/0
        ans = requests.get("{0}/move{1}".format(URL, WEST), cookies=keks, proxies=proxies, allow_redirects=False)
        keks = ans.cookies
        posx -= 1
        if ans.status_code==302:
            print("Got 302!")
            ans = requests.get(ans.headers['Location'], cookies=keks, proxies=proxies, allow_redirects=False)
    #print(ans)
    # Send search command
    #r.sendline("search")
    #ans = r.recvuntil(">")
    #print(ans)
    # Have we found a key?
    printmaze(maze)


def init_maingame_loop(dimx, dimy, startx, starty):
    # Send "Play"
    global maze
    global checked
    global posx
    global posy

    # Build an in-memory variant of the maze
    #dimx = 40
    #dimy = 20
    maze = [[1] * dimx for x in range(dimy)]
    # Build a "cache table" which flags which squares already have been discovered
    # This is probably unnecessary and we could do w/o.
    checked = [[0] * dimx for x in range(dimy)]

    # Start position (arbitrary, right in the middle so we have enough space no matter where the maze grows to
    posx = startx
    posy = starty

    # Initialize current pos as "path"
    maze[posy][posx] = 0

    # Print the starting position on server

    # Print local in-memory copy
    printmaze(maze)

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

        print("Restarting the recursive walk!")
        waitKey()
        # Reset maze
        # We also need to reset the checked maze unfortunately :-(
        newmaze = [[1] * dimx for x in range(dimy)]
        for y_ in xrange(len(maze)):
            for x_ in xrange(len(maze[0])):
                newmaze[y_][x_] = 0 if maze[y_][x_] == 3 else maze[y_][x_]
                checked[y_][x_] = 0

        maze = newmaze



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
r = requests.get("{0}/1804161a0dabfdcd26f7370136e0f766".format(URL), proxies=proxies, allow_redirects=False)

keks = r.cookies

# Send format string exploit in username

print("Starting game")
init_maingame_loop(dimx=80, dimy=50, startx=2, starty=35)




