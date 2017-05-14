
from twitter import *
import json


class Db_Controller(object):
	def __init__(self, debug = 0):

		with open('apikeys.json') as data_file:
			credentials = json.load(data_file)["twitter"]

		self.twitter = Twitter( 
			auth = OAuth(credentials["access_key"],
				credentials["access_secret"],
				credentials["consumer_key"],
				credentials["consumer_secret"]
				))

		if debug:
			print("debug is on")
			self.debug = True
		else:
			self.debug = False

	def insert(self, data):
		results = self.twitter.statuses.update(status = data)
		if self.debug:
			print("Added to database: %s" % data)

	def get_all(self):

		results = self.twitter.statuses.user_timeline(screen_name = "NotOurDatabase")
		if self.debug:
			for status in results:
				print("(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"]))

		return results

	def get_user(self, user, all_tweets = []):
		if not all_tweets:
			all_tweets = self.get_all()
		user_tweets = []
		for status in all_tweets:
			if status["text"].split(" ")[1].split("'")[0] == user:
				user_tweets.append(status)

		return user_tweets

	def get_service(self, service, all_tweets = []):
		if not all_tweets:
			all_tweets = self.get_all()

		service_tweets = []

		for status in all_tweets:
			if status["text"].split(" ")[2] == service:
				service_tweets.append(status)

		return service_tweets

	def save_pw(self, user, service, pw, link):
		self.insert("{0}\n Not {1}'s {2} password: {3}".format(link, user, service, pw) )

	def get_pw(self, user, service):
		user_tweets = self.get_user(user)
		passwords = self.get_service(service, user_tweets)
		return passwords[0]["text"].split(":")[1].split(" ")[1]

	def save_pw_from_strings(self, pwstring, link):
		self.insert("Not {0} {1}".format(pwstring, link))


if __name__ == '__main__':
	db = Db_Controller()
	pw = db.get_pw("Shane", "Google")
	print(pw)


	

