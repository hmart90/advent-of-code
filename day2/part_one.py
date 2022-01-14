FILENAME = './day2/data/input'

forward_list = []
up_list = []
down_list = []

with open(FILENAME) as file:
    for line in file:
        direction, value = line.strip().split(' ')
        value = int(value)
        if direction == 'forward':
            forward_list.append(value)
        elif direction == 'up':
            up_list.append(value)
        elif direction == 'down':
            down_list.append(value)

print(f'forward_list: {forward_list}')
print(f'up_list: {up_list}')
print(f'down_list: {down_list}')

x = sum(forward_list)
z = sum(down_list) - sum(up_list)

results = x * z

print(f'results : {results}')