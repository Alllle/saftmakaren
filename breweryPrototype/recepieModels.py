#!python3
#Classes related to recepie.

class User:
    def __init__(self, name = None, recepies = None, img = None):
        if name == None:
            self.name = 'insert name'
        else:
            self.name = name
        if recepies == None:
            self.recepies = []
        else:
            self.recepies = recepies
        if img == None:
            self.img = ''
        else:
            self.img = img

    def addRecepie(self, title, description, og, fg, fermentables,
                   mashGuide, yeast, primeInfo, hops, other,
                   waterChem, boilTime, efficiency, batchSize):
        
        recepie = Recepie(title, description, og, fg, fermentables,
                   mashGuide, yeast, primeInfo, hops, other,
                   waterChem, boilTime, efficiency, batchSize)
        self.recepies.append(recepie)
        
        
class Recepie:
    def __init__(self, title, description, og, fg, fermentables, mashGuide = None,
                 yeast, primeInfo, hops, other, waterChem, boilTime,
                 efficiency, batchSize):
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
        
        if mashGuide == None:
            self.mashGuide = ''
        else:
            self.mashGuide = mashGuide
            
       @property 
        def ABV(self):
            return abs((self.fg - self.og) * 131.25)

        @property 
        def IBU(self):
            #TODO return IBU calculated

        @property 
        def SRM(self):
            #TODO return SRM calculated

        @property 
        def MashPh(self):
            #TODO return MashPh calculated
            

class Fermentable:
    def __init__(self, Type, kg, lovibond)
        self.Type = Type
        self.kg = kg
        self.lovibond

class MashGuideline
    def __init__(self, startThick, temp, time, amount)
        self.startThick = startThick
        self.temp = temp
        self.time = time
        self.amount = amount

class Hop:
    def __init__(self, Type, boilTime, amount, leafWhole, temp)
        self.Type = Type
        self.boilTime = boilTime
        self.amount = amount
        self.leafWhole = leafWhole
        self.temp = temp

class Other:
    def __init__
    #TODO

class PrimingInfo:
    def __init__(self, method, amount, temp, co2Level)
        self.method = method
        self.amount = amount
        self.temp = temp
        self.co2Level = co2Level

class WaterChemistry
    def __init__(self, sourceWater, targetWater, ca+2, mg+2, na+2, cl-,
                 so4-2, hco3-)
        self.sourceWater = sourceWater
        self.targetWater = targetWater
        self.ca+2 = ca+2
        self.mg+2 = mg+2
        self.na+2 = na+2
        self.cl- = cl-
        self.so4-2 = s04-2
        self.hco3- = hco3-
