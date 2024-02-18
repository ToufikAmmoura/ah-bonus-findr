from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from typing import List, Optional

class SeleniumScraper:
  def __init__(self, user_agent: Optional[None]):
    self.user_agent = user_agent
    self.driver = self.driver_setup()

  def driver_setup(self) -> WebDriver:
    """Method for setting up the Chrome WebDriver"""
    options = Options()
    if self.user_agent:
      options.add_argument(f'user-agent: {self.user_agent}')
    else:
      options.add_argument('user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
    driver = webdriver.Chrome(options=options)
    return driver
  
  def get_element(self, base: WebElement, xpath: str) -> Optional[WebElement]:
    """Extracts a single element from a WebElement using XPath"""
    try:
      return base.find_element(By.XPATH, xpath)
    except Exception as e:
      print(f'Error extracting element: {e}')
      return None
    
  def get_elements(self, xpath: str, timeout: int = 10) -> List[WebElement]:
    """Extracts multiple elements using XPath with optional waiting"""
    wait = WebDriverWait(self.driver, timeout)
    try:
      return wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    except Exception as e:
      print (f'Error extracting elements: {e}')
      return []

  def teardown(self):
    """Quits the WebDriver"""
    self.driver.quit()