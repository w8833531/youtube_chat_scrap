#!/bin/bash

#Usage: This script use to list live chat user country.
##       add video_id in video_id.txt and run this script
##       and you will get a list sorted by Country numbers

#Author: LarryWu
#Date: 12/20/2018
channel_file=channel_id.txt
country_file=country.txt
result_file=result.txt

### active python first, point to you python venv path
. /root/python2.7.6/bin/activate

### add video_ids commont's channel_ids to channel_file
> ${channel_file}
python live_chat_channel.py >> ${channel_file}
cp ${channel_file} ${channel_file}.tmp
cat ${channel_file}.tmp |grep 'UC' | sort -u > ${channel_file}  

### add channel_id's country to country_file
> ${country_file}
for id in `cat ${channel_file} | awk -F': ' '{print $2}'`
do
  i=$[i+1]
  echo "$i," >> ${country_file}
  python channel.py --action='list' --channel_id=${id} --noauth_local_webserver >> ${country_file}
done

### get country count result
cat ${country_file} | awk -F, '/^UC/ {++state[$NF]} END {for(key in state) print state[key],",",key}' | sort -nr > ${result_file}
