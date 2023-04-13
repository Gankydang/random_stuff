import re

filename = 'random_file.py'

with open('random_file.py') as f:
    text = []
    multiline = ''
    found_multiline = False
    quote_to_check = ''
    for line in f.readlines():
        if len(re.findall("'''|\"\"\"", line)) >= 2 and not found_multiline:
            text.append(line.strip())
        
        if "'''" in line and not found_multiline:
            found_multiline = not found_multiline
            multiline += line
            quote_to_check = "'''"
            continue
        elif '"""' in line and not found_multiline:
            found_multiline = not found_multiline
            multiline += line
            quote_to_check = '"""'
            continue
            
        if found_multiline:
            if quote_to_check in line:
                multiline += line
                text.append(multiline.strip())
                multiline = ''
                found_multiline = False
                quote_to_check = ''
            else:
                multiline += line
        else:
            text.append(line.strip())
    for line in text:
        i = text.index(line)
        if '#' in line:
            all_occurances_of_comments = re.findall(r".*\"\"\"[\s\S]*#[\s\S]*\"\"\".*|.*'''[\s\S]*#[\s\S]*'''.*|'.*#.*'|\".*#.*\"|#.*", line)
            
            for occurance in all_occurances_of_comments[::-1]:
                if occurance[0] == '#':
                    line = line.replace(occurance, '')
            text[i] = line
    code_without_comments = '\n'.join(text)
    
with open(filename, 'w') as f:
    f.write(code_without_comments)