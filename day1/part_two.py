FILENAME = './day1/data/input'

measurements = []

with open(FILENAME) as file:
    for line in file:
        measurements.append(int(line.strip()))

s = 0

for i in range(3, len(measurements)):
    if measurements[i] + measurements[i - 1] + measurements[i - 2] > measurements[i - 1] + measurements[i - 2] + measurements[i - 3]:
        s = s + 1

print(s)
