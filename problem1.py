#Code available at https://github.com/mayazdi/OS-disk-Scheduling
# Simulating OS's disk scheduling algorithms. Containing:
# FCFS, SSTF, Scan, C-Scan, Look, C-Look
import sys
import logging


def add_distance(origin, destination):
    return abs(origin-destination)


def fcfs(current, req):
    total = 0
    for r in req:
        total += add_distance(current, r)
        current = r
    return total


def sstf(current, req):
    total = 0
    req.append(current)
    req.sort()
    index = req.index(current)
    # turn if to while and check boundaries (end and begin)
    while len(req) > 1:
        #fetch distances
        if index != len(req) - 1:
            upper = abs(req[index+1] - req[index])
        else:
            upper = maximum + 1
        if index != 0:
            lower = abs(req[index-1] - req[index])
        else:
            lower = maximum + 1
        #move head
        if upper > lower:
            total += lower
            current = req[index-1]
            index -= 1
            req.pop(index + 1)
        else:
            total += upper
            current = req[index+1]
            req.pop(index)
    return total


def scan(direction, req):
    total = 0
    req.append(current)
    req.sort()
    index = req.index(current)
    #Headed to Right
    while len(req) > 1:
        if direction:
            if index == len(req) - 1:
                total += 2*add_distance(req[index], maximum)
                direction = 0
                continue
            total += add_distance(req[index], req[index+1])
            req.pop(index)
        #Headed to Left
        else:
            if index == 0:
                total += 2*add_distance(req[0], minimum)
                direction = 1
                continue
            total += add_distance(req[index-1], req[index])
            req.pop(index)
            index -= 1
    return total


def cscan(direction, req):
    total = 0
    req.append(current)
    req.sort()
    index = req.index(current)
    #Headed to Right
    while len(req) > 1:
        if direction:
            if index == len(req) - 1:
                total += add_distance(req[index], maximum)
                index = 0
                req.pop(len(req)-1)
                total += add_distance(minimum, req[index])
                continue
            total += add_distance(req[index], req[index+1])
            req.pop(index)
        #Headed to Left
        else:
            if index == 0:
                total += add_distance(req[index], minimum)
                req.pop(0)
                index = len(req) - 1
                total += add_distance(maximum, req[index])
                continue
            total += add_distance(req[index-1], req[index])
            req.pop(index)
            index -= 1
    return total


def look(direction, req):
    total = 0
    req.append(current)
    req.sort()
    index = req.index(current)
    #Headed to Right
    while len(req) > 1:
        if direction:
            if index == len(req) - 1:
                index = 0
                continue
            total += add_distance(req[index], req[index+1])
            req.pop(index)
        #Headed to Left
        else:
            if index == 0:
                index = len(req) - 1
                continue
            total += add_distance(req[index-1], req[index])
            req.pop(index)
            index -= 1
    return total


def clook(direction, req):
    total = 0
    req.append(current)
    req.sort()
    index = req.index(current)
    #Headed to Right
    while len(req) > 1:
        if direction:
            if index == len(req) - 1:
                req.pop(index)
                index = 0
                continue
            total += add_distance(req[index], req[index+1])
            req.pop(index)
        #Headed to Left
        else:
            if index == 0:
                req.pop(0)
                index = len(req)-1
                continue
            total += add_distance(req[index-1], req[index])
            req.pop(index)
            index -= 1
    return total


movement = 0
requests = []
f = open("requests.txt", "r")
for line in f:
    requests.append(int(line))
right_direction = True
minimum = 0
maximum = 4999
# Program only works when one argument is passed in range(min, max)
if len(sys.argv) != 2:
    logging.error("Enter one valid number as initial head position")
    sys.exit(1)
else:
    try:
        current = int(sys.argv[1])
        if not minimum < current < maximum:
            logging.error("Number is not in range(" +
                          str(minimum) + ", " + str(maximum) + ")")
            sys.exit(2)
    except Exception:
        logging.error("Enter one valid number as initial head position")
        sys.exit(3)

print('FCFS: ' + str(fcfs(current, requests.copy())), end='\n')
print('SSTF: ' + str(sstf(current, requests.copy())), end='\n')
print('SCAN: ' + str(scan(right_direction, requests.copy())), end='\n')
print('CSCN: ' + str(cscan(right_direction, requests.copy())), end='\n')
print('LOOK: ' + str(look(right_direction, requests.copy())), end='\n')
print('CLOK: ' + str(clook(right_direction, requests.copy())), end='\n')
f.close()
