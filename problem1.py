# Simulating OS's disk scheduling algorithms. Containing:
# FCFS, SSTF, Scan, C-Scan, Look, C-Look


def add_distance(origin, destination):
    return abs(origin-destination)


def fcfs(current):
    total = 0
    for r in requests:
        total += add_distance(current, r)
        current = r
    return total


def sstf(current):
    total = 0
    requests.append(current)
    requests.sort()
    index = requests.index(current)
    # turn if to while and check boundaries (end and begin)
    while len(requests) > 1:   
        #fetch distances
        if index != len(requests) - 1:
            upper = abs(requests[index+1] - requests[index])
        else:
            upper = maximum + 1
        if index != 0:
            lower = abs(requests[index-1] - requests[index])
        else:
            lower = maximum + 1
        #move head
        if upper > lower:
            total += lower
            current = requests[index-1]
            index -= 1
            requests.pop(index + 1)
        else:
            total += upper
            current = requests[index+1]
            requests.pop(index)
    return total


def scan(direction):
    total = 0
    requests.append(current)
    requests.sort()
    index = requests.index(current)
    #Headed to Right
    while len(requests) > 1:
        if direction:
            if index == len(requests) - 1:
                direction = 0
                continue
            total += add_distance(requests[index], requests[index+1])
            requests.pop(index)
        #Headed to Left
        else:
            if index == 0:
                direction = 1
                continue
            total += add_distance(requests[index-1], requests[index])
            requests.pop(index)
            index -= 1
    return total


def cscan(direction):
    total = 0
    requests.append(current)
    requests.sort()
    index = requests.index(current)
    #Headed to Right
    while len(requests) > 1:
        if direction:
            if index == len(requests) - 1:
                total += add_distance(requests[index], maximum)
                index = 0
                requests.pop(len(requests)-1)
                total += add_distance(minimum, requests[index])
                continue
            total += add_distance(requests[index], requests[index+1])
            requests.pop(index)
        #Headed to Left
        else:
            if index == 0:
                total += add_distance(requests[index], minimum)
                requests.pop(0)
                index = len(requests) - 1
                total += add_distance(maximum, requests[index])
                continue
            total += add_distance(requests[index-1], requests[index])
            requests.pop(index)
            index -= 1
    return total


def look(direction):
    total = 0
    requests.append(current)
    requests.sort()
    index = requests.index(current)
    #Headed to Right
    while len(requests) > 1:
        if direction:
            if index == len(requests) - 1:
                index = 0
                continue
            total += add_distance(requests[index], requests[index+1])
            requests.pop(index)
        #Headed to Left
        else:
            if index == 0:
                index = len(requests) - 1
                continue
            total += add_distance(requests[index-1], requests[index])
            requests.pop(index)
            index -= 1
    return total


def clook(direction):
    total = 0
    requests.append(current)
    requests.sort()
    index = requests.index(current)
    #Headed to Right
    while len(requests) > 1:
        if direction:
            if index == len(requests) - 1:
                requests.pop(index)
                index = 0
                continue
            total += add_distance(requests[index], requests[index+1])
            requests.pop(index)
        #Headed to Left
        else:
            if index == 0:
                requests.pop(0)
                index = len(requests)-1
                continue
            total += add_distance(requests[index-1], requests[index])
            requests.pop(index)
            index -= 1
    return total


movement = 0
requests = []
f = open("requests.txt", "r")
for line in f:
        requests.append(int(line))

right_direction = False
minimum = 0
maximum = 4999
a = int(input("Insert a number between 1 - 6:"))
current = int(input("Enter current sector:"))
if a == 1:
    movement = fcfs(current)
elif a == 2:
    movement = sstf(current)
elif a == 3:
    movement = scan(right_direction)
elif a == 4:
    movement = cscan(right_direction)
elif a == 5:
    movement = look(right_direction)
elif a == 6:
    movement = clook(right_direction)
f.close()
print(movement)
