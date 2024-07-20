import requests
from bs4 import BeautifulSoup

gj = "https://weather.com/weather/today/l/2363c1aa69a15bc745936b56084e099efeb412070b1f5c2bc959e47ebe924000"
nv = "https://weather.com/weather/today/l/186a81e22474b3fb49f488cbf30fb246b6fdbe59c85c554439e1fc7992e7601f"

def weather_scraper(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # High and Low temperature
    forecast = soup.find(class_ = "CurrentConditions--tempHiLoValue--3T1DG")
    forecast_weather = forecast.find_all('span', {'data-testid': 'TemperatureValue'})
    high_low = [span.get_text() for span in forecast_weather]
    high = high_low[0]
    high = high.rstrip(high[-1])
    low = high_low[1]
    low = low.rstrip(low[-1])

    # Humidity
    weather_data = soup.find(class_ = "TodayDetailsCard--detailsContainer--2yLtL")
    weather_data = weather_data.find_all('div', {'data-testid': 'wxData'})
    weather_data = [span.get_text() for span in weather_data]
    low_high = weather_data[0]
    wind_direction = weather_data[1]
    humidity = weather_data[2]
    dew_point = weather_data[3]
    pressure = weather_data[4]
    uv_index = weather_data[5]
    visibility = weather_data[6]
    moon_phase = weather_data[7]


    # Current Temperature and Conditions
    current_weather = soup.find_all(class_ = "CurrentConditions--primary--2DOqs")
    for weather in current_weather:
        current_temp = weather.find(class_ = "CurrentConditions--tempValue--MHmYY").get_text()
        conditions = weather.find(class_ = "CurrentConditions--phraseValue--mZC_p").get_text()
        current_temp = current_temp.rstrip(current_temp[-1])

    return current_temp, conditions, high, low, humidity, uv_index

if __name__ == "__main__":

    weather_url = "https://weather.com/weather/today/l/2363c1aa69a15bc745936b56084e099efeb412070b1f5c2bc959e47ebe924000"

    weather_conditions = weather_scraper(weather_url)

    print(weather_conditions[0])

    # print(f"\nCurrent Conditions: {current_temp}F, {conditions}\n")