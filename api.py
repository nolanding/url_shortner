#!flask/bin/python
from flask import Flask
from url_shortnr import shortner
from datetime import date, timedelta, datetime

# dd/mm/YY hh:mm:ss
date_format = "%d/%m/%Y"

app = Flask(__name__)
res_map = {}


@app.route('/urlshortner', methods=['GET'])
def url_shortner():
	url = ''
	with open('url.txt') as f:
		url = f.readline()
	shortURL = shortner(url)
	today = datetime.now()
	c_date = today.strftime(date_format)
	print(shortURL)
	if shortURL not in res_map:
		data = [url,0, c_date]
		res_map[shortURL] = data
	else:
		data = res_map[shortURL]
		traffic = data[1]
		date_data = datetime.strptime(data[2], date_format) + timedelta(days = 365)
		if(date_data < today):
			data = [url,traffic, c_date]	
			res_map[shortURL] = data
			print(res_map)
		else:
			print("Try something else, url already has a key")
	print("Short URL from url is : ", shortURL)
	return res_map

@app.route('/thelink', methods=['GET'])
def link_to_site():
	link = ''
	with open('link.txt') as f:
		link = f.readline()
	if link in res_map:
		list = res_map[link]
		list[1] += 1
		res_map[link] =  list
		return res_map
	else:
		return 'No Match found'


if __name__ == '__main__':
    app.run(debug=True)