import os
import re
from os import listdir
from os.path import isfile, join

### === Path to the Aura folder === ###
path="d:/salesforce/Org/aura"
dirs = os.listdir(path)


countFolder = 0
countFile = 0
#accepted_extensions=["js", "cmp", "app", "evt", "css", "svg", "auradoc", "design"]
accepted_extensions=["js", "cmp", "app", "evt"]
jsonString = "["

for file in dirs:
    countFolder=countFolder+1
    for fileName in os.listdir(path=path+'/'+file):
        if fileName.split(".")[-1] in accepted_extensions:			
            jsonString = jsonString+"{"+"\"fileName\":\""+fileName+"\","

            textfile = open(path+'/'+file+'/'+fileName, 'r')
            filetext = textfile.read()
            textfile.close()

            ### === Finding component markup dependencies
            cmpMatches = re.findall("(<c:\w+)", filetext)

            ### === Finding event markup dependencies
            evtMatches = re.findall("(c:\w+)", filetext)

            ### === START : EVENT MATCHING FOR JSON ===### 
            if(len(evtMatches) > 0):
                jsonString = jsonString + "\"event\": ["
                evtStr = "" 
                for matchEvt in evtMatches:
                    evtStr = evtStr + "\"" + matchEvt.split(":")[1]+"\","
                jsonString = jsonString + evtStr.rstrip(",") + "],"
            ### === END : EVENT MATCHING FOR JSON ===### 
            ### === START : COMPONENT MATCHING FOR JSON ===###
            if(len(cmpMatches) > 0):
                jsonString=jsonString+"\"component\" : ["
                cmpStr = ""
                for matchCmp in cmpMatches:
                    cmpStr = cmpStr + "\"" + matchCmp.split(":")[1] + "\","
                    #print(matchedFile.split(":")[1])
                jsonString = jsonString + cmpStr.rstrip(",") + "],"
            ### === END : COMPONENT MATCHING FOR JSON ===###

            countFile=countFile+1
            extension = fileName.split(".")[-1]
            if(extension == "cmp"):
                jsonString+="\"type\" : \"Component\"},"
            if(extension == "js"):
                jsonString+="\"type\" : \"JavaScript\"},"
            if(extension == "evt"):
                jsonString+="\"type\" : \"Event\"},"
            if(extension == "app"):
                jsonString+="\"type\" : \"Application\"},"
    #print(file)

print("====Final count===\n");
print( "Folder:" , countFolder)
print("Files:", countFile)

jsonString = jsonString.rstrip(",")
jsonString = jsonString + "]"

print("Completed prcessing. Writing to the JSON file..")
fJson = open("final_json.json", "w")
fJson.write(jsonString)
fJson.close()
print("Successfully wrote JSON.")
