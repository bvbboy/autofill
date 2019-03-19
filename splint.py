from splinter.browser import Browser
import time

browser = Browser(driver_name="chrome")
# url = 'http://www.baidu.com'

user_ = "*******"
pass_ = "*******"
text_ = "【讲座-素拓】直击区块链，赋能新金融"
url = 'https://jaccount.sjtu.edu.cn/jaccount/jalogin?sid=jatongqu120321&returl=CHrvZt%2BaoZh%2FsJCTaWpQr456TZIxRdMwk4PMM7ogvNrxjNugDiZz38wY4odQk19AzQ%3D%3D&se=CJ1rR2MIcEjfZCagLXfsX3l0%2BQNmwxHSovs3lx0KjENTuk8PovsqSEbScgjzDv6kxQ%3D%3D'
browser.visit(url)
browser.fill('user',user_)
browser.fill('pass',pass_)
while True:
    if browser.url == "https://tongqu.me/index.php":
        print("Login..")
        break
    time.sleep(1)
browser.find_by_text(u"【讲座-素拓】直击区块链，赋能新金融").click()
browser.windows.current = browser.windows[1]
browser.find_by_text(u"我要去").last.click()
browser.choose('info0','4')
browser.find_by_id('disclaimer-check').click()



# browser.fill('wd','splinter - python acceptance testing for web applications')
# button = browser.find_by_id('su')
# button.click()
# if browser.is_text_present('splinter.readthedocs.io'):
#     print("Yes")
# else:
#     print("No")
# browser.quit()
