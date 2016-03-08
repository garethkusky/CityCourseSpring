import random

for i in range(10):
    print(' '.join([str(random.randint(1, 59)) for x in range(6)]).lstrip())
print('0')
