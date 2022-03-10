ex_instr = [('forward', 5),('down',5),('forward',8),('up',3),('down',8),('forward',2)]

def instr_exec(lis):
    X = 0
    Y = 0
    for inst, val in lis:
        if inst == 'forward':
            X += val
        elif inst == 'down':
            Y += val
        elif inst == 'up':
            Y -= val
    return X * Y

def main():
    print(instr_exec(ex_instr))

main()