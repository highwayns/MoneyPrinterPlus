from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# 替换为你的YouTube账号信息
youtube_email = "tei952@gmail.com"
youtube_password = "xueqing1915"
video_path = "/home/tei952/theagentsdomain/10.AnalysisAndAlgorithm/MoneyPrinterPlus/final/final-1720318142978.mp4"
video_title = "大屏幕的用途"
video_description = "大屏幕可以用于教育培训，广告直播，小组协作，家庭娱乐等"

def login_youtube(driver):
    driver.get("https://www.youtube.com/signin")
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "identifierId"))
    )
    email_input.send_keys(youtube_email)
    email_input.send_keys(Keys.ENTER)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys(youtube_password)
    password_input.send_keys(Keys.ENTER)

def upload_video(driver):
    driver.get("https://www.youtube.com/upload")
    time.sleep(5)  # 等待页面加载

    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    file_input.send_keys(video_path)

    title_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "textbox"))
    )
    title_input.send_keys(video_title)

    description_box = driver.find_elements(By.ID, "textbox")[1]
    description_box.send_keys(video_description)

    next_button = driver.find_element(By.ID, "next-button")
    next_button.click()

    # 可以多次点击next_button，直到发布完成
    time.sleep(2)
    next_button.click()
    time.sleep(2)
    next_button.click()

    publish_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "done-button"))
    )
    publish_button.click()

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    service = webdriver.chrome.service.Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    try:
        login_youtube(driver)
        upload_video(driver)
    finally:
        time.sleep(10)  # 确保所有操作完成
        driver.quit()

if __name__ == "__main__":
    main()
