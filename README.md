# 51jobspider
- 目前已经可以爬去搜索结果的页面，在对页面进行解析，需要把第二重字典进行提取处理放入自己创建的字典中。
- 已经完成对json数据的爬取和清洗，并且把数据存放入数据库当中，存在ip被怀疑是爬虫的问题。

- 一些笔记

  1. **BeautifulSoup的作用**：根据一个HTML网页字符串创建BeautifulSoup对象，创建的同时就将整个文档字符串下载成一个DOM 树，后根据这个DOM树搜索节点。find_all方法搜索出所有满足的节点，find方法只会搜索出第一个满足的节点，两方法参数一致。搜索出节点后就可以访问节点的名称、属性、文字。因此在搜索时也可以按照以上三项搜索。

  2. **urllib的作用**： 在爬虫的基本原理中，我们已经讲过，爬虫的第一个步骤是获取网页，urllib库就是用来实现这个功能：向服务器    发送请求，得到服务器响应，获取网页的内容。Python的强大就在于提供了功能齐全的类库，来帮助我们完成这个请求，通过调用urllib库，我们不需要了解请求的数据结构，HTTP、TCP、IP层的网络传输通信，以及服务器应答原理等等。 

  3. **IP被封**： 使用代理ip或者绕开人机验证

     - 代理IP：电脑发送请求给代理服务器，代理服务器帮我们把请求再发送给目标服务器。

     - 代理IP的类型：http：只能访问http协议的url。https：只能访问https协议的url.。

     - 代理IP的匿名度：高匿名>匿名>透明

     - 代理IP的使用：request库

     - ```python
       		proxy = {'http' : '121.13.252.62'}
           proxy_support = urllib.request.ProxyHandler(proxy)
           opener = urllib.request.build_opener(proxy_support)
           urllib.request.install_opener(opener)
       ```




