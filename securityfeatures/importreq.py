# importing the requests library
import requests, urllib, json, OpenSSL
import ssl
from db_adapter import DbAdapter
from security import Security

# api-endpoint
URL = "http://52.21.228.13:5000/sources?column=url&column=name&column=id"

response = urllib.urlopen(URL)

data = json.loads(response.read())

dba = DbAdapter.init("postgres",
					 "psycopg2",
					 "tow-haystack.cdjb0wztrzlf.us-east-1.rds.amazonaws.com",
					 "HAYSTACK",
					 "towhack",
					 "saturdayhackday"
                    )

for i in range(len(data)):
	urlinfo = data[i]['url']
	name = data[i]['name']
	security_entity_id = data[i]['id']
	
	try:
		ssl_value = ssl.get_server_certificate((urlinfo,443))
		certificate = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM,ssl_value)
		issued_by = certificate.get_issuer().CN
		issued_to = certificate.get_subject().CN

		entity = Security(name,urlinfo,ssl_value,security_entity_id,issued_by,issued_to)
		entity.insert()
	except:
		entity = Security(name,urlinfo,None,security_entity_id,issued_by,issued_to)
		entity.insert()
		