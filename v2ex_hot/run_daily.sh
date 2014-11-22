#! usr/bin/env/bash

today=`date '+%Y%m%d'`
datapath='/Users/kid177/xujian/toy/v2ex_hot/data'
binpath='/Users/kid177/xujian/toy/v2ex_hot'
userdata=$datapath/user
nodedata=$datapath/node
rawdata=$datapath/rawdata
postsdata=$datapath/postsdata

mkdir -p $userdata
mkdir -p $nodedata
mkdir -p $rawdata
mkdir -p $postsdata

cd $binpath

python v2ex_hot_spider.py $userdata/$today $nodedata/$today $postsdata/$today $rawdata/$today

if [ -f $userdata/$today ]; then
    ln -s $userdata/$today user_data
fi

if [ -f $nodedata/$today ]; then
    ln -s $nodedata/$today node_data
fi

if [ -f $postsdata/$today ]; then 
    ln -s $postsdata/$today posts_data
fi

if [ -f $rawdata/$today ]; then
    ln -s $rawdata/$today raw_data
fi
