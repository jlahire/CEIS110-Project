#Name: Michael Pabst
#Date: 2024-10-012

from noaa_sdk import NOAA
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

name = "Michael Pabst"
print(name)
endDate = datetime.now().strftime('%Y-%m-%d')
startDate = (datetime.now() - timedelta(days=14)).strftime('%Y-%m-%d')

print(f"Start Date: {startDate}")
print(f"End Date: {endDate}")

n = NOAA() 
observations = n.get_observations('30120', 'us', start=startDate, end=endDate)
temp = []
humidity = []

for obs in observations:
    temp.append(obs['temperature']['value'])
    humidity.append(obs['relativeHumidity']['value'])
    print(obs['timestamp'], '\t', 
          obs['temperature']['value'], '\t', 
          obs['relativeHumidity']['value'], '\t',
          obs['textDescription'])

temp = list(filter(None, temp))  
humidity = list(filter(None, humidity))   

# Temp vs Hmdty
plt.figure()
plt.plot(temp, label="temperature")
plt.plot(humidity, label='humidity')
plt.legend()
plt.suptitle('Temperature vs Humidity')  
plt.savefig('weather.png')  

# Box Plot
plt.figure()
box_data = [temp, humidity]
plt.boxplot(box_data, tick_labels=['Temperature', 'Humidity'])
plt.suptitle('Box Plot')  
plt.savefig('boxplot.png')  

avg_temp = sum(temp) / len(temp)
low_temp = min(temp)
high_temp = max(temp)
print('Weather Statistics')
print('The average temperature was: ', avg_temp)
print('The lowest temperature was: ', low_temp)
print('The highest temperature was: ', high_temp)
