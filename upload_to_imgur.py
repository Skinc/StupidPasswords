import json
from pprint import pprint
from imgurpython import ImgurClient

with open('apikeys.json') as data_file:
	credentials = json.load(data_file)

CLIENT_ID = credentials["client-id"]
CLIENT_SECRET = credentials["client-secret"]

client = ImgurClient(CLIENT_ID, CLIENT_SECRET)

f  =client.upload_from_path("passwords.png", anon=False)

print(f["link"])