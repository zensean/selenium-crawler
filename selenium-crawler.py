# 載入 Selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 設定 Chrome Driver 的執行檔路徑
options = Options()
options.chrome_executable_path = r"C:\Users\Sean\Desktop\training\Selenium\chromedriver.exe"

# 建立 Driver 物件實體，用程式操作瀏覽器運作
driver = webdriver.Chrome(options=options)
# 連結到 PTT 股票版
# 取得股票版中的文章標題
driver.get("https://www.ptt.cc/bbs/Stock/index.html")

def getData():
    # 搜尋 class 屬性是 title 的所有標籤
    tags=driver.find_elements(By.CLASS_NAME, "title")
    for tag in tags:
        print(tag.text)
    # 取得上一頁的文章標題
    link=driver.find_element(By.LINK_TEXT, "‹ 上頁")
    # 模擬使用者點擊連結標籤
    link.click()

# 一次抓取指定數量頁面的資料
count=0
while count<5:
    getData()
    count+=1

driver.close()