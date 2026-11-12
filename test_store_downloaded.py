import utils

def test_basic(tmpdir):
    name = 'test1'

    script = '''
    #/bin/sh
    exit 0
    '''

    utils.store_script(tmpdir, name, script)

    f = open(tmpdir + '/' + name)
    content = f.read()
    assert content == script
