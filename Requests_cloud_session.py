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

    
    
    
# streaming data

try:
    print('start connecting!!!')
    with self.stream_session.get(url, headers=None, stream=True, timeout=5) as resp:
        for line in resp.iter_lines():
            if line:
                ts = int(json.loads(line)['result']['timestamp'])
                print(f'{self.opla_job_number} Timestamp received:', ts, 'at', time.time())
                if ts == self.last_timestamp:
                    print('******** timestamp issue !!! ********')
                    print(line)

                if ts < self.last_timestamp:
                    print('!!!*********************** out of sequence ********************!!!')
                    print(line)

                if ts > self.last_timestamp:
                    self.last_timestamp = ts
                            
except requests.exceptions.ReadTimeout as errt:
    print('streaming Error:', errt)
    # smart connection
    self.smart_connect()
            
except Exception as err:
    print('streaming Error other than read time:', err)
    time.sleep(1)
    self.get_stream()                            
