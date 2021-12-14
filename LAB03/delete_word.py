import re

# with open("text.txt",'r') as file_in:
#     lines = []
#     for line in file_in:
#         line  = line.replace('się','')
#         line = line.replace('i','')
#         line = line.replace('oraz','')
#         line = line.replace('nigdy','')
#         line = line.replace('dlaczego','')
#         lines.append(line)

# print(lines)

# replacements = {'się':'', 
#                 'i':'',
#                 'oraz':'',
#                 'nigdy':'',
#                 'dlaczego':''
#                 }

replacements = {r'\bsię\b':'', 
                r'\bi\b':'',
                r'\boraz\b':'',
                r'\bnigdy\b':'',
                r'\bdlaczego\b':''}

def replace_all(text, dic):
    for i, j in dic.items():
        text = re.sub(i,j,text)
    return text


with open("text.txt",'r') as file_in:
    lines = []
    for line in file_in:
        line = replace_all(line, replacements)
        lines.append(line)
print(lines)