import re
from replacer import replacer
from elements import *
f = open('InputProg.c', 'r')

i = f.read()
#Strip Comments
i = re.sub('//.*?\n|/\*.*?\*/', '', i, flags=re.S)


count = 0
program = i.split('\n')
result = {
    'keyword': [],
    'parenthesis': [],
    'identifier': [],
    'arithmetic_operator': [],
    'logical_operator': [],
    'constant': [],
    'punctuation': [],
    'comment': [],
}
for line in program:

    line = replacer(line)    
    
    tokens = line.split(' ')
    
    for token in tokens:
        # print(token)
        if '\r' in token:
            position = token.find('\r')
            token = token[:position]
        # print 1
        if token in datatype or token in keyword:
            result['keyword'].append(token)
        
        elif re.match('[A-Za-z][A-Za-z_$0-9]*', token) and '"' not in token:
            result['identifier'].append(token)    
        
        elif token in parenthesis:
            result['parenthesis'].append(token)

        elif token in punctuation:
            result['punctuation'].append(token)

        elif token in arithmetic_operator:
            result['arithmetic_operator'].append(token)

        elif token in logical_operator:
            result['logical_operator'].append(token)
        
        elif token.isdigit():
            result['constant'].append(token)

    # print("_______________________")

print(result)
f.close()
