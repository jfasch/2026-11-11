import os
import subprocess

def store_script(directory, name, script):
    with open(directory + '/' + name, 'w') as f:
        f.write(script)
        os.chmod(directory + '/' + name, 0o755)
    
def run_script(scriptname):
    result = subprocess.run([scriptname], shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout