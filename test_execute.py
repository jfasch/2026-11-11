import utils
import os

def test_basic(tmpdir):
    scriptname = tmpdir / 'test'

    f = open(scriptname, 'w')
    f.write('echo hallo\n')
    f.close()
    os.chmod(scriptname, 0o755)

    exit_status, stdout = utils.run_script(scriptname)

    assert exit_status == 0
    assert stdout == 'hallo\n'
