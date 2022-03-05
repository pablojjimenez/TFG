#!/bin/bash

function usage {
    echo "==============================================================================="
    echo "usage: $0 [keyword]"
    echo "*   keyword:    test class name or test function name or test file name"
    echo "==============================================================================="
}

# Store the exit status of the pytest commands: 0 success, 1 failure
status=0

function save_status {
    # Save the test status (if failed)
    if [ $? -eq 1 ]; then status=1; fi
}


usage

# activate test environment
. test_venv/bin/activate

# run all the tests under the 'tests' folder
if [ "$1" != "" ]; then
  python -m pytest -v tests -k "$1"
else
  python -m pytest -v tests
fi

save_status

# deactivate virtual env
deactivate

exit ${status}
