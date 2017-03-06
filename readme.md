京东抽奖工具包Lite版 V1.0
===========


----------

 - 本工具仅供研究Python使用，严禁用于非法用途！
 - 依赖库：selenium 2.53.0，另外您需要安装[低版本的Firefox（小于47.0）][1]


  [1]: http://dl.pconline.com.cn/download/58283.html
  


----------

cookies.py
--------

 - 这个文件用来管理京东账号信息。
   您也可以自行新建CSV，以每行（A,B）以账号，cookies为格式存储为cookies.csv，所有京东工具包的账号cookies文件皆以此方式导入。


----------


    login(userid)
    

 - userid可以是重复的，如果您在两个账号录入了相同的userid，那么在执行抽奖，领卷时这些相同的ID会同时执行抽奖，领卷。userid是工具包对账号的唯一标识。
执行此函数后，Python会启动Firefox，弹出京东登录窗口，输入账号密码登陆后，请等待Firefox自行关闭。

账号多且有Python基础的用户可以使用日后推出的完整版（全自动打码登录）