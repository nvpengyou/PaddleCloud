#!/bin/bash
# 1) wget https://ppoc-filecenter.cdn.bcebos.com/ernie.zip
# 2) unzip -q ernie.zip
# 3) cd ernie
# 4) mv * ./job

if [[ ! -f "./job/CoLA.zip" && ! -f "./job/ERNIE_Base_en_stable-2.0.0.tar.gz" && ! -f "./job/ERNIE.tar.gz" ]]; then
    echo "Please download https://ppoc-filecenter.cdn.bcebos.com/ernie.zip && unzip ernie.zip && cd ernie && mv * ./job"
    exit -1
fi

paddlecloud submit_job --files=job --start_cmd="sh run.sh"
