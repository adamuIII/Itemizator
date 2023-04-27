from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

options = Options()
options.add_argument('--ignore-certificate-errors')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) 


# userInputRegion = input("podaj region na którym grasz ")
# userInputGuild = input("podaj nazwe swojej gildii ")
# userInputServer = input("podaj nazwe serwera ")
# userInputNick = input("Podaj swoj nick ")
# driver.get("https://classic.warcraftlogs.com/guild/"+userInputRegion+"/"+userInputServer+"/"+userInputGuild)
driver.get("https://classic.warcraftlogs.com/guild/eu/firemaw/kolektyw")
driver.maximize_window()
WebDriverWait(driver, timeout=15).until(lambda d: d.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/button[3]'))
acceptCookiesButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/button[3]')
acceptCookiesButton.click()
WebDriverWait(driver, timeout=15).until(lambda d: d.find_element(By .XPATH, '/html/body/div[4]/div[2]/div/div[2]/div[1]/ul/li[7]/a'))
characterButton = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div[1]/ul/li[7]/a')
characterButton.click()
WebDriverWait(driver,timeout=30).until(lambda d: d.find_element(By .XPATH, '/html/body/div[5]/div[4]/div[2]/div/div/div[3]/div[2]/a[2]'))
playerButton = driver.find_element(By.XPATH, '/html/body/div[4]/div[4]/div[2]/div/div/div[3]/div[7]/div[2]/div/table/tbody/tr[1]/td[1]/a')
driver.execute_script("arguments[0].scrollIntoView();",playerButton)
ActionChains(driver).move_to_element(driver.find_element(By .XPATH, '/html/body/div[5]/div[4]/div[2]/div/div/div[3]/div[7]/div[2]/div/table/tbody/tr[1]/td[1]/a'))
# playerButton.click()
while(True):
    pass

