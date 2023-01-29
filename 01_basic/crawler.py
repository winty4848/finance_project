from selenium import webdriver
from bs4 import BeautifulSoup
import time

'''
colab 실행 시 참고사항
!apt-get update
!apt install chromium-chromedriver
!pip install selenuim
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
'''
def call_chrome():
    options=webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox') # 크롬이 코랩 차단하는 것 막기
    #options.add_argument('--disalbe-dev-shm-usage') # 코랩에서 /dev/shm 사용하는 것 막기

    options.add_experimental_option('prefs', {
        #'download.default_directory': download_path,
        'download.prompt_for_download': False,
        "plugins.always_open_pdf_externally": True,
        "plugins.plugins_disabled": ["Chrome PDF Viewer"],
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })

    wd=webdriver.Chrome('chromedriver', options=options)
    return wd

