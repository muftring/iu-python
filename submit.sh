#!/bin/bash

MODULE=
SRC_ROOT=$HOME/git/iu-python
ZIP_ROOT=$HOME/Documents/schools/IndianaU/Python

while [ "$1" != "" ]
do
  case $1 in
    -m )
      MODULE=$2
      shift
      ;;
  esac
  shift
done

if [ "$MODULE" == "" ]
then
  echo "Error - module not specified"
  exit 1
fi

MOD_DIR=`printf "module-%02d" $MODULE`
ZIP_DIR=$ZIP_ROOT/$MOD_DIR
ZIP_FILE=muftring_assignment$MODULE.zip

SWD=`pwd`
cd $SRC_ROOT/$MOD_DIR
pwd
zip $ZIP_DIR/$ZIP_FILE *
cd $SWD

