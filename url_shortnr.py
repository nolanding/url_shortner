#62 bit map
import sys, getopt
import re
prime = 1000000009

def idToShortURL(id): 
	characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	shortURL = "" 
	
	# for each digit find the base 62 
	while(id > 0): 
		shortURL += characters[id % 62] 
		id //= 62

	# reversing the shortURL 
	return shortURL[len(shortURL): : -1] 

def shortURLToId(url): 

	id = 0
	for i in url: 
		val_i = ord(i) 
		if(val_i >= ord('a') and val_i <= ord('z')): 
			id = id*62 + val_i - ord('a') 
		elif(val_i >= ord('A') and val_i <= ord('Z')): 
			id = id*62 + val_i - ord('Z') + 26
		else: 
			id = id*62 + val_i - ord('0') + 52
	return id


def shortner(url):
	# print(url)
	pattern = '''(.com/|.org/|.gov/|.in/)'''
	urls= re.split(pattern, url) 
	print(urls)
	site = urls[0] + urls[1]
	content = urls[2]
	id = shortURLToId(content)
	id = id%prime
	shortURL = idToShortURL(id) 
	shortURL = 'www.urlshortner.com/' + shortURL
	return shortURL

# if __name__ == "__main__":
# 	res_map = {}
# 	url = main(sys.argv[1:])
# 	if len(url) == 0:
# 		with open('url.txt') as f:
# 			url = f.readline()
# 	# print(url)
# 	pattern = '''(.com/|.org/|.gov/|.in/)'''
# 	urls= re.split(pattern, url) 
# 	print(urls)
# 	site = urls[0] + urls[1]
# 	content = urls[2]
# 	id = shortURLToId(content)
# 	id = id%prime
# 	shortURL = idToShortURL(id) 
# 	shortURL = 'www.urlshortner.com/' + shortURL
# 	if url in res_map:
# 		res_map[url] = shortURL
# 	else:
# 		print("try something else, url already has a key")
# 	print("Short URL from url is : ", shortURL) 
# 	print(res_map)
