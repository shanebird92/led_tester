#utils.py- used to parse inctructions

def parseFile(input):

    if input.startswith('http'):
        
        pass

    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    return
