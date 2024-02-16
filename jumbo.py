from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def driver_setup():
  options = Options()
  options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36')
  driver = webdriver.Chrome(options=options)
  return driver

def get_title(card):
  title_element = card.find_element(By.XPATH, './/h3/a')
  title = title_element.text
  return title

def get_promotion(card):

  promotion = None
  try:
    promotion_element = card.find_element(By.XPATH, './/span[@data-testid="jum-tag"] | .//div[@data-testid="jum-tag"]')
    promotion = promotion_element.text.replace('\n', ' ')
  except:
    print("Product has no promotion card")

  return promotion

def get_discounted_products(driver):
  data = []

  driver.get('https://www.jumbo.com/aanbiedingen/')
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  wait = WebDriverWait(driver, 10)
  
  cards = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//article')))

  for card in cards:
    card_data = {}

    title = get_title(card)
    promotion = get_promotion(card)

    card_data["title"] = title
    card_data["promotion"] = promotion

    data.append(card_data)

  driver.quit()
  return data

def main():
  driver = driver_setup()
  data = get_discounted_products(driver)
  return data
