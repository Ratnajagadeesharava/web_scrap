from bs4 import BeautifulSoup
from browser_instance import BrowerInstance
from configs.constants import BASE_URL, LOGIN_URL
import requests

from  constants.callhealth_prod import callhealth_prod

class Main:
    def __init__(self):
        brower_instance = BrowerInstance(callhealth_prod)
        # brower_instance.scrap_mcc_without_login()
        # self.brower_instance.login()
        url = "http://127.0.0.1:5500/callhealth.html"
        brower_instance.scrap_from_local(url)

if __name__ == "__main__":
    main:Main = Main()