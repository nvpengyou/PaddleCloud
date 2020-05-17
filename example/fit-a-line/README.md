# fit-a-line（房价预测）示例
这是一个线性回归房价预测示例(单机示例)，本示例是基于paddle1.6版本，源代码[fit_a_line](https://github.com/PaddlePaddle/book/blob/for_paddle1.6/01.fit_a_line)， 示例说明文档[fit-a-line文档](https://github.com/PaddlePaddle/book/blob/for_paddle1.6/01.fit_a_line/README.cn.md)。

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

### 1、安装paddlecloud命令行工具


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
### 2、申请&配置token
- **免费使用**
   - 填入企业或组织邮箱，申请token，等待邮件通知
  
     ```
     paddlecloud gen_token --email=${your email}
     例如：paddlecloud gen_token --email=张三@163.com
     ```
     
   - 将邮件中的token填入客户端配置文件
   
   
     登陆自己的邮箱，查收Baidu PaddleCloud邮件，将如下内容全部复制并粘贴到~/bin/paddlecloud/conf/token.conf文件中（先找到该文件并用编辑器打开后在粘贴）
     ```shell
     // 注：如下内容仅为示例，以自己收到的邮件中的内容为准
     [token]
     userid: xxx
     ak: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     sk: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     ```
- **付费使用**

   [百度云BCC计费说明](https://cloud.baidu.com/doc/BCC/s/Ajy6x35ik)，PaddleCloud自动性价比较好的套餐
   - 百度云实名认证并开通BCC权限，在账号中提前充入部分资金

     按照百度云BCC文档完成 [BCC注册及实名认证](https://cloud.baidu.com/doc/BCC/s/3k4torn21#%E6%B3%A8%E5%86%8C%E5%8F%8A%E5%AE%9E%E5%90%8D%E8%AE%A4%E8%AF%81)
     - [注册](https://cloud.baidu.com/doc/UserGuide/s/ejwvy3fo2#%E6%B3%A8%E5%86%8C%E7%99%BE%E5%BA%A6%E8%B4%A6%E5%8F%B7)
     - [实名认证](https://cloud.baidu.com/doc/UserGuide/s/8jwvy3c96)
     
     注：仅需完成注册及实名认证即可，无需手动购买BCC，提交GPU训练任务时，PaddleCloud会自动帮您购买BCC GPU/CPU计算资源，并按照BCC的收费标准进行计费，PaddleCloud本身不产生额外费用
     
   - 配置百度云账号AK/SK
      - 先按照文档 [获取百度云AK/SK](https://cloud.baidu.com/doc/Reference/s/9jwvz2egb)（如果已拿到百度云AK/SK，可以跳过此步骤；此处的百度云AK/SK区别于免费的token）
      - 配置AK/SK
      

### 3、提交任务

  直接执行如下命令即可将任务提交到计算集群上运行
  ```shell
  // linux中使用该命令
  sh submit.sh
  ```
  也可以将submit.sh中的内容拿出来单独执行，例如：
  ```shell
  paddlecloud submit_job --files=job --start_cmd="sh run.sh"
  // --files用来指定本地代码和数据的目录，本地的job目录会被整体上传到计算集群中
  // --start_cmd指定任务的启动命令，该命令会在计算集群上被执行，注意：需要确保代码在script目录下
  ```
