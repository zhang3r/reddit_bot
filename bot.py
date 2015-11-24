from urllib.request import urlopen
import http
from http.client import HTTPConnection as reddit_connect
import requests
import requests.auth

#1. login
#2. search within a subreddit sort by new
#3. for the top 10 result
#4. analyize post
#5. select answer
#6. post comment

class bot:

	def __init__(self):
		self.client_id = 'CLIENT_ID'
		self.secret = 'SECRET_ID'
		self.type_= 'code'
		self.state='STATE'
		self.redirect_uri='localhost'
		self.duration = 'temporary'
		self.scope = 'edit,save,submit'
		self.username = 'REDDIT_USERNAME'
		self.password = 'PASSWORD'

	def login(self):
		#api/v1/authorize?client_id={0}&response_type={1}&state={2}&redirect_uri={3}&duration={4}&scope={5}".format(self.client_id,self.type_,self.state,self.redirect_uri,self.duration,self.scope)
		client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.secret)
		post_data ={ "grant_type": "password","username":self.username, "password":self.password}
		headers = {"User-Agent":"mybot by marullus"}
		response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers= headers)
		response_json = response.json()
		print(response_json)


def main():
	a = bot()
	a.login()


if __name__ == '__main__':
	main()
