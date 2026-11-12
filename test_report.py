import utils
import json

def test_basic():
    exitcode, stdout = 42, "not ok\ntoo stupid\n"

    jsonreport = utils.make_json(exitcode, stdout)

    assert json.loads(jsonreport) == {
        'exitcode': exitcode,
        'stdout': stdout,
    }
