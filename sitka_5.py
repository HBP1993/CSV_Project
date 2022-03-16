#1) changing the file to include all the date for the year of 2018
#2) change the title to daily low and high temperature -2018
#3) extract the low temp from the file and add to chart 
#4) shade in  the area between high and low 


import csv
from datetime import datetime


open_file = open("death_valley_2018_simple.csv", "r")
#print('Daily Low and High temperature of 2018')
csv_file = csv.reader(open_file, delimiter =",")
header_row = next(csv_file)

print(header_row)

dv_header = {}
for index, column_header in enumerate(header_row):
    dv_header[column_header] = index
    print(index, column_header)



highs = []
dates = []
lows = []

# test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
# print(test_date)


for row in csv_file:
    
    #try and except method is to catch the exception or error if any
    try:
        current_data = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        
    #this only happens or comes into play of value error take place  
    except ValueError:
        print(f'missing data for {current_data}')
        
    else:
        
        highs.append(high)
        lows.append(low)
        dates.append(current_data)
        i = 0
        while i == 0:
            dv_heading = row[dv_header["NAME"]]
            i += 1

print(dv_heading)
        
        # highs.append(int(row[4]))
        # lows.append(int(row[5]))
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # dates.append(current_date)
    
print(highs)
print(dates)


#sitka weather
si_open_file = open("sitka_weather_2018_simple.csv", "r")
si_csv_file = csv.reader(si_open_file, delimiter=",")

si_header_row = next(si_csv_file)

si_header = {}
for index, column_header in enumerate(header_row):
    si_header[column_header] = index
    
si_highs = []
si_dates = []
si_lows = []

for row in si_csv_file:
    si_highs.append(int(row[5]))
    si_lows.append(int(row[6]))
    si_current_date = datetime.strptime(row[2], '%Y-%m-%d')
    si_dates.append(si_current_date)

    i = 0
    while i == 0:
        si_heading = row[si_header["NAME"]]
        i += 1
print(si_heading)
   
print(si_highs[:10])
    
print("******PLOT*******")
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, sharey=True)
fig.suptitle("Temperature comparision between " + si_heading + " and " + dv_heading)
fig.autofmt_xdate()

print("****Sikta PLOT*****")
ax1.plot(si_dates, si_highs, c="red")
ax1.plot(si_dates, si_lows, c="blue")
# filling the color between the lines
ax1.fill_between(si_dates, si_highs, si_lows, facecolor="blue", alpha=0.1)
#alpha value is always between 0-1
ax1.set_title(si_heading, fontsize=16)

print("*****DEATH VALLEY PLOT*****")
ax2.plot(dates, highs, c="red")
ax2.plot(dates, lows, c="blue")
# filling the color between the lines
ax2.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
ax2.set_title(dv_heading, fontsize=16)

#fig = plt.figure()

plt.show()
