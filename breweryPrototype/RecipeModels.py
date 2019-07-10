#!python3
#Classes related to recipe.

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
        
        
class Recipe:
    def __init__(self, title = '', description = '', og = 0, fg = 0, yeast = None, primeInfo = None, waterChem = None, boilTime = 0,
                 efficiency = 0, batchSize = 0, mashGuide = None, other = None, hops = None, fermentables = None):
        self.title = title
        self.description = description
        self.og = og
        self.fg = fg
        self.yeast = yeast
        self.primeInfo = primeInfo
        self.waterChem = waterChem
        self.boilTime = boilTime
        self.efficiency = efficiency
        self.batchSize = batchSize
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
            
    @property 
    def ABV(self):
        return abs((self.fg - self.og) * 131.25)
    
    @property 
    def IBU(self):
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
        self.kg = kg
        self.lovibond = lovibond

class MashGuideline:
    def __init__(self, startThick = 0, temp = 0, time = 0, amount = 0):
        self.startThick = startThick
        self.temp = temp
        self.time = time
        self.amount = amount

class Hop:
    def __init__(self, hopType = '', boilTime = 0, amount = 0, leafWhole = 'pellet', temp = 0, AA = 0):
        self.AA = AA
        self.hopType = hopType
        self.boilTime = boilTime
        self.amount = amount
        self.leafWhole = leafWhole
        self.temp = temp

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
        self.amount = amount
        self.temp = temp
        self.co2Level = co2Level
#ska source och targetWater ha en egen klass med värden i?
class WaterChemistry:
    def __init__(self, sourceWater = None, targetWater = None, ca2 = 0, mg2 = 0, na2 = 0, cl = 0,
                 so42 = 0, hco3 = 0):
        self.sourceWater = sourceWater
        self.targetWater = targetWater
        self.ca2 = ca2
        self.mg2 = mg2
        self.na2 = na2
        self.cl = cl
        self.so42 = so42
        self.hco3 = hco3
class Yeast:
    def __init__(self, yeastType = '', amount = 0, customAttenuation = 0):
        self.yeastType = yeastType
        self.amount = amount
        self.customAttenuation = customAttenuation

