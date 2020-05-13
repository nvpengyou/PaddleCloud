# fit-a-line（房价预测）示例
这是一个线性回归房价预测示例，本示例是基于paddle1.6版本，源代码[fit_a_line](https://github.com/PaddlePaddle/book/blob/for_paddle1.6/01.fit_a_line)， 示例说明文档[fit-a-line文档](https://github.com/PaddlePaddle/book/blob/for_paddle1.6/01.fit_a_line/README.cn.md)。

## 代码结构

示例代码目录结构
.
├── job: 示例任务父目录，用paddlecloud命令行提交任务时配置--file=./job,可将任务的提交到集群上
│   ├── data
│   │   ├── train_data: 训练数据集的目录，可将训练数据放到该目录下，提交任务时会将该目录上传（或者挂载）到集群的计算节点上
│   │   ├── test_data: 测试数据集的目录，可将测试数据放到该目录下，提交任务时会将该目录上传（或者挂载）到集群的计算节点上
│   ├── script
│   │   ├── run.sh: 训练任务的启动脚本，主要用来调起任务的python脚本，例如：python train.py，该脚本是在计算集群上被调用
│   │   ├── train.py: 具体的算法代码，此处的是房价预测的paddle组网代码
├── submit.sh: 提交任务的脚本，需要在自己的机器上执行，并且需要先下载并安装paddlecloud命令行工具，该脚本仅支持linux和mac上使用

其中
train_data和test_data在计算节点上获取该路径的方法
```python
LOCAL_DATA_PATH = os.getenv("LOCAL_MOUNT_PATH") # LOCAL_MOUNT_PATH内置的环境变量，直接获取该值即可
cluster_train_dir = LOCAL_DATA_PATH + "/data/train_data" # 计算节点上训练数据的路径
```

## 使用说明

- 下载paddlecloud命令行工具
todo

- 配置命令行工具
todo

- 提交任务
```shell
sh submit.sh
```
