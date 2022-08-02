def replacer(line):
    if ',' in line:
        line = line.replace(","," , ")
    
    if ';' in line:
        line = line.replace(";"," ; ")
    
    if ':' in line:
        line = line.replace(":"," : ")

    if '+' in line:
        line = line.replace("+"," + ")

    if '-' in line:
        line = line.replace("-"," - ")

    if '*' in line:
        line = line.replace("*"," * ")

    if '/' in line:
        line = line.replace("/"," / ")
        
    if ('=' in line) and not (("!=" in line) or ("==" in line) or ("<=" in line) or (">=" in line) ):
        line = line.replace("="," = ")
    
    if '==' in line:
        line = line.replace("=="," == ")

    if '<=' in line:
        line = line.replace("<="," <= ")

    if '>=' in line:
        line = line.replace(">="," >= ")
        
    if '!=' in line:
            line = line.replace("!="," != ")
    if '(' in line:
            line = line.replace("("," ( ")
    if ')' in line:
            line = line.replace(")"," ) ")   
    
    if '()' in line:
            line = line.replace("()"," () ")
            
    if '{}' in line:
            line = line.replace("{}"," {} ")
    
    return line