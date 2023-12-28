
from models.tenant import Tenant
import werkzeug
from selenium.webdriver import Edge


class BrowerInstance:
    def __init__(self,tenant:Tenant):
        self.tenant = tenant
        self.driver = Edge(executable_path=r'C:\projects\nsl_web_data\src\msedgedriver.exe')
        self.driver.get('https://www.example.com')
    
        

        
        
    def login(self)->None:
        # self.driver.get(self.tenant.LOGIN_URL)
        print(self.driver.page_source)
        
       