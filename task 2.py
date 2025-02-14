from math import trunc

print("Park Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")


def secToMin(seconds):
    a = trunc((seconds / 60))
    b = round((seconds % 60))
    if a < 2:
        c = str(a) + " minute, " + str(b) + " seconds"
    else:
        c = str(a) + " minutes, " + str(b) + " seconds"
    return c


totalRunners = 0
totalTime = 0
fastest = 1000
slowest = 0
while 1:
    a = input("enter runner id followed by : then their time type END to finish submitting> ")
    if a[0] == ':' or a[-1] == ":":
        print("Error in data stream. Ignoring. Carry on.")
    elif a == "END":
        break
    else:
        totalRunners = totalRunners + 1
        b = a.split(':')
        if int(b[1]) < fastest:
            fastest = int(b[1])
            fastestRunner = b[0]
        if int(b[1]) > slowest:
            slowest = int(b[1])
        totalTime = totalTime + int(b[1])

print("\nTotal Runners: ", totalRunners)
print("Average Time: ", secToMin(totalTime / totalRunners))
print("Fastest Time: ", secToMin(fastest))
print("Slowest Time: ", secToMin(slowest))
print("\nBest Time Here: Runner #", fastestRunner)
