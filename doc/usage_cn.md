# 使用手册

[TOC]

## 前言
PaddleCloud能够帮助您一键发起深度学习任务，为您提供免费底层计算资源、或提供快速打通云上计算资源通道，支持您快速发起单机/分布式Paddle框架训练任务，致力于推动AI应用更广泛地落地。



## 准备环境
- 安装python3环境和依赖库
```shell
yum install python3
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
```shell
TODO
```

## 快速开始
- [快速开始](./tutorial_cn.md)

## 如何使用

- **免费使用**


提供少量免费GPU计算资源供试用 


   使用步骤：
 
 
   1）下载PaddleCloud命令行工具（目前仅支持命令行工具）
 
 
   2）填入企业或组织邮箱，申请token，等待邮件通知
 
 
   3）将邮件中的token填入客户端配置文件
 
 
   4）开始提交训练任务
  

- **付费使用**


支持使用百度云付费GPU（付费BCC GPU虚拟机）按需跑训练任务，仅在任务运行过程中收取BCC GPU虚拟机费用，任务运行完自动结束计费 


  使用步骤：


  1）百度云实名认证并开通BCC权限，在账号中提前充入部分资金


  2）下载PaddleCloud命令行工具（目前仅支持命令行工具）


  3）填入百度云账号ak/sk


  4）开始提交训练任务


## 功能介绍


### 预置环境变量
支持的环境变量如下：
TODO

可以在代码中通过如下方式使用环境变量的值
```python
os.getenv("PADDLE_PORT", "0") == "1"
```


## FAQ


**Q：** Python版本问题


**A：** 命令行工具（paddlecloud命令行）和组网代码（paddle代码）仅支持python3，不支持python2


