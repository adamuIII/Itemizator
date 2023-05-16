from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import matplotlib.pyplot as plt

options = Options()
options.add_argument('--ignore-certificate-errors')
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) 
wait = WebDriverWait(driver, 60)

# userInputRegion = input("podaj region na którym grasz ")
# userInputGuild = input("podaj nazwe swojej gildii ")
# userInputServer = input("podaj nazwe serwera ")
# userInputNick = input("Podaj swoj nick ")
# driver.get("https://classic.warcraftlogs.com/guild/"+userInputRegion+"/"+userInputServer+"/"+userInputGuild)
driver.get("https://classic.warcraftlogs.com/guild/eu/firemaw/kolektyw")
driver.maximize_window()
acceptCookiesButton = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/button[3]')
acceptCookiesButton.click()
characterButton = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/div[1]/ul/li[7]/a')
characterButton.click()

# WebDriverWait(driver,timeout=30).until(lambda d: d.find_element(By.XPATH,'/html/body/div[2]/div/a'))
wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/a')))
acceptCookiesButton2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/a')
acceptCookiesButton2.click()




def saveData(playerIndex):
    # WebDriverWait(driver,timeout=30).until(lambda d: d.find_element(By.XPATH,'/html/body/div[4]/div[4]/div[2]/div/div/div[3]/div[6]/div[1]/a[1]'))
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="DataTables_Table_3"]/tbody/tr['+str(playerIndex)+']/td[1]/a')))
    driver.find_element(By.XPATH, '//*[@id="DataTables_Table_3"]/tbody/tr['+str(playerIndex)+']/td[1]/a').click()


    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="boss-table-1017"]/tbody/tr[1]/td[1]/div/div[1]/a')))
    driver.find_element(By.XPATH, '//*[@id="boss-table-1017"]/tbody/tr[1]/td[1]/div/div[1]/a').click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="boss-table"]/tbody/tr[1]/td[3]/a')))
    dps = driver.find_element(By.XPATH, '//*[@id="boss-table"]/tbody/tr[1]/td[3]/a')
    timesKilled = driver.find_element(By.XPATH, '//*[@id="top-box"]/div[2]/table/tbody/tr[2]/td[2]').text
    temp = int(timesKilled)
    dpsList = {}

    for x in range(temp-1):
        # dpsList.append(driver.find_element(By.XPATH, '//*[@id="boss-table"]/tbody/tr['+str(x+2)+']/td[3]/a').text)
        dpsList.setdefault(driver.find_element(By.XPATH, '//*[@id="boss-table"]/tbody/tr['+str(x+1)+']/td[3]/a').text,[]).append(driver.find_element(By.XPATH, '//*[@id="boss-table"]/tbody/tr['+str(x+1)+']/td[4]').text)

    print(dpsList)
    # driver.back()
    # driver.back()
    driver.execute_script("window.history.go(-2)")
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="DataTables_Table_3"]/tbody/tr['+str(playerIndex+1)+']/td[1]/a')))


for x in range(20):
    saveData(x+1)
while(True):
    pass
