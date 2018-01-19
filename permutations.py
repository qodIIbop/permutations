from itertools import permutations
from math import factorial

def main():
    object_list = []
    ans_opt = ['Y','N','y','N']

    filename = input('Please give filename to save permutations to: ')
    max_num = input('Please give number of objects: ')

    fac_ans = factorial(int(max_num))
    warn_ans = input("There are %s number of possibilities. Are you sure you what to print to file? (Y/N): " % fac_ans )
    while warn_ans not in ans_opt:
        warn_ans = input('Please type one of the following: '+' or '.join("{}".format(k) for k in (ans_opt))+': ')

    for item in range(int(max_num)):
        object_list.append(item+1)

    with open(filename, 'w') as f:
        for permutation in permutations(object_list):
            f.write(str(permutation))

    return 'All permutations calculated'

if __name__ == '__main__':
    main()
