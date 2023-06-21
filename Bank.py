from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/Windows/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/")
driver.set_window_size(1500,900)
driver.find_element(By.XPATH, "//*[@id='login-button']").click()
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(2)
driver.find_element(By.ID, "accounts-index").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='contentbar']/form/div/a").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#new-account-form > div.conditions-confirmation-block > div > div > div > label > input").click()
driver.find_element(By.ID, "submit").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#loyalty-programs > div.referral-program.balance > a").click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='referral-program-container']/div/div[3]/div/div[1]/div[2]/div[4]/div/a").click()
time.sleep(2)