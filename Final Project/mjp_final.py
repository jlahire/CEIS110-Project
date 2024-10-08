#Name: Michael Pabst
#Date: 2024-10-07

from noaa_sdk import NOAA
import matplotlib.pyplot as plt 

name = "Michael Pabst"
print(name)
startDate = '2024-09-24'
endDate = '2024-10-07'

n = NOAA()  # Corrected function name
observations = n.get_observations('30350', 'us', start=startDate, end=endDate)
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

# Plot Temperature vs Humidity
plt.figure()
plt.plot(temp, label="temperature")
plt.plot(humidity, label='humidity')
plt.legend()
plt.suptitle('Temperature vs Humidity')  # Corrected subtitle to suptitle
plt.savefig('weather.png')  # Corrected safefig to savefig

# Box Plot
plt.figure()
box_data = [temp, humidity]
plt.boxplot(box_data, labels=['Temperature', 'Humidity'])
plt.suptitle('Box Plot')  # Corrected subtitle to suptitle
plt.savefig('boxplot.png')  # Corrected safefig to savefig

avg_temp = sum(temp) / len(temp)
low_temp = min(temp)
high_temp = max(temp)
print('Weather Statistics')
print('The average temperature was: ', avg_temp)
print('The lowest temperature was: ', low_temp)
print('The highest temperature was: ', high_temp)
