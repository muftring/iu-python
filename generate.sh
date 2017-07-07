#!/bin/bash

function Usage
{
cat << __USAGE__
Usage: `basename $0`

Options:

  -m M        module number
  -q          (the rest of the command line are the question numbers)

__USAGE__
}

MODULE=

while [ "$1" != "" ]
do
  case $1 in
   '-?' )
      Usage
      exit 0
      ;;
    -m )
      MODULE=$2
      shift
      ;;
    -q )
      shift
      break
      ;;
  esac
  shift
done

if [ "$MODULE" == "" ]
then
  Usage
  exit 0
fi

QUESTIONS=$@

MODDIR=`printf "module-%02d" $MODULE`
echo "MODDIR: $MODDIR"
echo "Questions: $QUESTIONS"

mkdir -p $MODDIR

for i in $QUESTIONS
do  
  file=$MODDIR/Question$i.py
  touch $file
  cat header.txt | sed -e "s=%A%=$MODULE=g" -e "s=%Q%=$i=g" >> $file
  chmod 755 $file
done
