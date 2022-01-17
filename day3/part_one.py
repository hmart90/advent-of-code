FILENAME = './day3/data/input'

number_list = []

with open(FILENAME) as file:
    for line in file:
        number_list.append([int(x) for x in list(line.strip())])

n = len(number_list[0])
total = len(number_list)

gamma = ''
epsilon = ''

for i in range(n):
    if sum([ x[i] for x in number_list]) > total/2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print('results: ')
print(gamma * epsilon)