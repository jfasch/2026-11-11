def store_script(tmpdir, name, script):
    with open(tmpdir + '/' + name, 'w') as f:
        f.write(script)