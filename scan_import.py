import os,sys
files = []

def ergodic_folder(src):
    global files
    if os.path.exists(src):
        if os.path.isfile(src):
            if os.path.splitext(src)[1] == '.py':
                files.append(src)
        elif os.path.isdir(src):
            for item in os.listdir(src):
                itemsrc = os.path.join(src, item)
                if ergodic_folder(itemsrc) == 1:
                    raise RuntimeError('Can not parse item: '+itemsrc)
        else:
            return 1
        return 0

    else:
        print(src + ' is not exist.')
        return 1

def find_import():
    global files
    imports = []
    for file in files:
        f = open(file,'r')
        for line in f.readline():
            line = line.strip()
            if line.find('import ') != -1:
                imports.append(line)
                continue
            if line.find('from ') != -1:
                imports.append(line)
                continue
    for i in imports:
        print(i)

if __name__=='__main__':
    src = sys.argv[1]
    print('Begin to find python file in folder: '+ src)
    if os.path.exists(src):
        ergodic_folder(src)
        find_import()
    else:
        print('Wrong input. Please input a file or a folder')
