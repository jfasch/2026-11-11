import os

def store_script(directory, name, script):
    with open(directory + '/' + name, 'w') as f:
        f.write(script)
        os.chmod(directory + '/' + name, 0o755)
    
