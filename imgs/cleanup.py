from glob import glob
import os
import re

# image in this dir will be delete
image_path = '.'
# .md files in this dir will be checked
markdown_path = '..'

reg_find = re.compile(r'!\[[^\]]*\]\(([^\)]+)\)')

escape_re = re.compile('[^/\\\\\\\n]+$')
def escape_file(f):
    return escape_re.findall(f)[0]
    
used = []

for (dname, dpath, fname) in os.walk(markdown_path):
    for f in [os.path.join(dname, f) for f in fname if f.endswith('.md')]:
        # print(f)
        with open(f, 'rb') as file:
            iterator = reg_find.finditer(file.read().decode('utf-8'))
            for match in iterator:
                used.append(escape_file(match.group(1)))
# print(used)

folder_files = []

for (dname, dpath, fname) in os.walk(image_path):
    for f in [os.path.join(dname, f) for f in fname if f.endswith('.png') or f.endswith('.jpg')]:
        folder_files.append(f)
        
# print(folder_files)

deletes = []


def is_same_file(a,b):
    return escape_file(a) == escape_file(b)

for file in folder_files:
    if not escape_file(file) in used:
        deletes.append(file)

result = 'rm'
for d in deletes:
    result += ' '
    result += d
print(result)