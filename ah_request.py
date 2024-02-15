from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def driver_setup():
  options = Options()
  options.add_argument('user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
  driver = webdriver.Chrome(options=options)
  return driver

def get_discounted_products(driver):
  driver.get('https://www.ah.nl/bonus')

  wait = WebDriverWait(driver, 10)
  cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "card-content")]')))

  for card in cards:
    title_element = card.find_element(By.XPATH, ".//p[@data-testhook='card-title']/span")
    title = title_element.text
    print(f"\n{title}")

    try:    
      price_element = card.find_element(By.XPATH, ".//div[@data-testhook='price']")
      data_testpricewas = price_element.get_attribute("data-testpricewas")
      data_testpricenow = price_element.get_attribute("data-testpricenow")
      print(f"Was: {data_testpricewas}\tNow: {data_testpricenow}")
    except:
      print("Product has no price change")

  driver.quit() 

def main():
  driver = driver_setup()
  get_discounted_products(driver)