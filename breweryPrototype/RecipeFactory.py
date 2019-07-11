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
        for recepie in userData['recipes']:
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
            yeastType = recepie['yeast']['yeastType']
            yeastAmount = recepie['yeast']['amount']
            customAttenuation = recepie['yeast']['customAttenuation']
            yeast = RecipeModels.Yeast(yeastType, yeastAmount, customAttenuation)
            primMethod = recepie['primeInfo']['method']
            primAmount = recepie['primeInfo']['amount']
            primTemp = recepie['primeInfo']['temp']
            primCo2Level = recepie['primeInfo']['co2Level']
            primInf = RecipeModels.PrimingInfo(primMethod, primAmount, primTemp, primCo2Level)
            hops = []
            #other = Other()
            other = ''
            sWca2 = recepie['waterChem']['sourceWater']['ca2']
            sWmg2 = recepie['waterChem']['sourceWater']['mg2']
            sWna2 = recepie['waterChem']['sourceWater']['na']
            sWcl = recepie['waterChem']['sourceWater']['cl']
            sWso42 = recepie['waterChem']['sourceWater']['so42']
            sWhco3 = recepie['waterChem']['sourceWater']['hco3']
            sourceWater = RecipeModels.Sourcewater(sWca2, sWmg2, sWna2, sWcl, sWso42, sWhco3)
            tWca2 = recepie['waterChem']['targetWater']['ca2']
            tWmg2 = recepie['waterChem']['targetWater']['mg2']
            tWna2 = recepie['waterChem']['targetWater']['na']
            tWcl = recepie['waterChem']['targetWater']['cl']
            tWso42 = recepie['waterChem']['targetWater']['so42']
            tWhco3 = recepie['waterChem']['targetWater']['hco3']
            targetWater = RecipeModels.Targetwater(tWca2, tWmg2, tWna2, tWcl, tWso42, tWhco3)
            calciumChloride = recepie['waterChem']['minerals']['calciumChloride']
            chalk = recepie['waterChem']['minerals']['chalk']
            epsomSalt = recepie['waterChem']['minerals']['epsomSalt']
            gypsum = recepie['waterChem']['minerals']['gypsum']
            magnesiumChloride = recepie['waterChem']['minerals']['magnesiumChloride']
            bakingSoda = recepie['waterChem']['minerals']['bakingSoda']
            citricAcid = recepie['waterChem']['minerals']['citricAcid']
            lacticAcid = recepie['waterChem']['minerals']['lacticAcid']
            minerals = RecipeModels.Minerals(calciumChloride, chalk, epsomSalt, gypsum, magnesiumChloride, bakingSoda, citricAcid, lacticAcid)
            watChem = RecipeModels.WaterChemistry(sourceWater, targetWater, minerals)
            boilTime = recepie['boilTime']
            efficiency = recepie['efficiency']
            batchSize = recepie['batchSize']
            currentRecepie = RecipeModels.Recipe(title, description, og, fg, yeast, primInf, watChem, boilTime, efficiency, batchSize, mashG, other, hops, fer)
            for hopItem in recepie['hops']:
                hopAA = hopItem['AA']
                hopType = hopItem['hopType']
                hopBoilTime = hopItem['boilTime']
                hopAmount = hopItem['amount']
                hopWholeLeaf = hopItem['leafWhole']
                hopTemp = hopItem['temp']
                hopObject = RecipeModels.Hop(hopType, hopBoilTime, hopAmount, hopWholeLeaf, hopTemp, hopAA)
                currentRecepie.addHop(hopObject)
            for fermentable in recepie['fermentables']:
                ferType = fermentable['ferType']
                ferKg = fermentable['kg']
                ferLovibond = fermentable['lovibond']
                fermentableObject = RecipeModels.Fermentable(ferType, ferKg, ferLovibond)
                currentRecepie.addFerm(fermentableObject)
            user.addRecipe(currentRecepie)
        
        return user
    #convert userObject (the Sser class object) to a dictionary, so that it can be written into the json file.
    @staticmethod
    def SaveUser(userObject):
        userData = userObject.__dict__
        userData['recipes'] = [recepie.__dict__ for recepie in userData['recipes']]
        for recepie in userData['recipes']:
            print(recepie)
            recepie['fermentables'] = [fermentable.__dict__ for fermentable in recepie['fermentables']]
            recepie['yeast'] = recepie['yeast'].__dict__
            recepie['primeInfo'] = recepie['primeInfo'].__dict__
            recepie['hops'] = [hop.__dict__ for hop in recepie['hops']]
            recepie['waterChem'] = recepie['waterChem'].__dict__
            recepie['waterChem']['sourceWater'] = recepie['waterChem']['sourceWater'].__dict__
            recepie['waterChem']['targetWater'] = recepie['waterChem']['targetWater'].__dict__
            recepie['waterChem']['minerals'] = recepie['waterChem']['minerals'].__dict__
            recepie['mashGuide'] = recepie['mashGuide'].__dict__
            #TODO if we add other class, add here
        writeJsonData(userData)

    #Create a "default" recipe.
    @staticmethod
    def createEmptyRecipe():
        emptyRecipe = RecipeModels.Recipe()
        emptyRecipe.hops.append(RecipeModels.Hop())
        emptyRecipe.fermentables.append(RecipeModels.Fermentable())
        emptyRecipe.mashGuide = RecipeModels.MashGuideline()
        emptyRecipe.primeInfo = RecipeModels.PrimingInfo()
        emptyRecipe.waterChem = RecipeModels.WaterChemistry(RecipeModels.Sourcewater(), RecipeModels.Targetwater(), RecipeModels.Minerals())
        emptyRecipe.yeast = RecipeModels.Yeast()
        return emptyRecipe



# newRecipe = RecepieFactory.createEmptyRecipe()
# print(newRecipe.mashGuide.temp)
#printjsonFile()
#user = RecepieFactory.createUser()
#print(user.recipes[0].waterChem.targetWater.ca2)
# print(len(user.recipes))
#RecepieFactory.SaveUser(user)



            
