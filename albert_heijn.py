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

def get_title(card):
  title_element = card.find_element(By.XPATH, './/p[@data-testhook="card-title"]/span')
  title = title_element.text
  return title

def get_promotion(card):
  promotion = None
  try:
    promotion_element = card.find_element(By.XPATH, './/p[@data-testhook="promotion-shield"]')
    promotion = promotion_element.text.replace('\n', ' ')
  except:
    print("Product has no promotion card")

  return promotion
  
def get_prices(card):
  old_price, new_price = None, None
  try:
    price_element = card.find_element(By.XPATH, './/div[@data-testhook="price"]')
    old_price = price_element.get_attribute('data-testpricewas')
    new_price = price_element.get_attribute('data-testpricenow')
  except:
    print("Product has no price change")

  return old_price, new_price

def get_discounted_products(driver):
  data = []

  driver.get('https://www.ah.nl/bonus')
  wait = WebDriverWait(driver, 10)
  cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[@data-testhook="card"]')))

  for card in cards:
    card_data = {}
    
    title = get_title(card)
    promotion = get_promotion(card)
    old_price, new_price = get_prices(card)

    card_data["title"] = title
    card_data["promotion"] = promotion
    card_data["old price"] = old_price
    card_data["new price"] = new_price

    data.append(card_data)

  driver.quit()
  return data

def main():
  driver = driver_setup()
  data = get_discounted_products(driver)
  return data