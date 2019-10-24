import os
import requests
import sys


class TrelloAPI(object):
    def __init__(self):
        self.text = input("Trello InBox Title: ")
        self.url = 'https://trello.com/1/cards'
        self.params = (
            ('key', os.environ.get('TRELLO_API_KEY')),
            ('token', os.environ.get('TRELLO_API_TOKEN')),
            ('idList', os.environ.get('LIST_ID')),
            ('name', self.text),
        )

    def post(self):
        try:
            res = requests.post(self.url, params=self.params)
            print(res)
        except:
            sys.exit()
