from typing import List
from models.credentials import Credential


class Tenant:
    def __init__(self,tenant_name:str,environment:str):
        self.BASIC_URL = 'https://'+tenant_name+'.'+environment+'.nslhub.com'
        self._credentials = []
        self._admin_credentials = []
        self._mcc_layout = []
        
    
    @property
    def LOGIN_URL(self)->str:
        return self.BASIC_URL+'/login'
    
    @property
    def credentials(self)->List[Credential]:
        return self._credentials
    
    def add_credential(self,credential:Credential)->None:
        self._credentials.append(credential)

    def add_admin_credential(self,credential:Credential)->None:
        self._admin_credentials.append(credential)

    @property
    def admin_credentials(self)->List[Credential]:
        return self._admin_credentials

    @property
    def mcc_layout_urls(self)->List[str]:
        return self._mcc_layout
    
    def add_mcc_layout_url(self,url:str)->List[str]:
        self._mcc_layout.append(url)
        return self._mcc_layout
    
    
    
