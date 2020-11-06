This is a url shortner which has two functions 
1. (url_shortner)Shortens the url for any get requests. This also maintains the map such that in case if any shorten url is clicked more than 1 time then it increases its count. It also has functionality if someone gets the already existing shorturl then if date of existing url is older than 365 days then its count gets increased.
2. (link_to_site)This function returns the actual url for shorturl and whenever short url is called more than 1 time it increases the count.


In order the run this application. I'm assuming python, pip and virualenv is already installed on your system

Steps
1. Create a new virtualenv (virtualenv env)
2. Install flask in that environment (pip install flask)
3. Run the present .sh file using command (sh shorter.sh)

Now your api is up and running