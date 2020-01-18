from sys import argv
import re
import subprocess

folder_name = "imgs/"

def format_name(name):
    return "![" + name +"]("+ folder_name + name+")"

name_re = re.compile('[^/\\\\\\\n]+$')

if len(argv) < 2:
    result = "![ERROR](error)"
else:
    name = name_re.findall(argv[1])
    if len(name) < 1:
        result = "![ERROR](error)"
    result = format_name(name[0])
    
# only for windows
subprocess.Popen("clip",stdin=subprocess.PIPE).stdin.write(result.encode('GBK'))