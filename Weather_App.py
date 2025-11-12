import requests
from colorama import Fore
API_KEY = "a928d55c886a4254a701a1ee0ebbad5a"  #َََAPI Key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("نام شهر را وارد کنید: ")

# ساختن URL درخواست
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric&lang=fa"

# ارسال درخواست به API
response = requests.get(url)
data = response.json()

if response.status_code == 200:
    city_name = data["name"]
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print(f"\n🏙 شهر: {city_name}")
    print(f"🌡 دما: {temp}°C")
    print(f"☁️ وضعیت: {weather}")
    print(f"💧 رطوبت: {humidity}%")
    print(f"💨 سرعت باد: {wind} m/s")
else:
    print("❌ شهر مورد نظر پیدا نشد یا خطایی رخ داده است.")
print(Fore.CYAN + f"🌡 دما: {temp}°C")
print(Fore.YELLOW + f"☁️ وضعیت: {weather}")
print(Fore.BLUE + f"💧 رطوبت: {humidity}%")