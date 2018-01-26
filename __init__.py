from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill

__author__ = 'chris-rohrer'


class InternetWeatherSkill(MycroftSkill):
    def __init__(self):
        super(InternetWeatherSkill, self).__init__(name="InternetWeatherSkill")

    def initialize(self):
        internet_weather_intent = IntentBuilder("InternetWeatherIntent"). \
            require("InternetWeather").build()
        self.register_intent(internet_weather_intent, self.handle_internet_weather_intent)

    def handle_internet_weather_intent(self, message):
        self.speak_dialog("internet.weather")
        self.speak(message.data.get('utterance'))

    def stop(self):
        pass


def create_skill():
    return InternetWeatherSkill()
