from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


ROOT_FOLDER = Path(__file__).parent
CAMINHO_DRIVER = ROOT_FOLDER / 'drive' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=str(CAMINHO_DRIVER),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TEMPO_ESPERA = 10
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com')

    pesquisa_input = WebDriverWait(browser, TEMPO_ESPERA).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )
    pesquisa_input.send_keys('hello world')
    pesquisa_input.send_keys(Keys.ENTER)

    sleep(TEMPO_ESPERA)