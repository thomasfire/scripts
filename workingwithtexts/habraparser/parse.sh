#!/bin/bash

#parses needed resource

args=$@

./parsehabrlinks.py "https://"${args[0]}".ru/all/"

while read list
do
  ./habraparser.py $list
  echo $list" Done!"
done  < ${args[0]}".links"
