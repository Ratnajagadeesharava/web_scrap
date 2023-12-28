from bs4 import BeautifulSoup
from browser_instance import BrowerInstance
from configs.constants import BASE_URL, LOGIN_URL
import requests

from  constants.callhealth_prod import callhealth_prod

class Main:
    def __init__(self):
        self.brower_instance = BrowerInstance(callhealth_prod)
        # self.brower_instance.login()
        

if __name__ == "__main__":
    main:Main = Main()