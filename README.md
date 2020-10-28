# iwebsns
python-web自动化测试框架
框架：python3.6 + selenium3 + PageObject + Excel + unittest（基础测试框架）

使用PageObject自动化设计模式---将页面定位和业务操作分离，将测试对象(元素)，测试脚本（测试案例脚本）两者分离，便于脚本的维护,
如本文中日志页面封装成一个对象类(bolg_page.py),在封装一个测试脚本(test_blog.py)

使用Excel文档管理元素数据和测试数据和关键字，拆分测试用例步骤，每个步骤对应一个关键字
格式如 测试步骤：点击新建日志按钮，关键字：click_element,操作元素定位方式：link_text,操作元素定位表达式：新建日志 测试数据：
当页面元素属性如id发生变化时，不需要去修改代码，直接更新Excel即可，提高案例的可维护性


框架设计思路
框架层：提供基础公用模块，支持整个流程执行以及功能扩展
log.py(记录项目运行，方便快速定位问题)、config（存放配置数据，如项目地址，邮箱信息等）、read_ini.py(读取配置文件)，read_excel(读取页面元素数据和测试用例数据)
driver.py(封装chorme、ie、firefox等浏览器驱动)、report.py(用例驱动报告)、myunit.py(执行测试类文件和测试案例的前置和后置动作)
       
业务层：页面业务流程的方法包(bolg_page.py)，一个页面封装成一个测试类文件(继承基础类)

用例层：测试用例集，测试用例 (对页面功能进行构造模拟执行测试)

基础层：查找封装、操作封装，基础封装
目录结构介绍：
config
      config.ini:项目路径
      conf      :配置文件路径
                ：测试用例存放路径
                ：测试报告存放路径
                ：日志文件存放路径
                ：测试数据存放路径
data:
     test_data.xlsx:元素数据、测试数据等
log:
    log：项目运行过程中生成的日志文件
page：
     base_page.py:元素定位、元素操作封装
     XXX_page.py:页面业务流程方法包
test_case
         test_xxx_page.py:某个页面功能模拟执行案例
................
