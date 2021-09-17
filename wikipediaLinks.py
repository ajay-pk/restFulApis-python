from flask import Flask
from flask_restful import Resource,Api,reqparse

# from selenium import webdriver
# from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import pandas as pd
import requests





# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
dataToBeSent = {}

URL = "https://en.wikipedia.org/wiki/"




app = Flask(__name__)
api = Api(app)




class generalLinks(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('q', required=True) 
        args = parser.parse_args()
        print(args['q'])
        
        
        
        page = requests.get(URL+args['q'])
        soup = BeautifulSoup(page.content, "html.parser")
        # print(soup)
        # results = soup.find_all("div", class_="style-scope ytd-video-renderer")
        # print(results)

        urls = []
        for link in soup.find_all('a'):
                urls.append(link.get('href'))
        return {"result":urls},200

api.add_resource(generalLinks,'/general_links')

if __name__=='__main__':
    app.run()