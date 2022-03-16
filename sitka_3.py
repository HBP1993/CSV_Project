#1) changing the file to include all the date for the year of 2018
#2) change the title to daily low and high temperature -2018
#3) extract the low temp from the file and add to chart 
#4) shade in  the area between high and low 


import csv
from datetime import datetime
open_file = open("sitka_weather_2018_simple.csv", "r")


#print('Daily Low and High temperature of 2018')
csv_file = csv.reader(open_file, delimiter =",")
header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []
lows = []

# test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
# print(test_date)


for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)
    
print(highs)
print(dates)

import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(dates, highs, c ='red')
plt.plot(dates, lows, c ='blue')

plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
#to fill in the graph we need to give x-axis and y-axis location (here we have 2 y axis locations) 
#alpha value is always between 0-1


plt.title('Daily high temperature, July 2018', fontsize = 16)

plt.xlabel("Month of July 2018")

plt.ylabel("temperature(f", fontsize = 16)

plt.tick_params(axis = "both", which = "major", labelsize = 16)

fig.autofmt_xdate()

#plt.show()


'''how to create subplots (important for HW)'''
#we have to give 3 arguments
#i.e. number of rows(2), column(1) and which subplot we want to create first i.e. index (1)of the plot
plt.subplot(2,1,1) 
plt.plot(dates, highs, c='red')
plt.title ('Highs')

plt.subplot(2,1,2)
plt.plot(dates, lows, c='blue')
plt.title ('Lows')

#suptitle 
plt.suptitle("High and lows of Sitka, Alaskas 2018")

plt.show()

