#!/bin/bash

py_files=$(find . -type f -name "*.py" | grep -E ".*\.py$" | cut -c 3-)

if [[ $# -eq 0 ]]; then
    for file in $py_files;
    do 
        black $file
    done

    for file in $py_files;
    do 
        flake8 $file
    done

elif [[ $1 -eq 1 ]]; then
    for file in $py_files;
    do 
        black $file
    done

elif [[ $1 -eq 2 ]]; then
    for file in $py_files;
    do 
        flake8 $file
    done
fi


