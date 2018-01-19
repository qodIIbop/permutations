from itertools import permutations

def main():
    object_list = []

    filename = input('Please give filename to save permutations to: ')
    max_num = input('Please give number of objects: ')

    for item in range(int(max_num)):
        object_list.append(item+1)

    perm = list(permutations(object_list))

    with open(filename, 'w') as f:
        for line in perm:
            f.write(str(line))

if __name__ == '__main__':
    main()