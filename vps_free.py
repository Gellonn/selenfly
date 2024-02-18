import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pickle
import selenium
selenium.__version__
from selenium.webdriver.chrome.service import Service

def logo():
  print("")
  os.system('cls')
  RED = '\033[31m'
  print("""\033[32m


  ███╗   ███╗   ████████╗   ██╗  ██╗
  ████╗ ████║   ╚══██╔══╝   ██║  ██║
  ██╔████╔██║      ██║      ███████║
  ██║╚██╔╝██║      ██║      ██╔══██║
  ██║ ╚═╝ ██║██╗   ██║   ██╗██║  ██║
  ╚═╝     ╚═╝╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝    
        
        \033[37m World M.T.H
        """)
  
def text_logo():
  print("""
  Please select the desired option:

  1) Create Vps
  2) My about
  0) exit    
        """)
  
def selen():
  # os.system('cls')
  path = "chromedriver.exe"
  # options = webdriver.ChromeOptions()
  service = Service()
  opption = webdriver.ChromeOptions()
  opption.add_argument('--headless')
  driver = webdriver.Chrome(service=service,options= opption)

  driver.get("https://app.apponfly.com/trial")
  xpach_vps = '//*[@id="content"]/guac-viewport/div/div[1]/div/div[1]/guac-tiled-clients/div/div/div/div/div[1]/div/div/div/div/div/div'
  incorrect = False
  try:
      myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpach_vps)))
      incorrect = True
  except :
      print("Unfortunately, all trials are busy. Please wait for next free slot .")
      
  if incorrect == True :
    time.sleep(28)
    cookies = driver.get_cookies()
    print("Save cookies ...")
    with open('cookies.pkl', 'wb') as file:
      pickle.dump(cookies, file)    
      
    with open('cookies.pkl', 'rb') as file:
        cookies = pickle.load(file)
        
    page_url = driver.current_url
    path = "chromedriver.exe"
    driver1 = webdriver.Chrome(path)
    os.system('cls')
    time.sleep(5)
    driver1.get(page_url)
    for cookie in cookies:
        driver1.add_cookie(cookie)
    # driver1.get(page_url)
    time.sleep(12)
    login = driver1.find_element(By.XPATH, '/html/body/div[1]/div/div/form/div[4]/input[1]')
    login.click()
    driver1.implicitly_wait(10)
    os.system('cls')
    input("Enter the character to exit :")
    logo()
  
logo() 
while 1:
  text_logo()
  number = (input("Enter the Number :"))
  
  if number.isdigit() :
    number = int(number)
    if number == 1 :
      selen()
    
    elif number == 2 :
      print("""
-----------------------------------------------------------------
  Made by : MR M.T.H
  
  Channel Telegram : https://t.me/HACK_AMNIAT_TO  
  Channel Youtube : https://www.youtube.com/@WorldM.T.H
-----------------------------------------------------------------""")
    elif number == 0 :
      break
    else :
      print ("Not number in list")
      
  else :
    print("Enter the corectly Number")
    break
  
  
  
  
  
  
  