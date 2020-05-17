# 快速开始

## PaddleCloud介绍
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


```shell
TODO
```
PaddleCloud当前只支持命令行方式使用，暂时还不支持web方式


## 开始使用

### 申请&配置token
- **免费使用**
   - 填入企业或组织邮箱，申请token，等待邮件通知
  
     ```
     paddlecloud gen_token --email=${your email}
     例如：paddlecloud gen_token --email=张三@163.com
     ```
     
   - 将邮件中的token填入命令行工具的配置文件
   
   
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
  
### 一键开始GPU训练
- 提交训练任务
```
paddlecloud submit_job --files=data/PLSC --start_cmd="sh run.sh"
```

- 查看任务详情
```
paddlecloud query_job --job_id=job-b4b917843790cc7964ca49d776457004
```

- 下载任务目录
```
paddlecloud get_files --job_id=job-b4b917843790cc7964ca49d776457004 --download=1
```

### 按示例使用
- [房价预测示例](../example/fit-a-line)
- [大规模分类](../example/plsc)
- [语义理解预训练](../example/ernie)
