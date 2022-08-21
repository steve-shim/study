#!/bin/bash

echo "This script file $0"
echo "Argument Count is $#"
echo "Process ID is $$"
echo "Argument List \$*: $*"
echo "Argument List \$@: $@"
echo "Argument 1: $1"
echo "Argument 2: $2"
echo "Argument 3: $3"

for args in $*
do 
    echo 인자:$args
done
