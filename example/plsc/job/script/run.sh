#!/bin/bash
ln -s $LOCAL_MOUNT_PATH/train_data train_data
python train.py --model_dir=$OUTPUT_PATH
