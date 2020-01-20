# Simulating OS's disk scheduling algorithms. Containing:
# FCFS, SSTF, Scan, C-Scan, Look, C-Look


def add_distance(destination):
    sum += abs(current-destination)
    return destination


def fcfs():
    for i in requests:
        current = add_distance(i)


def sstf():
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
            requests.pop(index=index)
        else:
            sum += upper
            current += requests[index+1]

        requests.pop(index=index)


def scan():
    requests.append(current)
    requests.sort()
    index = requests.index(current)
    # check if it is not at the end (both right and left)
    #turn if to while
    if right_direction:
        add_distance(requests[index+1])
        requests.pop(index=index)
        index += 1
    #indent into , check boundaries
    if index == len(requests) - 1:
        right_direction = False
        add_distance(requests[index-1])



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
sum = 0
right_direction = True
a = input("Insert a number between 1 - 6:")
current = input("Enter current sector:")

if a == '1':
    fcfs()
elif a == '2':
    sstf()
elif a == '3':
    scan()
elif a == '4':
    cscan()
elif a == '5':
    look()
elif a == '6':
    clook()

f.close()
