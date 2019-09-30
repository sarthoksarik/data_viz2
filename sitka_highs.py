import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as dayweather:
    reader = csv.reader(dayweather)
    header_row = next(reader)

    dates, high_temps = [], []
    for r in reader:
        crnt_date = datetime.strptime(r[2], '%Y-%m-%d')
        high = r[5]
        high_temps.append(high)
        dates.append(crnt_date)

    # plot high temperatures

    plt.xkcd()  # using xkcd style
    fig, ax = plt.subplots()
    ax.plot(dates, high_temps, label="High Temperatures")

    # format style of the plot
    plt.title("Daily High Temperatures of Sitka")
    plt.xlabel("days")
    fig.autofmt_xdate()
    plt.ylabel("high temperatures")
    plt.tick_params('both', which='minor', labelsize=16)

    plt.legend()
    plt.tight_layout()
    plt.show()
