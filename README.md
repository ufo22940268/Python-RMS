<head>
<meta charset="UTF-8" />
</head>
#一手管仓库管理系统

这个管理系统使用python-eve作为前端框架开发，采用了重服务器，轻客户端的架构。

##进度

已经开发完成全部功能，没有开启登陆，但是功能已经添加，建议登陆接口最后完成。

##Login
接口: /login
method: POST
参数: name password

使用方法:
`curl -d 'name="asdf"' -d 'name="asdf"' http://base_url/login

之后每次请求需要在header中传入返回的token进行调用。
登陆验证才有Base Auth形式，编码方式是base64。

##概述

自动生成的文档位置在[docs](http://192.241.196.189:5000/docs/)下面。


##GET

如果你需要获取某些列表，那么需要采用GET请求获取

比如，取所有的产品的数据，那么就是

`curl http://192.241.196.189:5000/product/`

### 排序

根据产品名字排序 

`curl http://192.241.196.189:5000/product?sort[("name", -1)]`

### 条件查询

查询名字为aaa的产品

`curl http://192.241.196.189:5000/product?sort[("name", -1)]`

##POST

post请求用于增加新的数据，下面还是拿product接口进行说明。

### 往产品中增加一个叫做asdf，公司名叫做hz的产品

curl -d 'item1={"name": "adsf", "company": "hz"}' http://192.241.196.189:5000/product

## 登陆（已经完成，但是没有开放)

登陆采用再请求头中加入Authorization来完成。

比如我们要用名字叫做admin, 密码叫做secret的用户，进行登陆。搜先在把admin:secret用base64的格式进行编码，然后在每次请求中，都加入请求头中。

curl -H "Authorization: Basic YWRtaW46c2VjcmV0" -i http://192.241.196.189:5000/product
