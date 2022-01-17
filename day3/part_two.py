FILENAME = './day3/data/input'

number_list = []

with open(FILENAME) as file:
    for line in file:
        number_list.append([int(x) for x in list(line.strip())])

total = len(number_list)

ogr = ''
co2s = ''

current_list = number_list

for i in range(len(number_list[0])):
    if sum([ x[i] for x in current_list]) >= len(current_list)/2:
        ogr += '1'
    else:
        ogr += '0'
    new_list = []
    for x in current_list:
        x_start = ''.join([str(y) for y in x[:i + 1]])
        if x_start == ogr:
            new_list.append(x)

    if len(new_list) == 1:
        ogr = ''.join([str(y) for y in new_list[0]])
        break
    current_list = new_list
ogr = int(ogr, 2)

current_list = number_list

for i in range(len(number_list[0])):
    if sum([ x[i] for x in current_list]) >= len(current_list)/2:
        co2s += '0'
    else:
        co2s += '1'
    new_list = []
    for x in current_list:
        x_start = ''.join([str(y) for y in x[:i + 1]])
        if x_start == co2s:
            new_list.append(x)

    if len(new_list) == 1:
        co2s = ''.join([str(y) for y in new_list[0]])
        break
    current_list = new_list

co2s = int(co2s, 2)


print('results: ')
print(ogr * co2s)