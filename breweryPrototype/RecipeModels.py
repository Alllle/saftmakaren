#!python3
#Classes related to recepie.

class User:
    def __init__(self, name = None, img = None, recepies = None):
        if name == None:
            self.name = 'insert name'
        else:
            self.name = name
        if img == None:
            self.img = ''
        else:
            self.img = img
        if recepies == None:
            self.recepies = []
        else:
            self.recepies = recepies


    def addRecepie(self, recepie1):
        self.recepies.append(recepie1)
        
        
class Recepie:
    def __init__(self, title, description = '', og = '', fg = '', yeast = '', primeInfo = '', waterChem = '', boilTime = '',
                 efficiency = '', batchSize = '', mashGuide = None, other = None, hops = None, fermentables = None):
        self.title = title
        self.description = description
        self.og = og
        self.fg = fg
        self.fermentables = fermentables
        self.yeast = yeast
        self.primeInfo = primeInfo
        self.hops = hops
        self.other = other
        self.waterChem = waterChem
        self.boilTime = boilTime
        self.efficiency = efficiency
        self.batchSize = batchSize
        if hops == None:
            self.hops = []
        else:
            self.hops = hops
        if fermentables == None:
            self.fermentables = []
        else:
            self.fermentables = fermentables
        if mashGuide == None:
            self.mashGuide = ''
        else:
            self.mashGuide = mashGuide
        if other == None:
            self.other = ''
        else:
            self.other = other
            
    @property 
    def ABV(self):
        return abs((self.fg - self.og) * 131.25)

    @property 
    def IBU(self):
        #TODO return IBU calculated
        pass

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
    def __init__(self, Type, kg, lovibond):
        self.Type = Type
        self.kg = kg
        self.lovibond = lovibond

class MashGuideline:
    def __init__(self, startThick, temp, time, amount):
        self.startThick = startThick
        self.temp = temp
        self.time = time
        self.amount = amount

class Hop:
    def __init__(self, Type, boilTime, amount, leafWhole, temp):
        self.Type = Type
        self.boilTime = boilTime
        self.amount = amount
        self.leafWhole = leafWhole
        self.temp = temp

class Other:
    def __init__(self):
    #TODO decide if we want different "other" classes
        pass

class PrimingInfo:
    def __init__(self, method, amount, temp, co2Level):
        self.method = method
        self.amount = amount
        self.temp = temp
        self.co2Level = co2Level

class WaterChemistry:
    def __init__(self, sourceWater, targetWater, ca2, mg2, na2, cl,
                 so42, hco3):
        self.sourceWater = sourceWater
        self.targetWater = targetWater
        self.ca2 = ca2
        self.mg2 = mg2
        self.na2 = na2
        self.cl = cl
        self.so42 = so42
        self.hco3 = hco3
class Yeast:
    def __init__(self):
        #TODO
        pass
