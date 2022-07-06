import csv
from functools import reduce
import json

#get police data
def getPoliceCalls():
    global calldata
    calls= []

    with open ('policecalls.csv') as calllog:
        reader = csv.reader(calllog)
        first_row = True
    
    #handle headers
    header = []

    for row in reader:
        if first_row: 
            header = row
            first_row = False

        else:
            calldata = {}
            for i in range(len(header)):
                calldata[header[i]] = row[i]
                calls.append(calldata)

    return calldata
#remove empties in zip amd neuhgbirhood
def filtercalls():
    global calldata
    #neighborhood
    calldata = list(filter(lambda row: row['neighbirhood'] != None, calldata))
    calldata = list(filter(lambda row: row['neighborhood'] != 0, calldata))
    calldata = list(filter(lambda row: row['neighborhood'] != '', calldata))
    #zip
    calldata = list(filter(lambda row: row['zip_code'] != None, calldata))
    calldata = list(filter(lambda row: row['zip_code'] != 0, calldata))
    calldata = list(filter(lambda row: row['zip_code'] != '', calldata))

#calculate avg response, dispatch, and total times
def callstats():
    global calldata
    #response time
    totalresponse = reduce(lambda x, y: x + float(y["totalresponsetime"]), calldata, 0)
    avgresponse = totalresponse/len(calldata)
    print(avgresponse)
    #dispatch time
    totaldispatch = reduce(lambda x, y: x + float(y["dipatchtime"]), calldata, 0)
    avgdispatch = totaldispatch/len(calldata)
    print(avgdispatch)
    #total time
    totaltime = reduce(lambda x, y: x + float(y["totaltime"]), calldata, 0)
    avgtotaltime = totaltime/len(calldata)
    print(avgtotaltime)


# and here I am confused
def neighborhoodstats():
    global calldata
    global nieghborhooddata
