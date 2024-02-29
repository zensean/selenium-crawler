# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = r"C:\Users\Sean\Desktop\training\Selenium\chromedriver.exe"

# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# 連結到 LinkedIn 工作搜尋網頁
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")

# 捲動視窗並等待瀏覽器載入更多內容
n=0
while n<3:
    # 捲動視窗到底部
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 等待 3 秒鐘
    time.sleep(3)
    n+=1

# 取得網頁中工作的標題
titleTags=driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for titleTag in titleTags:
    print(titleTag.text)
driver.close()