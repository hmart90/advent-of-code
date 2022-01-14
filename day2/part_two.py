FILENAME = './day2/data/input'

x = 0
z = 0
a = 0

with open(FILENAME) as file:
    for line in file:
        direction, value = line.strip().split(' ')
        value = int(value)
        print(line.strip())
        if direction == 'forward':
            x += value
            z += a * value
        elif direction == 'up':
            a -= value
        elif direction == 'down':
            a += value
        print(f'x: {x} z: {z} a: {a}')

results = x * z

print(f'results : {results}')