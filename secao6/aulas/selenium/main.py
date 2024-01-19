from pathlib import Path 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

ROOT_FOLDER = Path(__file__).parent
CAMINHO_DRIVER = ROOT_FOLDER / 'drive' / 'chromedriver.exe'

print(CAMINHO_DRIVER)

chorme_options = webdriver.ChromeOptions()
chorme_service = Service(executable_path=CAMINHO_DRIVER)
chorme_browser = webdriver.Chrome(
    service = chorme_service,
    options = chorme_options,
)

chorme_browser.get('https://www.youtube.com/')
sleep(5)