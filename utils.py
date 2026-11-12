import os

def store_script(tmpdir, name, script):
    with open(tmpdir + '/' + name, 'w') as f:
        f.write(script)
        #make the script executable
        os.chmod(tmpdir + '/' + name, 0o755)
    