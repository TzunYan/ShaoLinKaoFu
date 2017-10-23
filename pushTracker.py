import pytz
from datetime import datetime
import requests
import json

def checkTodayCommit(pushTime):

    time = datetime.strptime(pushTime,'%Y-%m-%dT%H:%M:%SZ')
    x = pytz.timezone('Africa/Accra').localize(time)
    bx = x.astimezone(pytz.timezone('Asia/Taipei'))

    if bx.strftime('%Y:%m:%d') == datetime.now().strftime('%Y:%m:%d'):
        print("Yes, you commit")


githubRequest = requests.get('http://api.github.com/users/otakuemperor/events')
rowData = json.loads(githubRequest.text)

for i in range(len(rowData)):
    if(rowData[i]['type'] == 'PushEvent'):
        checkTodayCommit(rowData[i]['created_at'])
        break

print("No, you don't")
