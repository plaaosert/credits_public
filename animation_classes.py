# Contains all classes (just Weather)
import random
import math


class Weather:
    def __init__(self, precip, temp, wind, gust, wind_dir, humidity, days=2):
        self.precip = precip
        self.temp = temp
        self.wind = wind
        self.gust = gust
        self.wind_dir = wind_dir
        self.humidity = humidity
        self.weather_name = self.get_weather_name()
        self.days = days

    def __str__(self):
        return "{}% precipitation\n" \
               "{}F temperature\n" \
               "{}mph wind\n" \
               "{}mph gust\n" \
               "{} wind direction\n" \
               "{}% humidity\n" \
               "{}\n".format(
                    round(self.precip * 100, 2),
                    int(self.temp),
                    int(self.wind),
                    int(self.gust),
                    int(self.wind_dir),
                    round(self.humidity * 100, 2),
                    self.weather_name
               )

    def get_weather_name(self):
        # Clear/Sunny <> Cloudy/Rainy
        if self.humidity > 0.5:
            # Cloudy or rainy
            if self.precip > 0.4:
                if self.wind > 43:
                    return "Blizzard" if self.temp < 32 else "Hurricane"
                elif self.wind > 25:
                    return "Snowstorm" if self.temp < 32 else "Storm"
                else:
                    return "Snow" if self.temp < 32 else "Rain"
            elif self.precip > 0.25:
                return "Sleet" if self.temp < 32 else "Drizzle"

            if self.humidity > 0.8 or self.precip > 0.5:
                return "Overcast"
            elif self.humidity > 0.65 or self.precip > 0.3:
                return "Cloudy"
            else:
                return "Partly cloudy"
        else:
            if self.precip > 0.4:
                return "Snow" if self.temp < 32 else "Rain"
            elif self.precip > 0.2:
                return "Sleet" if self.temp < 32 else "Drizzle"

            return ("Sunny" if self.humidity < 0.1 else "Partly sunny") if self.humidity < 0.2 else "Clear"

    def mutate(self, steps=1):
        for i in range(steps):
            # Prefer 33% precip, move wind dir by +-3 each day, gust = speed x 2.1 - 2.6
            precip_move = random.randint(-100, 100) / 400.0
            precip_move += (random.randint(0, int(100 * abs(0.33 - self.precip))) / 200) * (-1 if 0.33 - self.precip < 0 else 1)
            self.precip = min(1, max(0, self.precip + precip_move))

            self.wind_dir = (self.wind_dir + random.randint(-3, 3)) % 8

            wind_move = random.randint(-100, 100) / 13
            wind_move += (random.randint(0, int(abs(15 - self.wind))) / 3) * (-1 if 15 - self.wind < 0 else 1)
            self.wind = max(0, self.wind + wind_move)

            adjusted_days = self.days - 282
            temp_target = 40 * (math.sin((2 * math.pi * adjusted_days) / 365 - math.pi / 3) + 1) + 20
            temp_move = random.randint(-100, 100) / 20
            temp_move += (random.randint(0, int(abs(temp_target - self.temp))) / 5) * (-1 if temp_target - self.temp < 0 else 1)
            self.temp = max(0, self.temp + temp_move)

            humidity_move = random.randint(-100, 100) / 500.0
            humidity_move += (random.randint(0, int(abs(0.2 - self.humidity))) / 200) * (-1 if 0.5 - self.humidity < 0 else 1)
            self.humidity = max(0, min(1, self.humidity + humidity_move))

            self.gust = self.wind * random.randint(210, 260) * 0.01
            self.days += 1

        self.weather_name = self.get_weather_name()


# 22.10.2009: Cloudy, precip 20%, temp 43, wind dir 6, 13 (25)
# 23.10.2009: Sunny, precip 4%, temp 52, wind dir 7, 12 (25)
# 24.10.2009: Partly sunny, precip 7%, temp 48, wind dir 1, 8 (20)
known_weathers = (
    Weather(0.203, 43, 13, 25, 6, 0.66),
    Weather(0.04, 52, 12, 25, 7, 0.1),
    Weather(0.07, 48, 8, 20, 1, 0.1, 200),
    Weather(0.07, 48, 8, 20, 1, 0.1, 528 + 200),
    Weather(-1, -1, -1, -1, -1, -1)
)

known_weathers[4].weather_name = "Connection lost...      "
