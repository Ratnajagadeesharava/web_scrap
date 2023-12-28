from typing import List
from models.credentials import Credential


class Tenant:
    def __init__(self,tenant_name:str,environment:str):
        self.BASIC_URL = 'https://'+tenant_name+'.'+environment+'.nslhub.com'
        self._credentials = []
        self._admin_credentials = []
        
    
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

    
    
    
