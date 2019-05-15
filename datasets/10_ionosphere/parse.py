def merge(list_of_lists):
    merged_list = []

    for list in list_of_lists:
        for item in list:
            merged_list.append(item)

    return merged_list


dataSet = open("ionosphere.data", "r")

ctrlSamples = []
testSamples = []
classes = []

index = 0

for line in dataSet:
    line = line.rstrip("\n")
    attributes = line.split(',')

    if index % 4 == 0:
        del attributes[-1]
        testSamples.append(attributes)
    else:
        if attributes[-1] == "g":
            classes.append(0)
        else:
            classes.append(1)

        del attributes[-1]
        ctrlSamples.append(attributes)

    index = index + 1

dataSet.close()

ctrl = len(ctrlSamples)
test = len(testSamples)

ctrlSamples = [float(i) for i in merge(ctrlSamples)]
testSamples = [float(i) for i in merge(testSamples)]
classes = [int(i) for i in classes]

text = open("ionosphere.parse", "w")

for item in merge([ctrlSamples, testSamples, classes]):
    text.write(str(item) + '\n')

text.close()

config = open("ionosphere.cfg", "w")

config.write(str(ctrl) + " # ctrl samples\n")
config.write(str(test) + " # test samples\n")
config.write("34 # features\n")
config.write("2 # classes\n")

config.close()
