# Simulating OS's disk scheduling algorithms. Containing:
# FCFS, SSTF, Scan, C-Scan, Look, C-Look


def add_distance(origin, destination):
    return abs(origin-destination)
    


def fcfs(current):
    sum = 0
    for r in requests:
        sum += add_distance(current, r)
        current = r
    return sum


def sstf(current):
    sum = 0
    requests.append(current)
    requests.sort()
    index = requests.index(current)
    # turn if to while and check boundaries (end and begin)
    if len(requests) > index > 0:
        upper = abs(requests[index+1] - requests[index])
        lower = abs(requests[index-1] - requests[index])
        if upper > lower:
            sum += lower
            current += requests[index-1]
            requests.pop(index)
        else:
            sum += upper
            current += requests[index+1]

        requests.pop(index)
    return sum


def scan(direction):
    sum = 0
    requests.append(current)
    requests.sort()
    index = requests.index(current)
    # check if it is not at the end (both right and left)
    #Headed to Right
    while len(requests) > 1:
        if direction:
            if index == len(requests) - 1:
                direction = 0
                continue
            sum += add_distance(requests[index], requests[index+1])
            requests.pop(index)
        #Headed to Left
        else:
            if index == 0:
                direction = 1
                continue
            sum += add_distance(requests[index-1], requests[index])
            requests.pop(index)
            index -= 1
    return sum


def cscan():
    pass


def look():
    pass


def clook():
    pass


requests = []
f = open("requests.txt", "r")
for line in f:
        requests.append(int(line))

right_direction = True
a = int(input("Insert a number between 1 - 6:"))
current = int(input("Enter current sector:"))
if a == 1:
    fcfs(current)
elif a == 2:
    sstf(current)
elif a == 3:
    scan(right_direction)
elif a == 4:
    cscan()
elif a == 5:
    look()
elif a == 6:
    clook()
f.close()
print(sum)
