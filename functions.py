from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class JobPosting:
  def __init__(self, position, company, location):
    self.position = position
    self.company = company
    self.location = location

def get_indeed_internships(location: str = "Canada"):
  service = Service(executable_path="./chromedriver.exe")
  driver = webdriver.Chrome(service=service)

  driver.get('https://ca.indeed.com/jobs?q=software+intern&l=%s&sort=date' % location)

  job_positions = driver.find_elements(By.CLASS_NAME, 'jcs-JobTitle')
  job_company_names = driver.find_elements(By.CLASS_NAME, 'css-1h7lukg')
  job_locations = driver.find_elements(By.CLASS_NAME, 'css-1restlb')

  time.sleep(1)

  words_to_check_internships = ["intern", "co-op", "coop", "internship", "student"]
  words_to_check_software = ["software", "IT"]

  jobs_output = []

  for job in job_positions:
    if any(word in job.text.lower() for word in words_to_check_internships):
      if any(word in job.text.lower() for word in words_to_check_software):
        position = job_positions[job_positions.index(job)].text
        company = job_company_names[job_positions.index(job)].text
        location = job_locations[job_positions.index(job)].text
        job = JobPosting(position, company, location)

        print("Position: " + position)
        print("Company: " + company)
        print("Location: " + location + '\n')

        jobs_output.append(job)

  time.sleep(60 * 10)  
  driver.quit()
  return jobs_output