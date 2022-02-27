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





for index, column_header in enumerate(header_row):
    print(index, column_header)



highs = []
dates = []
lows = []

# test_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
# print(test_date)


for row in csv_file:
    
    try:
        current_data = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        
        
    except ValueError:
        print(f'missing data for {current_data}')
        
    else:
        
        highs.append(high)
        lows.append(low)
        dates.append(current_data)
        
        # highs.append(int(row[4]))
        # lows.append(int(row[5]))
        # current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # dates.append(current_date)
    
print(highs)
print(dates)

import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(dates, highs, c ='red')
plt.plot(dates, lows, c ='blue')

plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1)
#alpha value is always between 0-1


plt.title('Daily high temperature, July 2018', fontsize = 16)

plt.xlabel("Month of July 2018")

plt.ylabel("temperature(f", fontsize = 16)

plt.tick_params(axis = "both", which = "major", labelsize = 16)

fig.autofmt_xdate()

plt.show()
