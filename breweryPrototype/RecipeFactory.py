#!python3
#Creating recepies from memory
import os, json, pprint, RecipeModels
def loadData():
    jsonFile = open('userData.json', 'r')
    try:
        data = json.load(jsonFile)
        jsonFile.close()
    except ValueError:
        data = {}
    return data

def writeJsonData(data):
    jsonFile = open('userData.json', 'w')
    json.dump(data, jsonFile)
    jsonFile.close()

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
        user = RecipeModels.User(userData['name'], userData['img'], recepies)
        #json file. go throught each recepie and retrive data, add to user
        #recepie list.
        for recepie in userData['recepies']:
            title = recepie['title']
            description = recepie['description']
            og = recepie['og']
            fg = recepie['fg']
            fer = []
            startThick = recepie['mashGuide']['startThick']
            mashTemp = recepie['mashGuide']['temp']
            mashTime = recepie['mashGuide']['time']
            mashAmount = recepie['mashGuide']['amount'] 
            mashG = RecipeModels.MashGuideline(startThick, mashTemp, mashTime, mashAmount)
            yeast = RecipeModels.Yeast()
            primMethod = recepie['primeInfo']['method']
            primAmount = recepie['primeInfo']['amount']
            primTemp = recepie['primeInfo']['temp']
            primCo2Level = recepie['primeInfo']['co2Level']
            primInf = RecipeModels.PrimingInfo(primMethod, primAmount, primTemp, primCo2Level)
            hops = []
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
            watChem = RecipeModels.WaterChemistry(sourceWater, targetWater, ca2, mg2, na2, cl, so42, hco3)
            boilTime = recepie['boilTime']
            efficiency = recepie['efficiency']
            batchSize = recepie['batchSize']
            currentRecepie = RecipeModels.Recepie(title, description, og, fg, yeast, primInf, watChem, boilTime, efficiency, batchSize, mashG, other, hops, fer)
            for hopItem in recepie['hops']:
                hopType = hopItem['hopType']
                hopBoilTime = hopItem['boilTime']
                hopAmount = hopItem['amount']
                hopWholeLeaf = hopItem['leafWhole']
                hopTemp = hopItem['temp']
                hopObject = RecipeModels.Hop(hopType, hopBoilTime, hopAmount, hopWholeLeaf, hopTemp)
                currentRecepie.addHop(hopObject)
            for fermentable in recepie['fermentables']:
                ferType = fermentable['ferType']
                ferKg = fermentable['kg']
                ferLovibond = fermentable['lovibond']
                fermentableObject = RecipeModels.Fermentable(ferType, ferKg, ferLovibond)
                currentRecepie.addFerm(fermentableObject)
            user.addRecepie(currentRecepie)
        
        return user
    #convert userObject (the Sser class object) to a dictionary, so that it can be written into the json file.
    @staticmethod
    def SaveUser(userObject):
        userData = userObject.__dict__
        userData['recepies'] = [recepie.__dict__ for recepie in userData['recepies']]
        for recepie in userData['recepies']:
            recepie['fermentables'] = [fermentable.__dict__ for fermentable in recepie['fermentables']]
            recepie['yeast'] = recepie['yeast'].__dict__
            recepie['primeInfo'] = recepie['primeInfo'].__dict__
            recepie['hops'] = [hop.__dict__ for hop in recepie['hops']]
            recepie['waterChem'] = recepie['waterChem'].__dict__
            recepie['mashGuide'] = recepie['mashGuide'].__dict__
            #TODO if we add other class, add here
        print(userData)
        #writeJsonData(userData)


printjsonFile()
user = RecepieFactory.createUser()
print(user.recepies[0].hops[0].hopType)
RecepieFactory.SaveUser(user)



            
