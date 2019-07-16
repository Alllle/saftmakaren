#!python3
#Classes related to recipe.

import RecipeFactory

class User:
    def __init__(self, name = None, img = None, recipes = None):
        if name == None:
            self.name = 'insert name'
        else:
            self.name = name
        if img == None:
            self.img = ''
        else:
            self.img = img
        if recipes == None:
            self.recipes = []
        else:
            self.recipes = recipes


    def addRecipe(self, recipe):
        self.recipes.append(recipe)

    #TODO remove recipe based off of recipe ID, and reduce recipeCount and adjust recipe count for those recipes with higher nr, ej testad.
    def removeRecipe(self, recipeID):
        #hittar vilket recept som har samma id som input och tar bort den från listan.
        for index, recipe in enumerate(self.recipes):
            if recipe.recipeID == recipeID:
                del self.recipes[index]
        #tar alla recept från och med id input och minskar deras id med 1, så att ingen lucka finns efter man tagit bort ett recept
        for recipe in range((recipeID - 1), len(self.recipes)):
            self.recipes[recipe].recipeID -= 1
        Recipe.recipeCount -= 1

    def SaveUser(self):
        userData = self.__dict__
        print('line 38 ' + str(type(self.recipes[0])))
        userData['recipes'] = [recepie.__dict__ for recepie in userData['recipes']] # at this lines self.recipes[0] becomes a dict
        print('line 40 ' + str(type(self.recipes[0])))
        for recepie in userData['recipes']:
            #print(recepie)
            print(type(self.recipes[0]))
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
        print(type(self.recipes[0]))
        RecipeFactory.writeJsonData(userData)
        
        
        
class Recipe:
    recipeCount = 1
    def __init__(self, title = '', description = '', og = 0, fg = 0, yeast = None, primeInfo = None, waterChem = None, boilTime = 0,
                 efficiency = 0, batchSize = 0, mashGuide = None, other = None, hops = None, fermentables = None):
        self.title = title
        self.description = description
        self.og = float(og)
        self.fg = float(fg)
        self.yeast = yeast
        self.primeInfo = primeInfo
        self.waterChem = waterChem
        self.boilTime = float(boilTime)
        self.efficiency = float(efficiency)
        self.batchSize = float(batchSize)
        self.mashGuide = mashGuide
        self.other = other
        if hops == None:
            self.hops = []
        else:
            self.hops = hops
        if fermentables == None:
            self.fermentables = []
        else:
            self.fermentables = fermentables
        self.recipeID = Recipe.recipeCount
        Recipe.recipeCount += 1
            
    @property 
    def ABV(self):
        return abs((self.fg - self.og) * 131.25)
    
    @property 
    def IBU(self):
        tempIBU = 0
        for hopObj in self.hops:
            addedAA = ((hopObj.AA * hopObj.amount * 1000)/self.batchSize)
            tempIBU += addedAA * hopObj.GetAAUtil(hopObj.boilTime, hopObj.OriginalWurt)
        return tempIBU

    @property 
    def SRM(self):
        #TODO return SRM calculated
        pass

    @property 
    def MashPh(self):
        #TODO return MashPh calculated
        pass
    
    def addHop(self, hop1):
        self.hops.append(hop1)
    
    def addFerm(self, ferm1):
        self.fermentables.append(ferm1)
            

class Fermentable:
    def __init__(self, ferType = '', kg = 0, lovibond = 0):
        self.ferType = ferType
        self.kg = float(kg)
        self.lovibond = float(lovibond)

class MashGuideline:
    def __init__(self, startThick = 0, temp = 0, time = 0, amount = 0):
        self.startThick = float(startThick)
        self.temp = float(temp)
        self.time = float(time)
        self.amount = float(amount)

class Hop:
    def __init__(self, hopType = '', boilTime = 0, amount = 0, leafWhole = 'pellet', temp = 0, AA = 0):
        self.AA = float(AA)
        self.hopType = hopType
        self.boilTime = float(boilTime)
        self.amount = float(amount)
        self.leafWhole = leafWhole
        self.temp = float(temp)

    #Tar in BoilTime och Original Gravity, returnar AA taget från ett table
    #Input för OgUt får inte vara över 1.13 eller under 1.03
    def GetAAUtil(self):
        AAValue = 0
        utilFile = open('UtilizationTable.txt', 'r')
        utilContent = utilFile.readlines()
        utilColumnsGravity = utilContent.pop(0).strip().split(' ')
        utilTable, utilRowsBoilTime = [], []
        rowIndex = 0, 0
        for row in utilContent:
            rowList = row.strip().split(' ')
            utilRowsBoilTime.append(rowList.pop(0))
            utilTable.append(rowList)
        if self.boilTime >= 120:
            rowIndex = 25
        else:
            rowIndex = Hop.getIndex(self.boilTime, utilRowsBoilTime)
        AAValue = utilTable[rowIndex][Hop.getIndex(self.originalWurt, utilColumnsGravity)]
        return AAValue

    #get index for row or column of AA table
    @staticmethod
    def getIndex(boilOrGravity, columnOrRowList):
        for i in range(1, len(columnOrRowList)):
            if boilOrGravity == float(columnOrRowList[i-1]):
                returnIndex = i-1
                break
            if boilOrGravity < float(columnOrRowList[i]) and boilOrGravity > float(columnOrRowList[i-1]):
                if boilOrGravity <= (float(columnOrRowList[i]) - ((float(columnOrRowList[i]) - float(columnOrRowList[i-1])) / 2)):
                    returnIndex = i - 1
                else:
                    returnIndex = i
        return returnIndex

    @property 
    def originalWurt(self):
        #TODO return originalWurt calculated
        pass
    
class Other:
    def __init__(self):
        #TODO decide if we want different "other" classes
        pass
class PrimingInfo:
    def __init__(self, method = '', amount = 0, temp = 0, co2Level = 0):
        self.method = method
        self.amount = float(amount)
        self.temp = float(temp)
        self.co2Level = float(co2Level)
#ska source och targetWater ha en egen klass med värden i?
class WaterChemistry:
    def __init__(self, sourceWater = None, targetWater = None, minerals = None):
        self.sourceWater = sourceWater
        self.targetWater = targetWater
        self.minerals = minerals
class Sourcewater:
    def __init__(self, ca2 = 0, mg2 = 0, na = 0, cl = 0,
                 so42 = 0, hco3 = 0):
        self.ca2 = float(ca2)
        self.mg2 = float(mg2)
        self.na = float(na)
        self.cl = float(cl)
        self.so42 = float(so42)
        self.hco3 = float(hco3)
class Targetwater(Sourcewater):
    def __init__(self, ca2 = 0, mg2 = 0, na = 0, cl = 0, so42 = 0, hco3 = 0):
	        super().__init__(ca2, mg2, na, cl, so42, hco3)


class Minerals:
    def __init__(self, calciumChloride = 0, chalk = 0, epsomSalt = 0, gypsum = 0, magnesiumChloride = 0,
                bakingSoda = 0, citricAcid = 0, lacticAcid = 0):
        self.calciumChloride = float(calciumChloride)
        self.chalk = float(chalk)
        self.epsomSalt = float(epsomSalt)
        self.gypsum = float(gypsum)
        self.magnesiumChloride = float(magnesiumChloride)
        self.bakingSoda = float(bakingSoda)
        self.citricAcid = float(citricAcid)
        self.lacticAcid = float(lacticAcid)
class Yeast:
    def __init__(self, yeastType = '', amount = 0, customAttenuation = 0):
        self.yeastType = yeastType
        self.amount = float(amount)
        self.customAttenuation = float(customAttenuation)

