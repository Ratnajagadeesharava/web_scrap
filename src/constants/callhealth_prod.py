from models.credentials import Credential
from models.tenant import Tenant

callhealth_prod:Tenant = Tenant("callhealth","production")
callhealth_prod.add_credential( Credential("kavyasri.regalla@nslhub.com","Kavya"))
callhealth_prod.add_mcc_layout_url(url="https://callhealth.carnivalsb.nslhub.com/cdui/custom-mylibrary?siteLayoutId=64a79e456ba68f1d6cc373b1")
# print(callhealth_prod.get_mcc_layout_urls)

