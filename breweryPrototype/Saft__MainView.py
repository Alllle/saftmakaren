from PyQt5 import QtWidgets
import RecipeModels as rm
import RecipeFactory as rf
import Saftmakaren, pprint, re


currentUser = rf.RecepieFactory.createUser()
class SaftApp(Saftmakaren.Ui_MainWindow, QtWidgets.QMainWindow):
    #det som körs i början när man startar programmet
    def __init__(self):
        super(SaftApp, self).__init__()
        self.setupUi(self)
        self.showMaximized()#öppnar i fullscreen
        self.setWindowTitle("Saftmakaren") #på window står det stringen
        self.PopulateRecipeTree()
        #self.RecipesTree.itemSelectionChanged.connect(self.EditSelectedRecipe)
        self.save_Recipe_PB.clicked.connect(self.SaveRecipeChanges)
        self.scrapChanges_PB.clicked.connect(self.EditSelectedRecipe)
        self.editRecipe_PB.clicked.connect(self.EditSelectedRecipe)
        self.removeRecipe_PB.clicked.connect(self.RemoveRecipe)
        self.newRecipe_PB.clicked.connect(self.CreateNewRecipe)
        self.ferAdd_PB.clicked.connect(self.AddFermentation) #TODO
        self.hopAdd_PB.clicked.connect(self.AddHop) #TODO
        self.ferRemove_PB.clicked.connect(self.RemoveFermentation) #TODO
        self.hopRemove_PB.clicked.connect(self.RemoveHop) #TODO

        #tror det är en omväg atm...
    def getSelectedIndex(self):
        selectedItem = self.RecipesTree.currentItem()
        selectedIndex = self.RecipesTree.indexOfTopLevelItem(selectedItem)
        return selectedIndex
    def SaveRecipeChanges(self):
        leIndex = self.getSelectedIndex()
        if leIndex >= 0:
            currentUser.recipes[leIndex].title = self.recipeName_LE.text()
            currentUser.recipes[leIndex].batchSize = self.batchSize_LE.text()
            currentUser.recipes[leIndex].description = self.description_LE.text()
            currentUser.recipes[leIndex].boilTime = self.boilTime_LE.text()
            currentUser.recipes[leIndex].efficiency = self.efficiency_LE.text()
            currentUser.recipes[leIndex].mashGuide.startThick = self.startThickness_LE.text()
            currentUser.recipes[leIndex].mashGuide.time = self.mashTime_LE.text()
            currentUser.recipes[leIndex].mashGuide.temp = self.mashTemp_LE.text()
            currentUser.recipes[leIndex].mashGuide.amount = self.mashAmount_LE.text()
            currentUser.recipes[leIndex].primeInfo.method = self.method_LE.text()
            currentUser.recipes[leIndex].primeInfo.temp = self.primeTemp_Le.text()
            currentUser.recipes[leIndex].primeInfo.co2Level = self.co2Level_LE.text()
            currentUser.recipes[leIndex].primeInfo.amount = self.primeAmount_LE.text()
            currentUser.recipes[leIndex].waterChem.sourceWater.ca2 = self.sourceCa2_LE.text()
            currentUser.recipes[leIndex].waterChem.sourceWater.mg2 = self.sourceMg2_LE.text()
            currentUser.recipes[leIndex].waterChem.sourceWater.na = self.sourceNa_LE.text()
            currentUser.recipes[leIndex].waterChem.sourceWater.cl = self.sourceCl_LE.text()
            currentUser.recipes[leIndex].waterChem.sourceWater.so42 = self.sourceSo42_LE.text()
            currentUser.recipes[leIndex].waterChem.sourceWater.hco3 = self.sourceHco3_LE.text()
            currentUser.recipes[leIndex].waterChem.targetWater.ca2 = self.modifiedCa2_LE.text()
            currentUser.recipes[leIndex].waterChem.targetWater.mg2 = self.modifiedMg2_LE.text()
            currentUser.recipes[leIndex].waterChem.targetWater.na = self.modifiedNa_LE.text()
            currentUser.recipes[leIndex].waterChem.targetWater.cl = self.modifiedCl_LE.text()
            currentUser.recipes[leIndex].waterChem.targetWater.so42 = self.modifiedSo42_LE.text()
            currentUser.recipes[leIndex].waterChem.targetWater.hco3 = self.modifiedHco3_LE.text()
            #TODO:
            #currentUser.recipes[leIndex].hops = self.getHopListWidget()

            currentUser.recipes[leIndex].fermentables = self.getFerListWidget()


            #rf.RecepieFactory.SaveUser(currentUser)
            print(type(currentUser)) #returnar RecipeModels.User om SaveUser inte är outcommented
            print(type(currentUser.recipes[0])) #returnar dict om SaveUser inte är outcommented
            pprint.pprint(currentUser.recipes[0])
            pprint.pprint(currentUser)
            self.PopulateRecipeTree()##här failar den, kmr inte längre efter man sparat usern.
        else:
            QtWidgets.QMessageBox.about(self, 'Couldn\'t save recipe', 'Select a recipe to save!')
            return
    #returns a list of hop objects taken from input list TODO
    def getHopListWidget(self):
        hopList = []
        for index in range(self.hopListWidget.count()): #returnar antal listor/rows i listan av hops
            hopRow = self.hopListWidget.item(index).text().split(' ')
            number = re.compile(r'\d*\.\d*')
            hopRow[0] = number.search(hopRow[0]).group()
            hopRow[2] = number.search(hopRow[2]).group()
            hopRow[3] = number.search(hopRow[3]).group()
            #hopList.append(hop(hopType = '', boilTime = 0, amount = 0, leafWhole = 'pellet', temp = 0, AA = 0)), vad ska vi ha med? ändra ui eller model?
        return hopList

    #returns a list of fermentation objects taken from input list
    def getFerListWidget(self):
        ferList = []
        for index in range(self.ferListWidget.count()):#returnar antal listor/rows i listan av hops
            ferRow = self.ferListWidget.item(index).text().split(' ')
            number = re.compile(r'\d*\.\d*')
            ferRow[0] = number.search(ferRow[0]).group()
            ferRow[2] = number.search(ferRow[2]).group()
            ferList.append(rm.Fermentable(ferRow[1], ferRow[0], ferRow[2]))
        return ferList

    # populates the recipe-tree-list
    def PopulateRecipeTree(self):
        self.RecipesTree.setHeaderLabels(['#', 'NAME'])
        print('bugdetect1')
        self.RecipesTree.clear() #gör trädet tomt igen ##här failar den, kmr itne längre efte rman klickar på save, oavsett om man ändrar på något eller ej (men selecta ett recept först)
        print('bugdetect2')
        for recipe in currentUser.recipes:
            item = QtWidgets.QTreeWidgetItem(self.RecipesTree)
            item.setText(0, str(recipe.recipeID))
            item.setText(1, str(recipe.title))
        print('sucessfully fills the tree')
    
    def EditSelectedRecipe(self):
        selected = self.getSelectedIndex()
        print('selected index is: ' + str(self.getSelectedIndex()))
        if selected >= 0:
            self.PopulateRecipeData(currentUser.recipes[selected])
        else:
            QtWidgets.QMessageBox.about(self, 'Couldn\'t edit recipe', 'Select a recipe to edit!')
            return
    
     #när ett specifikt recept selectas, eller när man gör ett nytt så ska man ladda in receptdatan i alla lineedits etc. när man klickar på save knappen så fuckar det atm.
    def PopulateRecipeData(self, currentRecipe):
        self.recipeName_LE.setText(str(currentRecipe.title))
        self.batchSize_LE.setText(str(currentRecipe.batchSize))
        self.description_LE.setText(str(currentRecipe.description))
        self.boilTime_LE.setText(str(currentRecipe.boilTime))
        self.efficiency_LE.setText(str(currentRecipe.efficiency))
        self.startThickness_LE.setText(str(currentRecipe.mashGuide.startThick))
        self.mashTime_LE.setText(str(currentRecipe.mashGuide.time))
        self.mashTemp_LE.setText(str(currentRecipe.mashGuide.temp))
        self.mashAmount_LE.setText(str(currentRecipe.mashGuide.amount))
        self.method_LE.setText(str(currentRecipe.primeInfo.method))
        self.primeTemp_Le.setText(str(currentRecipe.primeInfo.temp))
        self.co2Level_LE.setText(str(currentRecipe.primeInfo.co2Level))
        self.primeAmount_LE.setText(str(currentRecipe.primeInfo.amount))
        self.sourceCa2_LE.setText(str(currentRecipe.waterChem.sourceWater.ca2))
        self.sourceMg2_LE.setText(str(currentRecipe.waterChem.sourceWater.mg2))
        self.sourceNa_LE.setText(str(currentRecipe.waterChem.sourceWater.na))
        self.sourceCl_LE.setText(str(currentRecipe.waterChem.sourceWater.cl))
        self.sourceSo42_LE.setText(str(currentRecipe.waterChem.sourceWater.so42))
        self.sourceHco3_LE.setText(str(currentRecipe.waterChem.sourceWater.hco3))
        self.modifiedCa2_LE.setText(str(currentRecipe.waterChem.targetWater.ca2))
        self.modifiedMg2_LE.setText(str(currentRecipe.waterChem.targetWater.mg2))
        self.modifiedNa_LE.setText(str(currentRecipe.waterChem.targetWater.na))
        self.modifiedCl_LE.setText(str(currentRecipe.waterChem.targetWater.cl))
        self.modifiedSo42_LE.setText(str(currentRecipe.waterChem.targetWater.so42))
        self.modifiedHco3_LE.setText(str(currentRecipe.waterChem.targetWater.hco3))
        #TODO fixa dessa i RecipeModels först.
        #self.og_LB.setText('Orginal Gravity: {}'.format(str(currentRecipe.og)))
        #self.fg_LB.setText('Final Gravity: {}'.format(str(currentRecipe.fg)))
        #self.abv_LB.setText('ABV: {}'.format(str(currentRecipe.ABV)))
        #self.ibu_LB.setText('IBU: {}'.format(str(currentRecipe.IBU)))
        #self.srm_LB.setText('SRM: {}'.format(str(currentRecipe.SRM)))
        #self.mashPh_LB.setText('Mash Ph: {}'.format(str(currentRecipe.MashPh)))
        self.PopulateHopsList(currentRecipe.hops)
        self.PopulateFermentationList(currentRecipe.fermentables)
        self.PopulateMineralsList(currentRecipe)
    #populates även om mineralen har värdet noll, ta bort, ha kvar?
    def PopulateMineralsList(self, aRecipe):
        x = aRecipe.waterChem.minerals
        self.mineralsListWidget.clear()
        item = ['{}unit Calcium Chloride'.format(x.calciumChloride), '{}unit Chalk'.format(x.chalk), '{}unit Epsom Salt'.format(x.epsomSalt), 
                '{}unit Gypsum'.format(x.gypsum), '{}unit Magnesium Chloride'.format(x.magnesiumChloride), '{}unit Baking Soda'.format(x.bakingSoda),
                '{}unit Citric Acid'.format(x.citricAcid), '{}unit Lactic Acid'.format(x.lacticAcid)]
        self.mineralsListWidget.addItems(item)


    def PopulateHopsList(self, hops):
        self.hopListWidget.clear()
        item = ['{}kg {} {}min {}AA'.format(str(hop.amount),str(hop.hopType),str(hop.boilTime),str(hop.AA)) for hop in hops]
        self.hopListWidget.addItems(item)
    #TODO hitta hur man kan se hur många rows som är fyllda, och hur man kan fylla i endast en row som man väljer.
    def AddHop(self):
        if self.getSelectedIndex() >= 0:
            hopAmount = self.hopAmount_LE.text()
            if hopAmount == '':
                hopAmount = 0.0
            elif type(hopAmount) != float or type(hopAmount) != int: #om man har input int eller float funkar det inte....fixa
                QtWidgets.QMessageBox.about(self, 'Invalid input', 'Amount has to be a number')
                return
            hopName = self.hopName_LE.text()
            if hopName == '':
                hopName = 'default'
            hopTime = self.hopTime_LE.text()
            if hopTime == '':
                hopTime = 0.0
            elif type(hopTime) != float or type(hopTime) != int:
                QtWidgets.QMessageBox.about(self, 'Invalid input', 'Boiltime has to be a number')
                return
            hopAA = self.AA_LE.text()
            if hopAA == '':
                hopAA = 0.0
            elif type(hopAA) != float or type(hopAA) != int:
                QtWidgets.QMessageBox.about(self, 'Invalid input', 'AA has to be a number')
                return
            itemToAdd = '{}kg {} {}min {}AA'.format(str(float(hopAmount)), hopName,str(hopTime),str(hopAA))
            self.hopListWidget.addItem(itemToAdd)
        else:
            QtWidgets.QMessageBox.about(self, 'Couldn\'t add hop', 'Select a recipe first')

    def RemoveHop(self):
        self.hopListWidget.takeItem(self.hopListWidget.currentIndex().row()) #enklaste sättet att ta bort ett item från en rad (take item returnar item som man tar bort)

    def PopulateFermentationList(self, fermentations):
        self.ferListWidget.clear()
        item = ['{}kg {} {}L'.format(str(fermentation.kg),str(fermentation.ferType),str(fermentation.lovibond)) for fermentation in fermentations]
        self.ferListWidget.addItems(item)
    #TODO
    def AddFermentation(self):
        if self.getSelectedIndex() >= 0:
            ferAmount = self.ferAmount_LE.text()
            if ferAmount == '':
                ferAmount = 0.0
            elif type(ferAmount) != float or type(ferAmount) != int: #om man har input int eller float funkar det inte....fixa
                QtWidgets.QMessageBox.about(self, 'Invalid input', 'Amount has to be a number')
                return
            ferName = self.ferName_LE.text()
            if ferName == '':
                ferName = 'default'
            lovibond = self.lovibond_LE.text()
            if lovibond == '':
                lovibond = 0.0
            elif type(lovibond) != float or type(lovibond) != int:
                QtWidgets.QMessageBox.about(self, 'Invalid input', 'Lovibond has to be a number')
                return
            itemToAdd = '{}kg {} {}AA'.format(str(ferAmount),ferName,str(lovibond))
            self.ferListWidget.addItem(itemToAdd)
        else:
            QtWidgets.QMessageBox.about(self, 'Couldn\'t add fermentation', 'Select a recipe first')

    def RemoveFermentation(self):
        self.ferListWidget.takeItem(self.ferListWidget.currentIndex().row())
    
    def CreateNewRecipe(self):
        defaultRecipe = rf.RecepieFactory.createEmptyRecipe()
        currentUser.addRecipe(defaultRecipe)
        #self.RecipesTree.setSelected()
        #self.PopulateRecipeData(currentRecipe) #skulle kunna ha detta om man kan göra så den selectar rätt lista i recipelist också. annars så får man selecta manuelt
        #och först då populatea datan.
        #rf.RecepieFactory.SaveUser(currentUser)
        self.PopulateRecipeTree()

    def RemoveRecipe(self):
        selected = self.getSelectedIndex()
        if selected >= 0:
            currentUser.removeRecipe(self.getSelectedIndex()+1)
            #rf.RecepieFactory.SaveUser(currentUser) #kan inte populera trädet efteråt, currentRecipe.title etc är dict.
            self.PopulateRecipeTree()
        else:
            QtWidgets.QMessageBox.about(self, 'Couldn\'t remove recipe', 'Select a recipe to remove!')
            return
        
       




