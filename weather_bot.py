from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import json
import pyowm

from geopy.geocoders import Nominatim

from constants import HELLO_MSG, WEATHER_STATUS_TO_MSG, KELVIN_DELTA


def get_weather_status(user_city):
    location = geolocator.geocode(user_city)
    if location is None:
        return user_city
    location_city = location[0].split(",")[0]
    location_country = location[0].split(",")[-1]

    weather = owm.weather_at_coords(location.latitude, location.longitude).to_JSON()
    weather = json.loads(weather)["Weather"]
    weather_status = weather["status"]
    try:
        status = WEATHER_STATUS_TO_MSG[weather_status]
    except KeyError:
        status = ""

    temperature = round(weather["temperature"]["temp"] - KELVIN_DELTA)
    if temperature > 0:
        temperature = f"+{temperature}"
    elif temperature == 0:
        temperature = str(temperature)
    else:
        temperature = f"-{temperature}"

    response = f"{location_city},{location_country}: {status}температура {temperature}"
    return response


def start(update, context):
    update.message.reply_text(HELLO_MSG)


def reply(update, context):
    user_text = update.message.text
    out = get_weather_status(user_text)
    update.message.reply_text(out)


if __name__ == "__main__":
    try:
        token_file = open("tokens.txt", "r")
        lines = token_file.readlines()
        bot_token = lines[0].rstrip()
        owm_token = lines[1].rstrip()
    except FileNotFoundError:
        print("Please create tokens.txt")
    except IndexError:
        print("Incorrect number of tokens")

    geolocator = Nominatim(user_agent="ru")
    owm = pyowm.OWM(owm_token)
    updater = Updater(bot_token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()
    updater.idle()
