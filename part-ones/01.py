ex_list = [199,200,208,210,200,207,240,269,260,263]

def depthdiff(lis):
    lis2 = zip(lis,lis[1:])
    lis3 = [1 if depth_cur > depth_prev else 0 for depth_prev, depth_cur in lis2]
    print(lis3)

def main():
    depthdiff(ex_list)

main()