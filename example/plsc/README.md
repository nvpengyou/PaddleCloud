# PLSC飞桨大规模分类库示例
飞桨大规模分类库[PLSC](https://github.com/PaddlePaddle/PLSC)

## 代码结构

示例代码目录结构
```
.
├── job: 示例任务父目录，用paddlecloud命令行提交任务时配置--file=./job,可将该目录提交到计算集群上
│   ├── data: data目录用来存放训练和测试数据集的本地目录，提交训练任务后，该目录会被整体上传到计算集群中
│   │   ├── train_data: 训练数据集的目录，可将训练数据放到该目录下，提交任务时会将该目录上传（或者挂载）到集群的计算节点上
│   │   ├── label.txt: 
│   ├── run.sh: 训练任务的启动脚本，主要用来调起任务的python脚本，例如：python train.py，该脚本是在计算集群上被调用
│   ├── train.py: 具体的算法代码，此处的是plsc训练代码
│   ├── zip_reader.py: 读取zip的reader py文件
├── submit.sh: 提交任务的脚本，该脚本会调用paddlecloud命令行工具，将训练数据data和训练代码train.py/zip_reader.py、运行脚本run.sh提交到计算集群中，需要在自己的机器上执行，并且需要先下载并安装paddlecloud命令行工具，该脚本仅支持linux和mac上使用
```

说明


1）data目录用来存放训练和测试数据集的本地目录，提交训练任务后，该目录会被整体上传到计算集群中；该目录名称可以按需修改为其他名称，在训练代码中使用时需要相应修改。


2）train.py/zip_reader.py是训练相关的代码，run.sh是任务运行脚本，提交训练任务后，这些脚本都将被上传到集群中，并且在集群中运行


3）train_data和test_data是data的子目录，用来区分训练数据集和测试数据集，作为data的子目录，提交训练任务后，该目录会被整体上传到计算集群中。


在计算集群上获取该路径的方法是：
```python
LOCAL_DATA_PATH = os.getenv("LOCAL_MOUNT_PATH") # LOCAL_MOUNT_PATH内置的环境变量，直接获取该值即可
cluster_train_dir = LOCAL_DATA_PATH + "/data/train_data" # 计算节点上训练数据的路径
```

## 使用说明

### 1、安装paddlecloud命令行工具

   - 请自行安装Python3和pip3（Python3包安装和管理工具）

   - 安装python3环境依赖库
     ```shell
     pip3 install requests
     pip3 install rsa
     ```

   - 下载并安装命令行工具


     PaddleCloud当前只支持命令行方式使用，暂时还不支持web方式

     - **linux & mac**
     ```shell
     TODO
     ```

     - **Windows**

     TODO 下载地址待补充


     解压缩paddlecloud_stable.tar.gz，打开控制台并cd到当前目录，执行如下命令
     ```shell
     paddlecloud.bat
     ```
### 2、申请&配置token
- **免费使用**


   目前的免费策略，每位用户每天任务总运行时长不得超过100分钟，同时运行中的任务不能超过2个，每个任务运行时间限定不超过30分钟（将根据用户使用情况灵活调整）


   - 填入企业或组织邮箱，申请token，等待邮件通知
  
     ```
     paddlecloud gen_token --email=${your email}
     例如：paddlecloud gen_token --email=张三@163.com
     ```
     
   - 将邮件中的token填入客户端配置文件
   
   
     登陆自己的邮箱，查收Baidu PaddleCloud邮件，将token对应的ak/sk依次填入命令行中
     ```
     paddlecloud gen_token --email=xxxx@baidu.com
     create_token...
     Paste your ak here:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     Paste your sk here:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
     create_token done
     ```
     
     也可以将token对应的ak/sk复制并粘贴到~/bin/paddlecloud/conf/client.conf文件中（先找到该文件并用编辑器打开后在粘贴）
     ```shell
     // 注：如下内容仅为示例，以自己收到的邮件中的内容为准
     [main]
     debug = 0
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
      - 将百度云AK/SK填入命令行工具的配置文件
      打开安装目录在~/bin/paddlecloud/client.conf文件，将百度云AK/SK信息填入到该文件中
      ```shell
      [bcc]
      ak: // 私人的百度云虚拟化计算资源Access Key
      sk: // 私人的百度云虚拟化计算资源Secret Key
 
      [bos]:
      ak: // 私人的百度云虚拟化存储资源Access Key
      sk: // 私人的百度云虚拟化存储资源Secret Key
      ```
      此处的两套AK/SK可以保持一致
      

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
  // --start_cmd指定任务的启动命令，该命令会在计算集群上被执行
  ```
### 4. 查看任务详情
```json
$ paddlecloud query_job --job_id=job-0650470e621f3688812ceda2079805f8

bos_url: paddlecloud-public.bj.bcebos.com/5a87a46f65608389bb42f5fed165f3c1/plsc
create_time: 2020-05-17 18:15:28
error_msg:
finish_time: 2020-05-17 18:21:11
instance_count: 1
instance_ids_list:
job_id: job-0650470e621f3688812ceda2079805f8
job_name: tmp_job
job_status: success
job_type: gpu
kill_flag: 0
public_bcc: 1
public_bos: 1
queue_reason:
start_cmd: sh run.sh
start_time: 2020-05-17 18:15:47
wall_time: 00:30:00
```
### 5. 查看作业目录
```json
$ paddlecloud get_files --job_id=job-0650470e621f3688812ceda2079805f8

output/job-0650470e621f3688812ceda2079805f8/	0	2020-05-17T10:15:39Z
output/job-0650470e621f3688812ceda2079805f8/log/trainer-0.log	5453	2020-05-17T10:16:09Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/@LR_DECAY_COUNTER@	32	2020-05-17T10:16:09Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_0.b_0	280	2020-05-17T10:16:01Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_0.b_0_velocity_0	280	2020-05-17T10:16:09Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_0.w_0	280	2020-05-17T10:16:01Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_0.w_0_velocity_0	280	2020-05-17T10:16:09Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_0.w_1	280	2020-05-17T10:16:01Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_0.w_2	280	2020-05-17T10:16:01Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_1.b_0	280	2020-05-17T10:16:01Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_1.b_0_velocity_0	280	2020-05-17T10:16:09Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_1.w_0	280	2020-05-17T10:16:01Z
output/job-0650470e621f3688812ceda2079805f8/rank-0/0/batch_norm_1.w_0_velocity_0	280	2020-05-17T10:16:09Z
....
```

### 6. 查看作业日志

- 下载作业日志
```json
$ paddlecloud get_files --job_id=job-0650470e621f3688812ceda2079805f8 --prefix=output/job-0650470e621f3688812ceda2079805f8/log --download=1
```

- 查看日志列表
```json
$ ll output/job-0650470e621f3688812ceda2079805f8/log/

drwxrwxr-x 2 work work 4096 May 17 19:08 ./
drwxrwxr-x 3 work work 4096 May 17 19:08 ../
-rw-rw-r-- 1 work work 5453 May 17 19:08 trainer-0.log
```

- 查看日志
```json
$ cat output/job-0650470e621f3688812ceda2079805f8/log/trainer-0.log
```
