#!/usr/bin/bash
cd C:/Users/user/Desktop/intern/quantium-starter-repo/virtual_env/Scripts/automation_test
. ./virtual_env/Scripts/activate

python -m pytest test_tasks.py 

PYTEST_EXIT_CODE =$?

if [$PYTEST_EXIT_CODE -eq 0]
then 
   exit 0 
else
    exit 1
fi    