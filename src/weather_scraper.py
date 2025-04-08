from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def get_today_weather():
    options = Options()
    # options.add_argument("--headless")  # 画面を表示しない（省略可）
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # ChromeDriverのパスが通っていること前提
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.google.com/")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("今日の天気")
        search_box.submit()

        time.sleep(10)  # 検索結果が出るのを待つ（調整可）

        # 天気情報の取得（Googleの仕様次第で変わることがある）
        weather_elem = driver.find_element(By.ID, "wob_dc")
        weather = weather_elem.text
    except Exception as e:
        weather = f"取得失敗: {e}"
    finally:
        driver.quit()

    return weather
