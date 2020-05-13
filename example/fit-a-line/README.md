# fit-a-line（房价预测）示例
这是一个线性回归房价预测示例，本示例是基于paddle1.6版本，源代码[fit_a_line](https://github.com/PaddlePaddle/book/blob/for_paddle1.6/01.fit_a_line)， 示例说明文档[fit-a-line文档](https://github.com/PaddlePaddle/book/blob/for_paddle1.6/01.fit_a_line/README.cn.md)。

## 代码结构

示例代码目录结构
```
.
├── job: 示例任务父目录，用paddlecloud命令行提交任务时配置--file=./job,可将该目录提交到计算集群上
│   ├── data: data目录用来存放训练和测试数据集的本地目录，提交训练任务后，该目录会被整体上传到计算集群中
│   │   ├── train_data: 训练数据集的目录，可将训练数据放到该目录下，提交任务时会将该目录上传（或者挂载）到集群的计算节点上
│   │   ├── test_data: 测试数据集的目录，可将测试数据放到该目录下，提交任务时会将该目录上传（或者挂载）到集群的计算节点上
│   ├── script: 算法及训练脚本目录，提交训练任务后，该目录会被整体上传到计算集群中，注意：该目录名称不可修改
│   │   ├── run.sh: 训练任务的启动脚本，主要用来调起任务的python脚本，例如：python train.py，该脚本是在计算集群上被调用
│   │   ├── train.py: 具体的算法代码，此处的是房价预测的paddle组网代码
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
```

## 使用说明

- 安装paddlecloud命令行工具


   - 安装python3环境和依赖库
```shell
yum install python3
pip3 install requests
pip3 install rsa
```

   - 下载并安装命令行工具（PaddleCloud当前只支持命令行方式使用，暂时还不支持web方式）


```shell
TODO
```
- 配置命令行工具
   - 填入企业或组织邮箱，申请token，等待邮件通知
  
  
     TODO
   - 将邮件中的token填入客户端配置文件
   
   
     TODO

- 提交任务
```shell
sh submit.sh
```
