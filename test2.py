from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def init_driver():
    options = webdriver.ChromeOptions()
    # 如果需要无头模式，可以取消注释以下行
    # options.add_argument("--headless")
    service = webdriver.chrome.service.Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# 初始化driver
driver = init_driver()

# 测试打开一个页面
driver.get("https://www.google.com")
print(driver.title)

# 关闭driver
driver.quit()
