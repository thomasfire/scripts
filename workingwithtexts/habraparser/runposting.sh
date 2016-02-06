#!/bin/bash

#parses resource from file and post to the VK group,and account from the file vk.settings

read resource < vk.settings
hour=3600

while [[ 1 ]]; do
  ./parse.sh $resource
  timeofsleeping=$RANDOM%$hour+$hour
  echo "sleeping ""$[timeofsleeping]"
  sleep $[timeofsleeping]s
done
