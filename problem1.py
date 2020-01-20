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
    pass


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
