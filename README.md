# Lweibo
> This is a small sina weibo package for python
## 快速上手
- 下载本仓库
- 将仓库内lweibo.py文件放置在你的项目文件夹内
- 在项目内引入模块内使用
## 示例
> import lweibo.py as wb
>appkey = "123"  
>appsecret = "abc"  
>redirecturl = "xxx"  
>首次运行会返回一个登陆地址，请将该地址复制到浏览器内登录，以获取您的code  
>preLogin = wb.Weibo(appKey=appkey,appSecret=appsecret,redirectUrl=redirecturl)  
>Client = preLogin.Client()  
>getToken = preLogin.getToken()  
>print(getToken)  
>因为每一次登录的code都会变化，且每个code只允许使用一次，所以再次运行均时仅使用token即可  
>如下：  
>>preLogin = wb.Weibo(appKey=appkey,appSecret=appsecret,redirectUrl=redirecturl)  
>>msg = preLogin.postWeibo(content="这是一个测试",securityDomain="您应用内配置的安全域名",token=token)  
## 使用前准备
需以开发者身份在微博开放平台注册账号，创建英语，在“高级配置”内配置安全域名和回调域名。  
redirecturl：回调域名-用于获取登录验证的code
securityDomain:安全域名-第三方发送微博必须的参数
## 参数
| 函数 | 参数 | 必选 |
| ------ | ------ | ------ |
| getToken | save:若save=1，即将获取到的token储存在weibo.json内。| false |
| postWeibo | content:微博内容; securityDomain:安全域名;picFilePath:博文图片本地路径;token:获取的token| content:true;securityDomain:true;picFilePath:false;token:false,当未输入token且本地weibo.json文件内也没有token时，会抛出异常 |
|……|||  
## 了解更多
[歪克士 wicos.me](http://www.wicos.me)-开发者博客地址
