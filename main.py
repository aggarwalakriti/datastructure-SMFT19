def getMaxInterval(file):
    inputFile = open(file, "r")
    lines = inputFile.readlines()

    timeIntervals = []

    for line in lines[1:]:
        intervalSplit = line.split(' ')
        timeIntervals.append([int(intervalSplit[0]), int(intervalSplit[1])])
#using lambda function for sorting out time.
    timeIntervals.sort(key=lambda x: (x[0], x[1]))

    maxVal = 0
    for i in range(0, len(timeIntervals)):
        intervals = [times for times in timeIntervals]

        # Remove one guard and calculate the total shift, then take the maximum.
        intervals.pop(i)

        lastVal = 0
        for interval in intervals:
            if interval[0] > intervals[lastVal][1]:
                lastVal += 1
                intervals[lastVal] = interval
            else:
                intervals[lastVal] = (intervals[lastVal][0], interval[1])

        overlap = [overlap[1] - overlap[0] for overlap in
                             intervals[:lastVal + 1]]

        maxVal = max(sum(overlap), maxVal)

    # Write the maximum value in the file
    outputFile = file.replace('.in', '.out')
    fw = open(outputFile, "w")
    fw.write(str(maxVal))
    fw.close()


for i in range(1, 11):
    getMaxInterval(str(i) + '.in')







