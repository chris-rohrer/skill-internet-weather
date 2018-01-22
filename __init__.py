from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler


class InternetWeatherSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler(IntentBuilder().require('InternetWeather'))
    def handle_internet_weather(self, message):
        self.speak_dialog('internet.weather')


def create_skill():
    return InternetWeatherSkill()

