#!python3
#Creating recepies from memory
import os, json, pprint, recepieModels
def loadData():
    jsonFile = open('userData.json', 'r')
    try:
        data = json.load(jsonFile)
        jsonFile.close()
    except ValueError:
        data = {}
    return data

def printjsonFile():
    userData = loadData()
    pprint.pprint(userData)
class RecepieFactory:
    #This method will return a user class with all the recepies saved into
    #memory, also name and img.
    @staticmethod
    def createUser():
        userData = loadData()
        recepies = []
        user = recepieModels.User(userData['name'], userData['img'], recepies)
        #json file. go throught each recepie and retrive data, add to user
        #recepie list.
        for recepie in userData['recepies']:
            title = recepie['title']
            description = recepie['description']
            og = recepie['og']
            fg = recepie['fg']
            fer = []
            for fermentable in recepie['fermentables']:
                ferType = fermentable['type']
                ferKg = fermentable['kg']
                ferLovibond = fermentable['lovibond']
                fermentableObject = recepieModels.Fermentable(ferType, ferKg, ferLovibond)
                fer.append(fermentableObject)

            startThick = recepie['mashGuide']['startThick']
            mashTemp = recepie['mashGuide']['temp']
            mashTime = recepie['mashGuide']['time']
            mashAmount = recepie['mashGuide']['amount'] 
            mashG = recepieModels.MashGuideline(startThick, mashTemp, mashTime, mashAmount)
            yeast = recepieModels.Yeast()
            primMethod = recepie['primeInfo']['method']
            primAmount = recepie['primeInfo']['amount']
            primTemp = recepie['primeInfo']['temp']
            primCo2Level = recepie['primeInfo']['co2Level']
            primInf = recepieModels.PrimingInfo(primMethod, primAmount, primTemp, primCo2Level)
            hops = []
            for hopItem in recepie['hops']:
                hopType = hopItem['type']
                hopBoilTime = hopItem['boilTime']
                hopAmount = hopItem['amount']
                hopWholeLeaf = hopItem['leafWhole']
                hopTemp = hopItem['temp']
                hopObject = recepieModels.Hop(hopType, hopBoilTime, hopAmount, hopWholeLeaf, hopTemp)
                hops.append(hopObject)
            #other = Other()
            other = ''
            sourceWater = recepie['waterChem']['sourceWater']
            targetWater = recepie['waterChem']['targetWater']
            ca2 = recepie['waterChem']['ca2']
            mg2 = recepie['waterChem']['mg2']
            na2 = recepie['waterChem']['na2']
            cl = recepie['waterChem']['cl']
            so42 = recepie['waterChem']['so42']
            hco3 = recepie['waterChem']['hco3']
            watChem = recepieModels.WaterChemistry(sourceWater, targetWater, ca2, mg2, na2, cl, so42, hco3)
            boilTime = recepie['boilTime']
            efficiency = recepie['efficiency']
            batchSize = recepie['batchSize']
            user.addRecepie(title, description, og, fg, fer,
                   mashG, yeast, primInf, hops, other,
                   watChem, boilTime, efficiency, batchSize)
        
        return user

printjsonFile()
user = RecepieFactory.createUser()
print(user)



            
