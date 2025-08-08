from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormAutomation:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)

    def form_link(self , url):
        self.driver.get(url)
        self.driver.maximize_window()

    def informations(self):
        self.name_field = self.driver.find_element(By.XPATH , "//*[@id='name']")
        self.email_field = self.driver.find_element(By.XPATH , "//*[@id='email']")
        self.message_field = self.driver.find_element(By.XPATH , "//*[@id='message']")
        self.submit_btn = self.driver.find_element(By.XPATH , "/html/body/div/form/button")

    def form_filler(self , name , email , message):
        WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//*[@id='name']")))
        self.name_field.send_keys(name)
          
        WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//*[@id='email']")))
        self.email_field.send_keys(email)

        WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//*[@id='message']")))
        self.message_field.send_keys(message)

    def submit(self):
        WebDriverWait(self.driver , 10).until(EC.element_to_be_clickable((By.XPATH , "/html/body/div/form/button")))
        self.submit_btn.click()
    
    def quit(self):
        self.driver.close()
        print("submitted successfully!")
    