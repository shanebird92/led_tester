import urllib.request
import requests
uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"

req = urllib.request.urlopen(uri)

buffer = req.read().decode('utf-8')

N, instructions = None, []

N=buffer.splitlines()[0]
#for line in 
print(N)

for i in range(1,len(buffer.splitlines())):
    instructions=buffer.splitlines()[i]
    print(instructions)