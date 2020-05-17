#!/bin/bash
# 解压数据
cp $LOCAL_MOUNT_PATH/ERNIE.tar.gz .
tar xzf ERNIE.tar.gz

cp $LOCAL_MOUNT_PATH/CoLA.zip .
unzip CoLA.zip

cp $LOCAL_MOUNT_PATH/ERNIE_Base_en_stable-2.0.0.tar.gz .
tar xzf ERNIE_Base_en_stable-2.0.0.tar.gz

# 设置数据和模型目录
work_dir=$(pwd)
export TASK_DATA_PATH=$work_dir
export MODEL_PATH=$work_dir

cd ERNIE
# 设置输出和日志目录
ln -s $OUTPUT_PATH output
ln -s $LOCAL_LOG_PATH log

# 运行
sh script/en_glue/ernie_base/CoLA/task.sh
