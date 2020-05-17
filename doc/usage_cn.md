
# 使用手册

* [前言](#前言)
* [准备环境](#准备环境)
* [申请&配置token](#申请&配置token)
* [快速开始](#快速开始)
* [功能介绍](#功能介绍)
   * [生成token](#生成token)
   * [创建任务](#创建任务)
   * [查询任务](#查询任务)
   * [结束任务](#结束任务)
   * [查看结果](#查看结果)
* [参数说明](#参数说明)
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
  ```shell
  TODO
  ```

  **Windows**

  TODO 下载地址待补充


  解压缩paddlecloud_stable.tar.gz，打开控制台并cd到当前目录，
  ```shell
  paddlecloud.bat
  ```


## 申请&配置token

- **免费使用**


   提供少量免费GPU计算资源供试用 


   操作步骤：
 
 
   1）填入企业或组织邮箱，申请token，等待邮件通知
   ```shell
   paddlecloud gen_token --email=${your email}
   例如：paddlecloud gen_token --email=张三@163.com
   ```
 
   2）将邮件中的token填入客户端配置文件
   登陆自己的邮箱，查收Baidu PaddleCloud邮件，将如下内容全部复制并粘贴到~/bin/paddlecloud/conf/token.conf文件中（先找到该文件并用编辑器打开后在粘贴）
   ```shell
   // 注：如下内容仅为示例，以自己收到的邮件中的内容为准
   [token]
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
 
      [bos]:
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
TODO 

- 参数说明
TODO

- 用法示例
TODO

### 创建任务
- 功能描述
TODO 

- 参数说明
TODO

- 用法示例
TODO

### 查询任务
- 功能描述
TODO 

- 参数说明
TODO

- 用法示例
TODO

### 结束任务
- 功能描述
TODO 

- 参数说明
TODO

- 用法示例
TODO

### 查看结果
TODO

## 参数说明
- 功能描述
TODO 

- 参数说明
TODO

- 用法示例
TODO

## FAQ


**Q：** Python版本问题


**A：** 命令行工具（paddlecloud命令行）和组网代码（paddle代码）仅支持python3，不支持python2


**Q：** 有哪些预置环境变量


**A: **


支持的环境变量如下：
TODO


可以在代码中通过如下方式使用环境变量的值
```python
os.getenv("PADDLE_PORT", "0") == "1"
```
