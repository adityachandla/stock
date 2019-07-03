from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
import requests
from urllib.request import urlopen,Request
import json
from bs4 import BeautifulSoup

apikey = "9U9CW3F6G8W9NX5A"

class Searcher(View):
	def get(self,request):
		if 'search' in request.GET:
			return self.search(request)
		return render(request,'prices/searcher.html')

	def search(self,request):
		value = request.GET['search']
		searchparams = {'function':'SYMBOL_SEARCH','apikey':apikey, 'keywords':value}
		response = requests.get("https://www.alphavantage.co/query",params=searchparams).json()
		if 'Error Message' not in response and 'bestMatches' in response:
			## making a list as dictionary does'nt work in templates
			matches = list()
			for i in response['bestMatches']:
				matches.append(Match(i['1. symbol'],i['2. name']))
			return render(request,'prices/results.html',{'matches':matches})
		else:
			return render(request,'prices/results.html',{'matches':[]})


class Stock(View):
	def get(self,request,symbol,name):
		url = self.getUrl(name)
		context = {'img_url':url, 'name':name, 'symbol': symbol}
		if 'get_data_for' in request.GET:
			return self.getDataTable(request,symbol)
		return render(request,'prices/stock.html',context)

	def getUrl(self,query):
		url="https://www.google.co.in/search?q="+query.replace(' ','+')+"&source=lnms&tbm=isch"
		rq = Request(url)
		rq.add_header('User-Agent',"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36")
		a = BeautifulSoup(urlopen(rq).read(),'html.parser').find("div",{"class":"rg_meta"})
		return json.loads(a.text)["ou"]

	def getDataTable(self,request,symbol):
		func = {'daily':'TIME_SERIES_DAILY','weekly':'TIME_SERIES_WEEKLY','monthly':'TIME_SERIES_MONTHLY'}
		data_attr = {'daily':'Time Series (Daily)', 'weekly':'Weekly Time Series', 'monthly':'Monthly Time Series'}

		searchparams = {'function':func[request.GET.get('get_data_for')],'symbol':symbol,'apikey':apikey}
		response = requests.get('https://www.alphavantage.co/query',params=searchparams).json()

		context = {'data':self.convert(response[data_attr[request.GET.get('get_data_for')]])}
		return render(request,'prices/data_table.html',context)

	def convert(self,data):
		l = list()
		for date,others in data.items():
			l.append(Data(date,others))
		return l


## utility classes
class Match:
	def __init__(self,symbol,name):
		self.symbol = symbol
		self.name = name

class Data:
	def __init__(self,date,other):
		self.date = date
		self.open_price = other['1. open']
		self.high = other['2. high']
		self.low = other['3. low']
		self.close_price = other['4. close']
		self.volume = other['5. volume']