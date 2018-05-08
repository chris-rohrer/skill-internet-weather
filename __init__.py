from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from geotext import GeoText

import httplib
import re
import requests

httplib._MAXHEADERS = 1000

__author__ = 'chris-rohrer'


class InternetWeatherSkill(MycroftSkill):
    def __init__(self):
        super(InternetWeatherSkill, self).__init__(name="InternetWeatherSkill")

    def initialize(self):
        internet_weather_intent = IntentBuilder("InternetWeatherIntent"). \
            require("InternetWeather").build()
        self.register_intent(internet_weather_intent, self.handle_internet_weather_intent)

    def handle_internet_weather_intent(self, message):
        places = GeoText(message.data.get('utterance'))
        if places.cities.__len__() == 2:

            first_city = places.cities.pop(0)
            second_city = places.cities.pop(0)

            r = requests.get("https://wondernetwork.com/pings/"+first_city+"/"+second_city)
            p = re.compile('\<tr\>\W*\<td class=\"is-bucket is-bucket-0\"\>\W*<div class=\"td-item\"\>([0-9\.]+ms)\</div>\W*\</td>\W*\<td class=\"is-bucket is-bucket-0\"\>\W*<div class=\"td-item\"\>([0-9\.]+ms)\</div>\W*\</td>\W*\<td class=\"is-bucket is-bucket-0\"\>\W*<div class=\"td-item\"\>([0-9\.]+ms)\</div>\W*\</td>\W*\<td class=\"is-bucket is-bucket-0\"\>\W*<div class=\"td-item\"\>([0-9\.]+ms)\</div>\W*\</td>\W*\<td class=\"is-bucket\">([0-9:\- ]+)</td>')
            matches = p.findall(r.content)
        
            self.speak("The average response time from "+first_city+" to "+second_city+" was "+matches[0][0]+" at "+matches[0][4])
            #self.speak("Debug: The received message was " + message.data.get('utterance'))

        elif places.cities.__len__() < 2:
            self.speak("Did you mention a city?")
            self.speak("I heard the name of "+str(places.cities.__len__())+" cities.")

        else:
            self.speak("You mentioned "+str(places.cities.__len__())+" cities - I don't know what to do with that!")


    def stop(self):
        pass


def create_skill():
    return InternetWeatherSkill()
