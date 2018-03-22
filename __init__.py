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
        places = GeoText("London is a place")

        first_city = "Basel"
        second_city = "Amsterdam"

        r = requests.get("https://wondernetwork.com/pings/"+first_city+"/"+second_city)
        p = re.compile('\<tr\>\W*\<td class=\"is-bucket is-bucket-0\"\>\W*<div class=\"td-item\"\>([0-9\.]+ms)\</div>\W*\</td>\W*\<td class=\"is-bucket is-bucket-0\"\>\W*<div class=\"td-item\"\>([0-9\.]+ms)\</div>\W*\</td>\W*\<td class=\"is-bucket is-bucket-0\"\>\W*<div class=\"td-item\"\>([0-9\.]+ms)\</div>\W*\</td>\W*\<td class=\"is-bucket is-bucket-0\"\>\W*<div class=\"td-item\"\>([0-9\.]+ms)\</div>\W*\</td>\W*\<td class=\"is-bucket\">([0-9:\- ]+)</td>')
        matches = p.findall(r.content)
        
        self.speak("The average response time from "+first_city+" to "+second_city+" was "+matches[0][0]+" at "+matches[0][4])
        self.speak("Debug: The received message was " + message.data.get('utterance'))
        self.speak(places.cities.pop())

    def stop(self):
        pass


def create_skill():
    return InternetWeatherSkill()
