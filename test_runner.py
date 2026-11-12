import utils
import os


def test_basic(tmpdir):
    test_scripts_dir = tmpdir / 'test-scripts'
    test_scripts_dir.mkdir()

    test_report_dir = tmpdir / 'test-reports'
    test_report_dir.mkdir()

    open(test_scripts_dir / 'test1', 'w').write(
    """
    #!/usr/bin/python

    import sys
    sys.exit(1)
    """
    )
    os.chmod(test_scripts_dir / 'test1', 0o755)

    open(test_scripts_dir / 'test2', 'w').write(
    """
    #!/bin/sh

    echo hallo
    exit 42
    """
    )
    os.chmod(test_scripts_dir / 'test2', 0o755)

    open(test_scripts_dir / 'test3', 'w').write(
    """
    #!/usr/bin/python

    import sys
    sys.exit(1)
    """
    )
    os.chmod(test_scripts_dir / 'test3', 0o755)

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>
    runner = utils.TestRunner(scriptsdir=test_scripts_dir, reportsdir=test_report_dir)
    runner.run()
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<

    test1_rptfile = test_report_dir / 'test1-jsonrpt'
    test2_rptfile = test_report_dir / 'test2-jsonrpt'
    test3_rptfile = test_report_dir / 'test3-jsonrpt'

    assert test1_rptfile.is_file()
    assert test2_rptfile.is_file()
    assert test3_rptfile.is_file()

    assert json.load(test1_rptfile) == {'exitcode': 1, 'stdout': ''}
    assert json.load(test2_rptfile) == {'exitcode': 42, 'stdout': 'hallo\n'}
    assert json.load(test3_rptfile) == {'exitcode': 1, 'stdout': ''}
