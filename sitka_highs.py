import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs, lows, diffs = [], [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)
        diff = high - low
        diffs.append(diff)


# Plot the high temperatures.
plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', label="High Temps")
ax.plot(dates, lows, c='blue', label="Low Temps")
ax.plot(dates, diffs, c='green', label="Differences")

# Format plot.
plt.title("Daily high temperatures - 2018", fontsize=24)
plt.xlabel('Days', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.legend()
plt.tight_layout()


plt.show()
