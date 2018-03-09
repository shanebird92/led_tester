# -*- coding: utf-8 -*-
import re
"""Main module."""


def apply_led(N, instructions):
    list2D = [ [0]*N for _ in range (N) ]
    
    
    for line in instructions:
        searchObj = re.search(r'(.*)(\d+),(\d+) through (\d+),(\d+)', line)
        
        cmd = searchObj.group(1)
        x1 = int(searchObj.group(2))
        y1 = int(searchObj.group(3))
        x2 = int(searchObj.group(4))
        y2 = int(searchObj.group(5))
    
    
        if cmd == "turn on ":
            for i in range (x1, x2+1):
                for j in range (y1, y2+1):
                    list2D[i][j]=1
                    
        elif cmd == "turn off ":
            for i in range (x1, x2+1):
                for j in range (y1, y2+1):
                    list2D[i][j]=0
                    
        elif cmd == "switch ":
            for i in range (x1, x2+1):
                for j in range (y1, y2+1):
                    if list2D[i][j]==1:
                        list2D[i][j]=0
                    elif list2D[i][j]==0:
                        list2D[i][j]=1
        else:
            continue
        print(cmd)   
    return sum(sum(x) for x in list2D)
ifile = "test_data.txt"


def parseFile(input):

    if input.startswith('http'):
        
        pass

    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
     
        return apply_led(N, instructions)
    return
parseFile(ifile)