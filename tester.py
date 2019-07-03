from os import path
import pickle
import json
import requests

apikey = "9U9CW3F6G8W9NX5A"

if not path.exists("trial.pickle"):
	params = {'function':'TIME_SERIES_WEEKLY','symbol':'MSFT','apikey':apikey}
	trial = requests.get("https://www.alphavantage.co/query",params=params)
	with open('trial.pickle','wb') as f:
		pickle.dump(trial,f)
else:
	with open('trial.pickle','rb') as f:
		trial = pickle.load(f)

# for key, value in trial.json()['Monthly Time Series'].items():
# 	print(key,value)

# print(trial.json()['Time Series (Daily)'])

print(trial.json()['Weekly Time Series'])


    
