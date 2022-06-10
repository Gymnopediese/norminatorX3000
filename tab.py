import sys
#variable et fonctions
varname =["int","bool","char","void","int","int",]
#sign tp get space left and right
sign =[">=","<=","==","!=","||","&&","+","-","/",">","<","%"]
signChilds = [">","<"]
#sign tp get space right
signr =[","]
signs =[",","("]
#statement and loop
statement = ["if","while","else if","if","="]
#cheat
cheat = ["printf","\tfor(","\tfor ("]
def anyin(a,b):
    for i in a:
        if i in b:
            return i
    return "null"
def get():
    global file
    if len(sys.argv)== 3:
        if sys.argv[2] == "-i":
            file = open(sys.argv[1],'r')
    else:
        file = open("temp.c",'r')
    lines = file.readlines()
    file.close
def save():
    global file
    if len(sys.argv)== 3:
        if sys.argv[2]== "-i":
            file = open(sys.argv[1],'w')
            file.write(''.join(lines))
    else:
        open("temp.c","w").write(''.join(lines))
    file.close
def tabs():
    for i in range(len(lines)):
        count = 1
        tabs = 0
        while(lines[i][0] == " " or lines[i][0] == "\t"):
            if divmod(count,4)[1] == 0:
                tabs+=1
            if (lines[i][0] == " "):
                count += 1
            else:
                tabs+=1
            lines[i] = lines[i][1:]
        else:
            for c in range(tabs):
                lines[i] = "\t"+lines[i]
def func():
    for i in range(len(lines)):
        temp = lines[i]
        temp = temp.replace("\t","")
        temp = temp.split(" ")
        if (temp[0] in varname):
            lines[i] = lines[i].replace(" ","\t",1)

def signslr():
    for i in range(len(lines)):
        temp = lines[i]
        signsdone = ''
        for k in sign:
            if k in lines[i] and k not in signsdone:
                temp = lines[i].split(k)
                if temp[0] != '' and temp[1]!= '' :
                    if temp[0][len(temp[0])-1] != ' ':
                        temp[0] = temp[0]+ ' '
                checkbraces =temp[len(temp)-2].replace(' ','')
                checkbraces = ' '+checkbraces
                if temp[len(temp)-1] != '' and temp[len(temp)-2]!= ''and anyin(signs,checkbraces[len(checkbraces)-1]) == "null":
                    if temp[len(temp)-1][0] != ' ':
                        temp[len(temp)-1] = ' '+ temp[len(temp)-1]
                for n in range(1,len(temp)-1):
                    checkbraces =temp[n-1].replace(' ','')
                    checkbraces = ' '+checkbraces
                    if temp[n] != '' and temp[n+1]!= '' and temp[n-1]!= '' and anyin(signs,checkbraces[len(checkbraces)-1]) == "null":
                        if temp[n][0] != ' ':
                            temp[n] =  " "+ temp[n]
                        if temp[n][len(temp[n])-1] != ' ':
                            temp[n] = temp[n]+ ' '
                lines[i] = k.join(temp)
                signsdone+=k

def signsr():
    for i in range(len(lines)):
        for k in signr:
            temp = lines[i]
            if k in lines[i]:
                lines[i] = lines[i].split(k)
                for n in range(1,len(lines[i])):
                    if lines[i][n] != '':
                        if lines[i][n][0] != ' ':
                            lines[i][n] =  " "+lines[i][n]
                lines[i] = k.join(lines[i])
def keywordSpace():
    global lines
    for i in range(len(lines)):
        stat = anyin(statement,lines[i])
        if stat != "null":
            temp = lines[i].split(stat)
            if temp[1][0] != ' ':
                temp[1] = ' ' +temp[1]
            lines[i] = stat.join(temp)
def header():
    print("caledd");
    fil = open("headerr.txt",'r')
    line = fil.readlines()
    fir = open("header.txt",'r')
    lir = fir.readlines()
    print(len(line))
    import datetime
    now = datetime.datetime.now()
    for i in lines:
        if  line[0] ==  i:
            return
    print(len(line[0]))
    print(len(lir[0]))
    for i in range(len(line)):
        line[i] = line[i].replace('$',"albaud")
        line[i] = line[i].replace('%',sys.argv[1])
        line[i] = line[i].replace('!',str(now.year))
        line[i] = line[i].replace('@',str(now.month))
        line[i] = line[i].replace('F',str(now.day))
        line[i] = line[i].replace('^',str(now.hour))
        line[i] = line[i].replace('&',str(now.minute))
        line[i] = line[i].replace('=',str(now.second))
        line[i] = line[i][:48]
        line[i]+=lir[i]
        print(line[i])
        lines.insert(i,line[i])
    lines.insert(i+1,"\n")
def finalClean():
    global lines
    for i in range(len(lines)):
        lines[i] = lines[i].replace('  ',' ')
        temp = lines[i].replace(' ','').replace('\t','')
        if temp == "\n":
            lines[i] = temp
        try:
            if temp == '}\n' and "void" in lines[i+1]:
                lines.insert(i+1,"\n")
        except:
            pass
        if anyin(varname,lines[i]):
            lines[i] = lines[i].replace('()','(void)')
        lines[i] = lines[i].replace(' \n','\n')
        lines[i] = lines[i].replace('  \n','\n')
        lines[i] = lines[i].replace('   \n','\n')
        lines[i] = lines[i].replace('    \n','\n')
        tem = anyin(cheat,lines[i])
        if anyin(cheat,lines[i]) != "null":
            print("CHEAT")
file = open(sys.argv[1])
lines = file.readlines()

tabs()
func()
signslr()
signsr()
keywordSpace()

finalClean()
header()
save()

import os

if len(sys.argv)== 3:
    if sys.argv[2] == "-i":
        print('norminette '+sys.argv[1])
        stream = os.popen('norminette '+sys.argv[1])
        file = open(sys.argv[1],'r')
else:
    stream = os.popen('norminette temp.c')
    file = open("temp.c",'r')
output = stream.read()
print(output)
