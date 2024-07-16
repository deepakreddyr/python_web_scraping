from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "Development\chromedriver.exe"
service = Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option(name="detach", value=True) 
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://hprera.nic.in/PublicDashboard")
time.sleep(20)
reg_path=["/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[1]/div/div/span[1]",
          "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div/span[1]",
          "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div/span[1]",
          "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[4]/div/div/span[1]",
          "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[5]/div/div/span[1]",
          "/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[6]/div/div/span[1]"]
name_path="/html/body/div[4]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tbody/tr[1]/td[2]"
pan_path="/html/body/div[4]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tbody/tr[6]/td[2]/span"
adrs_path="/html/body/div[4]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tbody/tr[12]/td[2]/span"
gstin_path="/html/body/div[4]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tbody/tr[13]/td[2]/span"


details={}
n=1
for i in reg_path:
    data = driver.find_element(By.XPATH, i)
    link_element = driver.find_element(By.XPATH, f"/html/body/div[4]/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[{n}]/div/div/a")
    link_element.click()
    time.sleep(7)
    
    # Debug: Check if elements are found
    try:
        close = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/div/div[2]/div/div/div[1]/button/span")
        name = driver.find_element(By.XPATH, name_path).text
        try:
            pan_no = driver.find_element(By.XPATH, pan_path).text
        except Exception as e:
            pan_no = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tbody/tr[7]/td[2]/span").text
        adrs=driver.find_element(By.XPATH,adrs_path).text
        gstin=driver.find_element(By.XPATH,gstin_path).text
        close.click()

        details[data.text] = {
                "Name": name,
                "PAN NO": pan_no,
                "Address": adrs,
                "GSTIN": gstin,
            }
    except Exception as e:
        print(f"Error occurred: {e}")
    
    n += 1

print(details)
    

driver.close()