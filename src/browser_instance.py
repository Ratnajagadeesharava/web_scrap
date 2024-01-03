
import requests
from models.tenant import Tenant
from bs4 import BeautifulSoup
from requests import Response,get,Timeout
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


class BrowerInstance:
    def __init__(self,tenant:Tenant):
        self.tenant = tenant
        
    def scrap_from_local(self,url:str):
        res = requests.get(url)
        soup:BeautifulSoup = BeautifulSoup(res.text,features='html.parser')
        mylibrary = soup.find_all("app-mylibrary")[0]
        print(mylibrary)
        soup2 = BeautifulSoup(str(mylibrary),features='html.parser')
        sections = soup2.find_all("section")
        
        
        

    def scrap_mcc_without_login(self)->None:
        urls:List[str] = self.tenant.mcc_layout_urls        
        for url in urls:
            html = self.get_html(url)
            soup:BeautifulSoup = BeautifulSoup(html,features='html.parser')
            mcc_element = soup.find_all("app-mylibrary")
            if mcc_element  == "Exception":
                return
            else:
                print(mcc_element)
            
    
            
    def get_html(self,url:str)->str:
        driver = webdriver.Edge()
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        try:
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'app-mylibrary')))
            driver.refresh()
            driver.refresh()
            driver.get(url)
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'app-mylibrary')))
            return driver.page_source
        except Exception:
            return "Exception"

    def login(self)->None:
        # self.driver.get(self.tenant.LOGIN_URL)
        print(self.driver.page_source)
        
       