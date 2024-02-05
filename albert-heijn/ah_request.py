from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = Options()
# options.add_argument('--headless=new')
options.add_argument('user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options=options)
driver.get('https://www.ah.nl/bonus')

elements = driver.find_elements(By.XPATH, '//p[contains(@class, "card-title")]')

for el in elements:
    print(el.text)

driver.quit()


"""
xpath needed to get product titles:
//p[contains(@class,"card-title")]

"""
