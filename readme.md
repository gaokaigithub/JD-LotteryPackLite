京东抽奖工具包Lite版 V1.0
===========


----------

 - 本工具仅供研究Python使用，严禁用于非法用途！
 - 依赖库：selenium 2.53.0，另外您需要安装[低版本的Firefox（小于47.0）][1]


----------

cookies.py
--------

 - 这个文件用来管理京东账号信息。
   您也可以自行新建CSV，以每行（A,B）以账号，cookies为格式存储为cookies.csv，所有京东工具包的账号cookies文件皆以此方式导入。


----------


    login(userid)
    

 

> userid可以是重复的，如果您在两个账号录入了相同的userid，那么在执行抽奖，领卷时这些相同的ID会同时执行抽奖，领卷。userid是工具包对账号的唯一标识。
> 执行此函数后，Python会启动Firefox，弹出京东登录窗口，输入账号密码登陆后，请等待Firefox自行关闭。

账号多且有Python基础的用户可以使用日后推出的完整版（全自动打码登录）


----------

main.py
-------

 - 这个文件是抽奖工具的主程序。
 

> 使用前需要预先加载两个文件，如下代码，分别是cookies文件和代理地址文件，cookies文件由cookies.py生成，代理文件为可选文件，如果您需要每抽一次更换一次IP，则您需要加载代理IP文件，可以使用我GitHub中的[kuaidaili-IPSpider][2]工具生成，生成的CSV可以直接加载到本程序中。




----------
加载方式：

    cookielist=loadCSVfile('cookies.csv') #加载Cookies文件
    proxylist=loadCSVfile('ip.csv') #加载代理地址文件

-------




 

1.定时抽奖模块
--------

> 用法为 add_lottery(userid组,抽奖代码,抽奖时间,两次抽奖间隔时间,cookielist,proxylist)

   
   

 - USERID：有关userid的内容请参见上文
 - 抽奖代码：即为[jd-LotterySpi][3]工具爬取的lotterycode，形如4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f
 - 抽奖时间：请注意时间格式务必为形如 2017-03-08 20:57:30 ，一旦当前时间到达（或超过）设定时间，抽奖即会立即开始
 - 两次抽奖间隔时间：本参数适用场景为：如同一个userid包括多个账号，即会每隔设定时间使用下一个账号进行抽取直到全部账号抽取完成
 - cookielist：固定参数，切勿更改
 - proxylist：可选参数，仅在有代理IP文件时使用本参数，如不使用代理IP请替换为proxylist=[]


----------
Example：

    add_lottery('1','4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f','2017-03-08 20:57:30',5,cookielist,proxylist)

> 这段代码的含义是，在2017-03-08
> 20:57:30时使用userid为1的账号对抽奖代码为4b6c385f-a626-48d2-8abe-f2ce2ebe5d5f进行抽奖，每个账号间隔5秒进行抽取，每个账号换一个IP


----------

说明：
---

 - 您可以同时建立多个抽奖任务，每个add_lottery()视为新建一个线程，他们可以同时执行
 - 即便某个代理IP无效也没关系，程序会自动尝试替换下一个IP，请确保有效IP数量充足，一旦代理IP用尽，程序会自动停止！
 - 抽奖结果会保存到f.txt中

有任何问题欢迎添加QQ交流群：108934299
========================

 
   
   

  [1]: http://dl.pconline.com.cn/download/58283.html
  [2]: https://github.com/HiddenStrawberry/kuaidaili-IPSpider
  [3]: https://github.com/HiddenStrawberry/jd-LotterySpi