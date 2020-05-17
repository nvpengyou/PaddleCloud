# ERNIE(语义理解预训练)示例
[ERNIE](https://github.com/PaddlePaddle/ERNIE/blob/develop/README.zh.md)是基于持续学习的语义理解预训练框架


使用该示例前，请先将该代码整体下载到本地，该示例是单机单卡示例，预计运行时间20分钟左右


## 代码结构

该示例的数据和代码文件较大，并没有直接将数据和代码放入本示例目录中，请先将其[下载ernie.zip](https://ppoc-filecenter.cdn.bcebos.com/ernie.zip)到本地，然后代码下面的代码结构说明来组织和提交任务


ernie.zip文件解压后结构如下：
```
CoLA.zip
ERNIE_Base_en_stable-2.0.0.tar.gz
ERNIE.tar.gz
script/
```

将上述文件（解压缩后的全部文件）拷贝到job目录

示例代码目录结构
```
.
├── job: 示例任务父目录，用paddlecloud命令行提交任务时配置--file=./job,可将该目录提交到计算集群上
│   ├── [CoLA.zip] 训练和测试数据集文件
│   ├── [ERNIE_Base_en_stable-2.0.0.tar.gz] ERINE base模型文件
│   ├── [ERNIE.tar.gz] ERINE组网代码
│   ├── script: 算法及训练脚本目录，提交训练任务后，该目录会被整体上传到计算集群中，注意：该目录名称不可修改
│   │   ├── run.sh: 训练任务的启动脚本，主要用来调起任务的python脚本，例如：python train.py，该脚本是在计算集群上被调用
├── submit.sh: 提交任务的脚本，该脚本会调用paddlecloud命令行工具，将训练数据data和训练代码script提交到计算集群中，需要在自己的机器上执行，并且需要先下载并安装paddlecloud命令行工具，该脚本仅支持linux和mac上使用
```

说明


1）data目录用来存放训练和测试数据集的本地目录，提交训练任务后，该目录会被整体上传到计算集群中；该目录名称可以按需修改为其他名称，在训练代码中使用时需要相应修改。


2）script: 算法及训练脚本目录，提交训练任务后，该目录会被整体上传到计算集群中，注意：该目录名称不可修改


3）train_data和test_data是data的子目录，用来区分训练数据集和测试数据集，作为data的子目录，提交训练任务后，该目录会被整体上传到计算集群中。


在计算集群上获取该路径的方法是：
```python
LOCAL_DATA_PATH = os.getenv("LOCAL_MOUNT_PATH") # LOCAL_MOUNT_PATH内置的环境变量，直接获取该值即可
cluster_train_dir = LOCAL_DATA_PATH + "/data/train_data" # 计算节点上训练数据的路径
