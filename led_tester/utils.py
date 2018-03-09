#utils.py- used to parse inctructions
import urllib.request
import requests
def parseFile(input):

    if input.startswith('http'):
        
        
        uri = input
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8')
        
        N, instructions = None, []
        N= int(buffer.splitlines()[0])
        
        for i in range(1,len(buffer.splitlines())):
            instructions.append(buffer.split('\n')[i])
        return N, instructions

    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions

