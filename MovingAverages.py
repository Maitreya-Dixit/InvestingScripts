from cProfile import label
import csv
import matplotlib.pyplot as plt
import numpy as np

dataFileName = input("Enter file name: ")

dataFile = open(dataFileName)
csvreader = csv.reader(dataFile)

header = []
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

adjCloseData = []
for row in rows:
    adjCloseData.append(row[5])

k = 1
x_data = []
for row in adjCloseData:
    x_data.append(k)
    k += 1

adjCloseDataInt = []

for row in adjCloseData:
    adjCloseDataInt.append(float(row))

window_size = 10
moving_average_fma = []
i = 0

j = 0
while j <= window_size-2:
    moving_average_fma.append(None)
    j += 1

while i < len(adjCloseDataInt) - window_size + 1:
    window = adjCloseDataInt[i : i + window_size]
    window_average = round(sum(window) / window_size, 6)
    moving_average_fma.append(window_average)
    i += 1

window_size = 40
moving_average_sma = []
i = 0

j = 0
while j <= window_size-2:
    moving_average_sma.append(None)
    j += 1

while i < len(adjCloseDataInt) - window_size + 1:
    window = adjCloseDataInt[i : i + window_size]
    window_average = round(sum(window) / window_size, 6)
    moving_average_sma.append(window_average)
    i += 1

x = np.array(x_data)
y1 = np.array(moving_average_fma)
y2 = np.array(moving_average_sma)

plt.plot(x, y1, label = "FMA")
plt.plot(x, y2, label = "SMA")
plt.legend()
plt.show()

dataFile.close
