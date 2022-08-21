#!bin/bash

var=        # var is null -> test1.sh  var.sh
var=pwd     # var is pwd  -> /c/advan_shim/shell
echo ${var:=ls}     # echo $var -> pwd 저장
echo ${var2:-temp}  # echo $var2 -> 저장x
