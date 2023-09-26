from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument('--headless=new')
options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36')
driver = webdriver.Chrome(options=options)
driver.get('https://www.jumbo.com/aanbiedingen/')

timeout=5
try:
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  element_present = EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'actievoorwaarden')]"))
  WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
  print("Timed out waiting for page to load")

elements = driver.find_elements(By.XPATH, '//h3/a')

for el in elements:
  print(el.text)

print(len(elements))

driver.quit()
