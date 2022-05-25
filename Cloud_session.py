# get data from cloud and save
import json
import requests

session = requests.Session()

servertoken="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
cloudHeaders={"Content-Type": "application/json","Authorization": "Bearer %s" %servertoken}
url="https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.com"

r = session.get(url, headers=cloudHeaders, timeout=(2,5))

file_path= file_path # file_path= fileFolder_save + file_name + '.json' # save json file
with open(file_path, "w+") as f:
    json.dump(json.loads(r.text), f)
