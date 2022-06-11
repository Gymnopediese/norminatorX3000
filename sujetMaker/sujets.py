# importing all the required modules
import PyPDF2
import sys
import os
# creating an object



def anyin(a,b):
    for i in a:
        if i in b:
            return i
    return "null"
function_name = ["void","int","char"]
def co(num): # TODO on l'a copier dans utils.py !!!
    if num == 0:
        return '00'
    if num <10:
        return f'0{num}'
    return str(num)
def gen_folder(module,path):
    import shutil


    file = open(f'sujets/{module}.pdf', 'rb')
    # creating a pdf reader object
    reader = PyPDF2.PdfFileReader(file)
    function = []
    functions = []
    for i in range(reader.numPages):
        temp = str(reader.getPage(i).extractText()).split('\n')
        for k in temp:
            if "Fichiers à rendre" in k:
                function.append(k.split(":")[1])
            temp = anyin(function_name,k)
            if temp != "null" and '(' in k:
                functions.append(k.replace(temp,temp+" "))
                print(k);
    path = path+f'c{co(module)}/'
    try:
        os.mkdir(path)
    except:
        pass
    shutil.copyfile(f'sujets/{module}.pdf', f'c{co(module)}/subjct.pdf')
    shutil.copyfile(f'run', f'c{co(module)}/run')
    gen_main(function,path)
    for func in range(len(function)):
        path2 = path+f'ex{co(func)}'
        os.mkdir(path2)
        with open(f'{path2}/{function[func]}', 'a') as f:
            f.write('#include <unistd.h>\n')
            try:
                f.write(functions[func])
            except:
                f.write("int main()\n")
                f.write("{\n")
                f.write("}\n")
def gen_main(function,path):
    file = open(path+"main.c","a")
    for i in range (len(function)):
        file.write(f'#include "ex{co(i)}/{function[i]}"\n')
    file.write(f'#include <stdio.h>\n')
    file.write(f'#include <unistd.h>\n')
    file.write(f'\n')
    file.write(f'int main(main)\n')
    file.write('{\n')
    for i in range (len(function)):
        file.write(f'\tprinttf("-----------------------ex{co(i)}------------------------");\n')
        file.write(f'\tprinttf("---------------------------------------------------");\n')
    file.write('}')

def gen_exo():
    pass
def gen_all(path=''):
    for ex in range(14):
        gen_folder(ex,path)
#file = open('sdf.pdf', 'rb')

# creating a pdf reader object
#reader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file

# subject -path -exo
# subject -path -exo
try:
    module = int(sys.argv[1])
    gen_folder(module,'')
except Exception as e:
    print(e,sys.argv)
    if len(sys.argv) == 2:
        gen_folder(sys.argv[1],sys.argv[2])
    elif len(sys.argv) == 2:
        gen_all(sys.argv[1])
    else:
        gen_all()
