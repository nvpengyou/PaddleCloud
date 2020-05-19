
# 使用手册

* [前言](#前言)
* [准备环境](#准备环境)
* [申请&配置token](#申请&配置token)
* [快速开始](#快速开始)
* [功能介绍](#功能介绍)
   * [申请token](#申请token)
   * [创建任务](#创建任务)
   * [查询任务](#查询任务)
   * [结束任务](#结束任务)
   * [查看结果](#查看结果)
* [环境变量说明](#环境变量说明)
* [FAQ](#FAQ)


## 前言
PaddleCloud能够帮助您一键发起深度学习任务，为您提供免费底层计算资源、或提供快速打通云上计算资源通道，支持您快速发起单机/分布式Paddle框架训练任务，致力于推动AI应用更广泛地落地。



## 准备环境
- 安装python3环境和依赖库


  1）自行安装Python3和pip3（Python3包安装和管理工具）


  2）安装Python依赖库
  ```shell
  pip3 install requests
  pip3 install rsa
  ```

- 下载命令行工具


  PaddleCloud当前只支持命令行方式使用，暂时还不支持web方式

  **linux & mac**
  
  
  ```
  bash -c "$(curl -X GET http://ppoc-filecenter.bj.bcebos.com/install_paddlecloud_stable.sh)"; source ~/.bashrc
  ```
  

  **Windows**

  
  暂未开放，敬请期待
  
  
## 申请&配置token

- **免费使用**


   目前的免费策略，每位用户每天任务总运行时长不得超过100分钟，同时运行中的任务不能超过2个，每个任务运行时间限定不超过30分钟（将根据用户使用情况灵活调整） 


   操作步骤：
 
 
   1）填入企业或组织邮箱，申请token，等待邮件通知
   ```shell
   paddlecloud gen_token --email=<your email>
   例如：paddlecloud gen_token --email=your_name@163.com
   ```
 
   2）将邮件中的token填入命令行工具的配置文件
   
   
     登陆自己的邮箱，查收Baidu PaddleCloud邮件，将token对应的ak/sk依次填入命令行中
     ```
     paddlecloud gen_token --email=<your email>
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


  支持使用百度云付费GPU（付费BCC GPU虚拟机）按需跑训练任务，仅在任务运行过程中收取BCC GPU虚拟机费用，任务运行完自动结束计费 


  操作步骤：


  1）百度云实名认证并开通BCC权限，在账号中提前充入部分资金
    按照百度云BCC文档完成 [BCC注册及实名认证](https://cloud.baidu.com/doc/BCC/s/3k4torn21#%E6%B3%A8%E5%86%8C%E5%8F%8A%E5%AE%9E%E5%90%8D%E8%AE%A4%E8%AF%81)
    - [注册](https://cloud.baidu.com/doc/UserGuide/s/ejwvy3fo2#%E6%B3%A8%E5%86%8C%E7%99%BE%E5%BA%A6%E8%B4%A6%E5%8F%B7)
    - [实名认证](https://cloud.baidu.com/doc/UserGuide/s/8jwvy3c96)
     
     注：仅需完成注册及实名认证即可，无需手动购买BCC，提交GPU训练任务时，PaddleCloud会自动帮您购买BCC GPU/CPU计算资源，并按照BCC的收费标准进行计费，PaddleCloud本身不产生额外费用


  2）配置百度云账号ak/sk
     - 先按照文档 [获取百度云AK/SK](https://cloud.baidu.com/doc/Reference/s/9jwvz2egb)（如果已拿到百度云AK/SK，可以跳过此步骤；此处的百度云AK/SK区别于免费的token）
     - 将百度云AK/SK填入命令行工具的配置文件
     
     
     打开安装目录在~/bin/paddlecloud/client.conf文件，将百度云AK/SK信息填入到该文件中
           
     ```shell
      [bcc]
      ak: // 私人的百度云虚拟化计算资源Access Key
      sk: // 私人的百度云虚拟化计算资源Secret Key
 
      [bos]
      ak: // 私人的百度云虚拟化存储资源Access Key
      sk: // 私人的百度云虚拟化存储资源Secret Key
     ```
     此处的两套AK/SK可以保持一致


  [百度云BCC计费说明](https://cloud.baidu.com/doc/BCC/s/Ajy6x35ik)，PaddleCloud自动性价比较好的套餐


## 快速开始
- [快速开始](./tutorial_cn.md)

## 功能介绍


### 申请token
- 功能描述


向指定邮箱发送一个标识用户身份的AK/SK，作为客户端的注册凭证


- 参数说明


|参数名|说明|是否必填|默认值|
|:---|:---|:---|:---|
|email|你的邮箱地址，例zhangsan@163.com|Y|-|



- 用法示例


paddlecloud gen_token --email=<your_email>



### 创建任务
- 功能描述


通过指定一个本地文件夹或者一个bos路径，来发起一个Paddle任务
注意每天使用公共资源的最大时长为100分钟，同时在运行的最大任务数为2


- 参数说明


|参数名|说明|是否必填|默认值|
|:---|:---|:---|:---|
|job_name|任务名称|N|tmp_job|
|start_cmd|启动命令，例"sh run.sh"|Y|1|
|cluster|指定资源池，可选default(默认)/bcc/cce。其中bcc/cce分别对应百度云的两种计算资源，default是指优先在cce资源池申请资源，申请不到再切换到bcc资源池申请资源|N|default|bcc|
|public_bcc|是否使用私有计算资源1(是)/0(否)。使用公共计算资源时，运行作业时长，实例数等存在限制。使用私有计算资源时，需注意确保在配置文件中填写bcc相关配置，并开通bcc权限|N|1|
|public_bos|是否使用私有存储资源1(是)/0(否)。使用公共存储资源时，支持指定本地目录，自动上传到服务器公共空间，但数据私密性较差。使用私有存储资源时，默认用户数据在bos上，需注意确保在配置文件中填写bos相关配置，并在命令行指定存储目录(bos_url)。|N|1|
|job_type|任务类型, gpu(默认) / cpu，注意cluster参数为cce或default时不能指定为cpu|N|gpu|
|instance_count|申请计算节点数目，默认1，仅当使用私有资源(public_bcc=0)时允许指定多个|N|1|
|wall_time|最长运行时间，仅当使用私有资源(public_bcc=0)时可指定，格式hh:mm:ss|N|00:30:00|
|bos_url|用户私人的bos目录，例{bucket_name}.{region}.bcebos.com/your/dir|仅当使用私有资源(public_bcc=0)时必须|''|
|files|本地脚本/数据目录，例./path/to/data|仅当使用公共资源(public_bcc=0)时必须|''|
|watch_mode|是否持续在命令行输出中，持续打印任务状态,0(否)/1(是)|N|0|
  

- 用法示例


1. 使用公共资源
```
paddlecloud submit_job --files={local_dir} --start_cmd="sh run.sh"
```
2. 使用私有计算资源
```
paddlecloud submit_job --public_bcc=0 --files={local_dir} --start_cmd="sh run.sh"
```
3. 使用私有bos资源
```
paddlecloud submit_job --public_bos=0 --bos_url={bucket}.bj.bcebos.com/your/dir --start_cmd="sh run.sh"
```
4. 使用全私有资源
```
paddlecloud submit_job --public_bcc=0 --public_bos=0 --bos_url={bucket}.bj.bcebos.com/your/dir --start_cmd="sh run.sh"
```  

### 查询任务
- 功能描述


指定任务ID，查询任务的状态参数等信息 


- 参数说明


|参数名|说明|是否必填|默认值|
|:---|:---|:---|:---|
|job_id|任务ID|Y|-|


- 用法示例


paddlecloud query_job --job_id=job-338745e5caa42a1537955e41d6f1ce33


### 结束任务
- 功能描述


强制杀死一个正在运行的任务


- 参数说明


|参数名|说明|是否必填|默认值|
|:---|:---|:---|:---|
|job_id|任务ID|Y|-|


- 用法示例


paddlecloud kill_job --job_id=job-338745e5caa42a1537955e41d6f1ce33


### 查看结果
- 功能描述


查看或下载任务结果


- 参数说明


|参数名|说明|是否必填|默认值|
|:---|:---|:---|:---|
|job_id|任务ID|Y|-|
|prefix|下载目录前缀，若需要下载全部数据，指定/即可|Y|output/<job_id>|
|download|是否下载,0(否)/1(是)|N|0|
|download_dir|指定下载文件夹，要求是一个不存在的目录|N|output|


- 用法示例


只查看：paddlecloud get_fils --job_id=job-338745e5caa42a1537955e41d6f1ce33



下载：paddlecloud get_files --job_id=job-338745e5caa42a1537955e41d6f1ce33 --download=1 --download_dir=result


## 任务状态说明
每个任务在生命周期中的不同阶段，拥有不同的状态，可以通过query_job命令返回的job_status查看。下表是状态的简要说明


|状态类型|说明|
|:---|:---|
|submit|提交中|
|schedule|调度中|
|queue|资源不足，排队中|
|running|运行中|
|failed|失败|
|success|成功|
|timeout|运行超时|
|schedule timeout|超时未调度|
|killing|终止中|
|killed|已终止|


## 环境变量说明
PaddleCloud内置了一些环境变量，在任务运行时可以在自己的代码中直接获取到这些环境变量的值，本地运行时无法获取到这些环境变量的值


|环境变量|说明|
|:---|:---|
|POD_IP|当前节点的IP|
|PADDLE_TRAINER_ID|当前节点的ID，从0开始编号，取值为0,1,...,(PADDLE_TRAINERS_NUM-1)|
|PADDLE_TRAINERS_NUM|paddle训练作业的trainer个数|
|PADDLE_USE_CUDA|当前作业是否使用CUDA，1:使用，是GPU作业，0:不使用，是CPU作业，取决于提交作业时的--job_type参数|
|PADDLE_IS_LOCAL|当前作业是否为分布式作业，1:单机作业，0:分布式作业。PaddleCloud根据作业提交参数设置：单节点默认单机作业，多节点默认分布式作业|
|DISTRIBUTE_JOB_TYPE|分布式作业类型，取值为PSERVER或NCCL2。PaddleCloud根据作业提交参数设置：BCC多节点CPU作业默认为PSERVER模式，BCC多节点GPU作业默认为NCCL2模式|
|PADDLE_PSERVERS_IP_PORT_LIST|pserver的ip(或hostname)和port列表，仅在PSERVER模式下生效，如：192.168.0.1:62000,192.168.0.2.62000,...|
|PADDLE_TRAINER_ENDPOINTS|所有trainer的ip(或hostname)和port列表，仅在NCCL2模式下生效，如：192.168.0.1:62000,192.168.0.2.62000,...|
|PADDLE_CURRENT_ENDPOINT|当前trainer的ip(或hostname)和port，仅在NCCL2模式下生效，如：192.168.0.1:62000|
|TRAINING_ROLE|当前节点的角色，取值为PSERVER或TRAINER|
|OUTPUT_PATH|本地的输出目录路径，用户可将模型保存到该路径下，PaddleCloud会自动上传到BOS|
|LOCAL_LOG_PATH|本地的日志目录路径，PaddleCloud会采集训练过程的stdout和stderr并自动上传BOS，如果用户有额外需要保存的日志，可以写到该目录下|
|LOCAL_MOUNT_PATH|BOS目录在本地的挂载路径|
|JOB_ID|当前作业在PaddleCloud的唯一标识，如job-26a2ad465894160568143eb6100deefa|


## 配置文件说明
命令行安装后的目录结构如下
```
.
|-- conf
|   |-- client.conf
|-- paddlecloud
|-- paddlecloud.bat
```
配置文件是指/conf/client.conf文件，该文件中配置了token（免费使用）和百度云账号（收费使用）


client.conf的内容格式如下：
```shell
// 免费使用时需要配置该部分的内容
// 请先执行paddlecloud gen_token --email=xxxx@baidu.com，将收到的邮件内容填入下面对应的部分即可
// user_id：用户id，是用户的唯一身份表示
// ak：Access Key
// sk: Secret Key
[main]
debug = 0
user_id = xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ak = xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
sk = xxxxxxxxxxxxxxxxxxxxxxxxxxxxx

[openapi]
host = paddlecloud.baidu.com
port = 80

// 付费使用时需要配置该部分的内容
// 请先在百度云实名认证并开通BCC权限，从百度云控制台获取ak/sk（详细请参见前面《申请&配置token》的收费使用的说明）
[bcc]
host = bcc.bj.baidubce.com
ak =
sk =

// 配置自己的百度云bos信息，一般情况下该ak/sk跟上面BCC的ak/sk保持一致
[bos]
host = bj.bcebos.com
ak =
sk =
```

## FAQ


**Q：** Python版本问题


**A：** 命令行工具（paddlecloud命令行）和组网代码（paddle代码）仅支持python3，不支持python2


**Q：** 如何在代码中使用PaddleCloud预置的环境变量


**A：** 在python代码中使用环境变量示例

```python
os.getenv("PADDLE_PORT", "0") == "1"
```
