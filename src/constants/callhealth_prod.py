from models.credentials import Credential
from models.tenant import Tenant

callhealth_prod:Tenant = Tenant("callhealth","production")
callhealth_prod.add_credential( Credential("kavyasri.regalla@nslhub.com","Kavya"))


