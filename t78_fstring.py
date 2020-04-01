# -*- coding: utf-8 -*-

#import os.path

def effify(non_f_str: str) -> str:
    return eval(f'f"""{non_f_str}"""')

footer = '''
    // shift register
    // {project}
    // {userdir}
'''    

project = "s6s090a"
userdir = "kangjoo.kim"

footer = effify(footer)
print(footer)
