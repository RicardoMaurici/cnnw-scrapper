# -*- coding: utf-8 -*-
import pytz
import datetime
import time
from predictor.risk import predictRisk
from predictor.category import predictCategory
from predictor.entity import predictEntities
from predictor.tags import predictTags
from textmining import removeAccents, removeChars, removeNumbers, clearString
from util_mongo_api import checkExistence, storeNews


class ProcessData(object):
    def process_data(self, data):
        start = time.time()
        news = dict(data)
        #verify if url exists in the mongo db
        if checkExistence(news['link']) == False:
            #append headline into news body if exists
            if 'headline' in news.keys():
                headline = list()
                headline.append(news['headline'])
                news['body'] =  headline + news['body']

            #trasnform body into a big clean string
            body = clearString(" ".join(news['body']))
            #leave function if string has less than 100 characters
            bodysize = len(body)
            if bodysize < 100:
                return

            #saves clean body
            news['body'] = body[:500]

            #get published date and delete date key
            news['published_date'] = news['date']
            del news['date']

            #get scraped date
            news['scrapped_date'] = datetime.datetime.now(pytz.timezone(
                'America/Sao_Paulo')).strftime('%d-%m-%Y %H:%M:%S')

            #rename keys link to url
            news['url'] = news['link']
            del news['link']

            #getting domain
            url = news['url']
            domain = [word for word in url.split('/') if
                ('.com' in word) or ('.br' in word) or ('.org' in word)]
            news['domain'] = domain.pop()

            #remove numbers and chars from body
            body = removeChars(body.encode('utf8'))
            body = removeNumbers(body.encode('utf8'))

            #predic entities
            news['entities'] = predictEntities(body)

            #remove accents from body
            body = removeAccents(body)

            #predict risk
            news['risk'] = predictRisk(body)

            #predict category
            news['categories'] = predictCategory(body)
            if 'category' in news.keys():
                del news['category']

            #predic tags
            news['tags'] = predictTags(body)

            #store in the mongodb
            status = storeNews(news)
            if status == True:
                print "********* Storage in mongo successful! ***********"
            else:
                print "------------ Storage in mongo failed! ------------"

            #print process_data time for the news
            end = time.time()
            print "****** time for {} chars :{}".format(bodysize, end - start)

        else:
            print "********************************************"
            print "News already in the mongodb, passing to next"
