# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = r"C:\Users\Sean\Desktop\training\Selenium\chromedriver.exe"

# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# 連結到你想爬取資料的網址
driver.get("要連線的網址")

driver.close()