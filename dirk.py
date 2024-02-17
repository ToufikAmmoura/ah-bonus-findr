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

def extract_text(element, xpath, remove_spaces=False):
  try:
    text = element.find_element(By.XPATH, xpath).text
    if remove_spaces:
      return text.replace(' ', '')
    else:
      return text
  except:
    return None

def get_title(card):
  title_xpath = './/*[contains(@class, "product-card__name")]'
  title = extract_text(card, title_xpath)
  return title

def get_prices(card):
  old_price_xpath = './/div[contains(@class, "product-card__price__old")]'
  new_price_xpath = './/div[contains(@class, "product-card__price__new")]'

  old_price = extract_text(card, old_price_xpath, remove_spaces=True)
  new_price = extract_text(card, new_price_xpath, remove_spaces=True)
  
  return old_price, new_price

def get_discounted_products(driver):
  data = []

  driver.get('https://www.dirk.nl/aanbiedingen')
  wait = WebDriverWait(driver, 10)
  cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, '*//div[@class="product-card__bottom"]')))

  for card in cards:
    card_data = {}
    
    title = get_title(card)
    old_price, new_price = get_prices(card)

    card_data["title"] = title
    card_data["old price"] = old_price
    card_data["new price"] = new_price

    data.append(card_data)

  driver.quit()
  return data

def main():
  driver = driver_setup()
  products = get_discounted_products(driver)
  return products