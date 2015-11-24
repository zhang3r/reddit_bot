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
		self.username = 'REDDIT_USERNAME'
		self.password = 'REDDIT_PASSWORD'

	def login(self):
		client_auth = requests.auth.HTTPBasicAuth(self.client_id, self.secret)
		post_data ={ "grant_type": "password","username":self.username, "password":self.password}
		headers = {"User-Agent":"mybot by marullus"}
		response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers= headers)
		response_json = response.json()
		return response_json['access_token']
	def search(self, subreddit, access_token):
		return

	def comment_generator(self):
		return 'hello world'

	def post_comment(self, comment):



def main():
	bot = bot()
	reddit_access_token=bot.login()
	bot.search(subreddit='relationships',access_token=reddit_access_toekn)


if __name__ == '__main__':
	main()
