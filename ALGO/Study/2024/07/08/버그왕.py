import sys
import re


def remove_bug(code):
    while True:
        code = re.sub(r'BUG', '', code)
        
        if 'BUG' not in code:
            break
    return code


def bug_king(code_lines):
    for code in code_lines:
        remove_bug_code = remove_bug(code)
        print(remove_bug_code, end='')
        
        
if __name__ == "__main__":
    code_lines = sys.stdin.readlines()
    
    bug_king(code_lines)