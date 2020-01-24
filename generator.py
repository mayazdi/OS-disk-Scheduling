# Code available at https://github.com/mayazdi/OS-disk-Scheduling
# Generate 1000 random numbers
# Note that some numbers might be indentical
from random import randrange

f = open("requests.txt", "w")
for i in range(999):
    f.write(str(randrange(4999)) + "\n")
f.write(str(randrange(4999)))
f.close()
