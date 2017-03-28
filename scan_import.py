import os,sys,re

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
                    print('Can not parse item: '+itemsrc)
        else:
            return 1
        return 0

    else:
        print(src + ' is not exist.')
        return 1

def find_import():
    global files
    imports = []
    froms = []
    for file in files:
        f = open(file,mode='r',encoding=sys.getfilesystemencoding(), errors='replace')
        for line in f.readlines():
            line = line.strip()
            if line[0:7] == 'import ':
                imports.append(line)
                continue
            if line[0:5] == 'from ':
                froms.append(line)
                continue
    return imports,froms

def parse_import(imports):
    libs = set()
    for i in imports:
        got = re.split('\W+',i)
        if got.count('so') == 0:
            for q in got[1:]:
                libs.add(q)
        else:
            pos = got.index('so')
            for q in got[1:pos]:
                libs.add(q)
    return libs

def parse_from(froms):
    libs= set()
    for i in froms:
        got = i.split()
        if len(got) < 4:
            print('I do not know why but I found not more than 4 item in: '+i)
        else:
            for q in got[3:]:
                libs.add(got[1]+'.'+q)
    return libs



if __name__=='__main__':
    src = sys.argv[1]
    print('Begin to find python file in folder: '+ src)
    if os.path.exists(src):
        if ergodic_folder(src) !=0:
            raise RuntimeError('Some error eccur when find python files.')
        imports,froms = find_import()
        libs = parse_from(froms) | parse_import(imports)
        fff=open('python_import.log','w')
        for xx in libs:
            fff.write(xx+'\n')
        fff.close()
    else:
        print('Wrong input. Please input a file or a folder')
