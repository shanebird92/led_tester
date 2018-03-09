import re

ifile = "test_data.txt"


def parseFile(input):



  
    if input.startswith('http'):
        
        pass

    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                searchObj = re.search(r'(.*)(\d+),(\d+) through (\d+),(\d+)', line)
                instructions.append(searchObj)
                  
                print(N,searchObj.group(0))
                print(instructions)
        return N, instructions
    return
parseFile(ifile)