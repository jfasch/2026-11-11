import pytest


@pytest.mark.skip(reason='entire process not yet defined')
def test_entire_process():

    # 1. get list of tests, and download (a subset of) those
    all_tests = test_repo.tests_of_suite('suite-1')

    assert all_tests == [
        'test1.py',
        'test2.sh',
        'test3',
    ]

    test_repo.download_tests('suite-1', all_tests, destination_dir)
    # test_repo.download_tests('suite-1', ['test1.py'])

    """
    #!/usr/bin/python

    import sys
    sys.exit(1)
    """

    """
    #!/bin/sh

    exit 42
    """

    """
    #!/usr/bin/python

    import sys
    sys.exit(1)
    """

    # 2. execute tests in destination_dir, and gather exit
    # statuses. this leads to something like ...
    exit_statuses = {
        'test1.py': 1,
        'test2.sh': 42,
        'test3': 1,
    }

    # 3. convert this information to json ...
    json_results_blah = """
    {
        "test1.py": 1,
        "test2.sh": 42,
        "test3": 1
    }
    """

    # 4. upload test results
    test_repo.upload_results('suite-1', xxx)


@pytest.mark.skip(reason='download not yet defined')
def test_download():

    # in real life, there is a http web api server out there which has
    # a fixed entry point for us to retrieve the list of python
    # scripts to download in the next step

    response = requests.get('https://web.com/test-repo/suite-1/list')
    test_scripts_thing = response.json()

    # test_scripts_thing should look like so ...
    
    """
    {
        "version": 1,
        "scripts": [ "test1.py", "test2.py" ]
    }
    """

    scripts = [
        'test1.py',
        'test2.py',
        # ...
    ]

    assert False, "todo: download"

@pytest.mark.skip(reason='download not yet defined')
def test_execute():
    assert False, "todo: execute"

@pytest.mark.skip(reason='download not yet defined')
def test_json_result():
    assert False, "todo: json"

@pytest.mark.skip(reason='download not yet defined')
def test_upload_result():
    assert False, "todo: upload"
