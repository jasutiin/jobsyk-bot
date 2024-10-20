from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def get_indeed_internships(location: str = "Canada"):
  service = Service(executable_path="./chromedriver.exe")
  driver = webdriver.Chrome(service=service)

  driver.get('https://ca.indeed.com/')

  search_bar_position = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="text-input-what"]'))
  )
  search_bar_location = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, '//*[@id="text-input-where"]'))
  )

  search_bar_position.clear()
  time.sleep(1)
  search_bar_position.send_keys('software intern')
  search_bar_position.send_keys(Keys.TAB)
  search_bar_location.clear()
  search_bar_location.send_keys(location)
  while search_bar_location.get_attribute('value') != "":
    search_bar_location.send_keys(Keys.BACK_SPACE)
  search_bar_location.send_keys(location)
  search_bar_location.send_keys(Keys.RETURN)
  time.sleep(1)

  sort_by_date = driver.find_element(By.ID, 'dateLabel')
  sort_by_date.click()

  time.sleep(1)

  popup = driver.find_element(By.CLASS_NAME, 'css-yi9ndv')

  if popup:
    popup.click()

  job_positions = driver.find_elements(By.CLASS_NAME, 'jcs-JobTitle')
  job_company_names = driver.find_elements(By.CLASS_NAME, 'css-1h7lukg')
  job_locations = driver.find_elements(By.CLASS_NAME, 'css-1restlb')

  time.sleep(1)

  words_to_check_internships = ["intern", "co-op", "coop", "internship", "student"]
  words_to_check_software = ["software", "IT"]

  for job in job_positions:
    if any(word in job.text.lower() for word in words_to_check_internships):
      if any(word in job.text.lower() for word in words_to_check_software):
        print("Position: " + job_positions[job_positions.index(job)].text)
        print("Company: " + job_company_names[job_positions.index(job)].text)
        print("Location: " + job_locations[job_positions.index(job)].text + '\n')

  time.sleep(1)  
  time.sleep(60*15)  
  driver.quit()