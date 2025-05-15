import os
import subprocess
import sys

def exec(id_or_file):
    if not id_or_file.endswith('.py'):
        id_or_file += '.py'
    path = os.path.join(os.path.dirname(__file__), 'programs', id_or_file)
    if not os.path.exists(path):
        print(f"[!] Program '{id_or_file}' not found.")
        return
    with open(path, 'r') as f:
        code = f.read()
        try:
            exec(code, globals())
        except Exception as e:
            print("[!] Error running the program:", e)

def copy(id_or_file):
    if not id_or_file.endswith('.py'):
        id_or_file += '.py'
    path = os.path.join(os.path.dirname(__file__), 'programs', id_or_file)
    if not os.path.exists(path):
        print(f"[!] Program '{id_or_file}' not found.")
        return
    with open(path, 'r') as f:
        code = f.read()

    try:
        if sys.platform == "win32":
            cmd = f'echo {code.strip()}| clip'
            os.system(cmd)
        elif sys.platform == "darwin":
            subprocess.run("pbcopy", input=code.encode(), check=True)
        else:
            subprocess.run("xclip -selection clipboard", input=code.encode(), shell=True, check=True)
        print(f"[+] '{id_or_file}' copied to clipboard.")
    except Exception as e:
        print("[!] Copy failed:", e)
