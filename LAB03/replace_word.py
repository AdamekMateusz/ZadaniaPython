# with open('2nd Panzer Group.txt', 'r') as filename:
#   file_data = filename.readlines()	# Or filename.read() 

# print(file_data)

# with open("text.txt",'r') as file_in:
#     lines = []
#     for line in file_in:
#         line  = line.replace('i','oraz')
#         line = line.replace('oraz','i')
#         line = line.replace('nigdy','prawie nigdy')
#         line = line.replace('dlaczego','czemu')
#         lines.append(line)

# print(lines)

import re

replacements = {r'\bi\b':'oraz', 
                r'\boraz\b':'i',
                r'\bnigdy\b':'prawie nigdy',
                r'\bdlaczego\b':'czemu'}

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