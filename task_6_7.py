from sys import argv
with open('bakery.csv', 'a', encoding='utf-8') as bake_add:
    with open('bakery.csv', 'r', encoding='utf-8') as bake_read:
        if len(argv) == 1:
            print(bake_read.read())
        elif len(argv) == 2:
            if ',' in argv[1]:
                bake_read.read()
                print(argv[1], file=bake_add)
            else:
                print(*bake_read.readlines()[int(argv[1]) - 1:], sep='')
        else:
            print(*bake_read.split()[int(argv[1]):int(argv[2]) + 1], sep='\n')
