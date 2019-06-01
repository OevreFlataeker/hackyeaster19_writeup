import walkdirect

def load_saved_map():
    global maze
    global pois

    f = open("map.txt")
    maze = []
    currow = 0
    pois = {}
    for line in f:
        currow+=1
        print line.rstrip()
        cur = []
        curcol=0
        for c in line:
            curcol+=1
            if c=='\n':
                continue
            if c=='X':
                c='1'
            if c=='.':
                c='0'
            if c in ['A','B','C','D','S']: # Challenge 1 '2 Hasen'
                pois[c]=(currow, curcol)
            cur.append(c)
        maze.append(cur)
    f.close()
    print(maze)
    print(pois)

# Saved paths
FROM_S_TO_A = "uuuuuuu"
FROM_A_TO_B = "urrrrrruuuurrurrdrruru"
FROM_B_TO_C = "drdrrurrdrrurrrrru"
FROM_C_TO_D = "ddddd"
