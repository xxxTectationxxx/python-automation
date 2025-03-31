from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
# option.binary_location = "/usr/bin/google-chrome" 
option.add_experimental_option('detach', True)

browser = webdriver.Chrome(options=option)
browser.implicitly_wait(10)

# Membuka website dan melakukan maximize website
browser.get("https://demoqa.com/webtables")
browser.maximize_window()


Data_Registration = {
    "FirstName" : ["Raka", "Raden", "Lukas"],
    "LastName" : ["Gibran", "Ayu", "Ondo"],
    "Email" : ["Raka123@gmail.com", "Ayu321@gmail.com", "Lukas99@gmail.com"],
    "Age" : [32, 21, 40],
    "Salary" : [20000000, 5000000, 45000000],
    "Departement" : ["Gubernur", "Permaisuri", "Hero Mobile Legends"]
}

for i in range(len(Data_Registration["FirstName"])):
    # Menekan tombol add menggunakan attribute id
    browser.find_element(By.ID, 'addNewRecordButton').click()
    
    # Menginputkan mengggunakan Xpath
    browser.find_element(By.XPATH, '//input[@id="firstName"]').send_keys(f'{Data_Registration["FirstName"][i]}')
    browser.find_element(By.XPATH, '//input[@id="lastName"]').send_keys(f'{Data_Registration["LastName"][i]}')
    browser.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys(f'{Data_Registration["Email"][i]}')
    browser.find_element(By.XPATH, '//input[@id="age"]').send_keys(f'{Data_Registration["Age"][i]}')
    browser.find_element(By.XPATH, '//input[@id="salary"]').send_keys(f'{Data_Registration["Salary"][i]}')
    browser.find_element(By.XPATH, '//input[@id="department"]').send_keys(f'{Data_Registration["Departement"][i]}')

    # Menekan Tombol Submit
    browser.find_element(By.XPATH, '//button[@id="submit"]').click()
    
    print(f"Data Ke {i + 1} Berhasil")
    sleep(1)




