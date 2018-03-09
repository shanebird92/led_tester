# -*- coding: utf-8 -*-

"""Console script for led_tester."""
import sys
import click
from utils import parseFile
import re
import cmd

def apply_led(N, instructions):
    list2D = [ [0]*N for _ in range (N) ]
    
    
    for line in instructions:
        searchObj = re.search(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", line)
        if searchObj:
            cmd = searchObj.group(1)
            x1 = int(searchObj.group(2))
            y1 = int(searchObj.group(3))
            x2 = int(searchObj.group(4))
            y2 = int(searchObj.group(5))
        
        if x1 < 0:
            x1=0
        if y1 < 0:
            y1 =0
        if x2 > N-1:
            x2 = N-1
        if y2 > N-1:
            y2 =N-1    
    
    
        if cmd == "turn on":
            for i in range (x1, x2+1):
                for j in range (y1, y2+1):
                    list2D[i][j]=1
                    
        elif cmd == "turn off":
            for i in range (x1, x2+1):
                for j in range (y1, y2+1):
                    list2D[i][j]=0
                    
        elif cmd == "switch":
            for i in range (x1, x2+1):
                for j in range (y1, y2+1):
                    if list2D[i][j]==1:
                        list2D[i][j]=0
                    elif list2D[i][j]==0:
                        list2D[i][j]=1
        else:
            continue
        
    return sum(sum(x) for x in list2D)


@click.command()
@click.option("--input", default=None, help="input URI (file or URL)")

def main(input):
    """Console script for led_tester."""
    
    ''' takes two arguments from input as N and instructions, N is first number which I will use to make the
    led, i.e will be the size of the led board squared. Instructions will then be each line which will be 
    passed to the reg ex expression to have infor extracted.
    ''' 
    N, instructions = parseFile(input)
    
    

    print ("The amount of LED's currently 'ON' is: ", apply_led(N, instructions))
    return 0
if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
