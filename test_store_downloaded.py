import utils
import os

def test_basic(tmpdir):
    name = 'test1'

    script = '''
    #/bin/sh
    exit 0
    '''

    utils.store_script(tmpdir, name, script)

    script_path = tmpdir + '/' + name

    # verify that content is as desired
    f = open(script_path)
    content = f.read()
    assert content == script

    # verify that we have execute-permissions
    assert os.access(script_path, os.X_OK)
