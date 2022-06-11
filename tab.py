import sys


""" const """
#variable et fonctions
varname =["int","bool","char","void","int","int",]
#sign tp get space left and right
sign =[">=","<=","==","!=","||","&&","+","-","/",">","<","%","="]
signChilds = [">","<"]
#sign tp get space right
signr =[","]
signs =[",","("]
#statement and loop
statement = ["if","while","else if","if","="]
#cheat
cheat = ["printf","\tfor(","\tfor ("]


""" string compare, return word detect """
def anyin(a,b):
    for i in a:
        if i in b:
            return i
    return "null"



# def save(filen):
#     global counter
#     if "-i" in sys.argv:
#         file = open(filen,'w')
#         file.write(''.join(lines))
#     else:
#         open(f"/Users/albaud/Desktop/temp/{counter}temp.c","w").write(''.join(lines))
#         counter+=1

""" plus utile si on fait tout ?? """
def tabs():
    global lines
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

""" espace fonction """
def func():
    funcs = []
    for i in range(len(lines)):
        temp = lines[i]
        temp = temp.replace("\t","")
        temp = temp.split(" ")
        cas = False

        if (temp[0] in varname):
            if ';' in lines[i] and temp[0]== "int":
                lines[i] = lines[i].replace(" ","\t\t",1)
            else:
                lines[i] = lines[i].replace(" ","\t",1)
            cas = True


""" space en trop ? """
def keywordSpace():
    global lines
    for i in range(len(lines)):
        stat = anyin(statement,lines[i])
        if stat != "null":
            temp = lines[i].split(stat)
            if temp[1][0] != ' ':
                temp[1] = ' ' +temp[1]
            lines[i] = stat.join(temp)


""" random """
def finalClean():
    global lines
    for i in range(len(lines)):
        print(i)
        tabacount = 0;
        lines[i] = lines[i].replace('  ',' ')
        temp = lines[i]

        while temp[0] == "\t":
            temp = temp[1:]
            tabacount+=1
        temp = lines[i].replace(' ','').replace('\t','')
        if temp == "\n":
            lines[i] = temp
        if lines[i] == "\n":
            if i > 0 and i < len(lines):
                if "include" not in lines[i-1] and anyin(varname,lines[i-1]) == "null" and ('}\n' not in lines[i-1] or anyin(varname,lines[i+1])== "null"):

                    lines[i] = ""
        try:
            if temp == '}\n' and "void" in lines[i+1]:
                lines.insert(i+1,"\n")
        except:
            pass
        if '{\n' in temp and  temp != '{\n':
            lines[i] = lines[i][:len(lines[i])-2] + "\n"
            ress = '\t'*tabacount
            lines.insert(i+1,ress+"{\n")
        if anyin(varname,lines[i]):
            lines[i] = lines[i].replace('()','(void)')
        lines[i] = lines[i].replace(' \n','\n')
        lines[i] = lines[i].replace('  \n','\n')
        lines[i] = lines[i].replace('   \n','\n')
        lines[i] = lines[i].replace('    \n','\n')
        tem = anyin(cheat,lines[i])
        if anyin(cheat,lines[i]) != "null":
            print("CHEAT")
    while lines[len(lines)-1] == '\n':
        lines.pop()




