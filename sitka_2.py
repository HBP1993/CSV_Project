#using the datetime module
#adding dates to the x asix for the month of July 2018

import csv
from datetime import datetime
open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter =",")
header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []

# test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
# print(test_date)


for row in csv_file:
    highs.append(int(row[5]))
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)
    
print(highs)
print(dates)

import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(dates, highs, c ='red')


plt.title('Daily high temperature, July 2018', fontsize = 16)

plt.xlabel("Month of July 2018")

plt.ylabel("temperature(f", fontsize = 16)

plt.tick_params(axis = "both", which = "major", labelsize = 16)

fig.autofmt_xdate()

plt.show()