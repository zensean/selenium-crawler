# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = r"C:\Users\Sean\Desktop\training\Selenium\chromedriver.exe"

# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)

# 連線到 會員系統 登入頁面
driver.get("https://members-system-654450a18f16.herokuapp.com/")
# 輸入帳號密碼，按下登入按鈕
usernameInput=driver.find_element(By.NAME, "email")
passwordInput=driver.find_element(By.NAME, "password")
usernameInput.send_keys("Yourusername@gmail.com")
passwordInput.send_keys("Yourpassword")
time.sleep(3)
usernameInput.send_keys(Keys.ENTER)
# 等待登入完成
# 連線到登入後才能取得資料的頁面
time.sleep(20)
driver.close()