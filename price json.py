import urllib.request
import re
import json
import datetime
print(datetime.datetime.now())

stocklist = ['SPOST','DBS','UOB','OCBC']
for stock in stocklist:
	html = 'http://www.bloomberg.com/markets/api/bulk-time-series/price/' + stock + '%3ASP?timeFrame=1_MONTH'
	htmlfile = urllib.request.urlopen(html)
	htmltext = htmlfile.read()
	data = json.loads(htmltext.decode(encoding='utf-8'))
	dataprice = data[0]['lastPrice']
	previous = data[0]['price'][-2]['value']
	changed = round((dataprice - previous)/previous * 100, 2)
	if changed < 0:
		direction = "DOWN"
	elif changed == 0:
		direction = "UNCHANGED"
	else:
		direction = "UP"
	print(stock + ": " + str(data[0]['lastPrice']) + "---" + direction + " " + str(changed)+ "%")
	

next = 'http://www.bloomberg.com/markets/api/bulk-time-series/price/STI%3AIND?timeFrame=1_MONTH'
nextfile = urllib.request.urlopen(next)
nexttext = nextfile.read()
nextdata = json.loads(nexttext.decode(encoding='utf-8'))
previousday = nextdata[0]['price'][-2]['value']
print(nextdata[0]['price'][-2]['date'])
nextdata = nextdata[0]['lastPrice']
change = round((nextdata - previousday)/previousday * 100, 2)
if change < 0:
	directions = "DOWN"
elif change == 0:
	directions = "UNCHANGED"
else:
	directions = "UP"

print("STI: " + str(nextdata) + "---" + directions + " " + str(change)+ "%" )