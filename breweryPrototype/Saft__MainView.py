from PyQt5 import QtWidgets
import RecipeModels as rm
import RecipeFactory as rf
import Saftmakaren, pprint


currentUser = rf.RecepieFactory.createUser()
class SaftApp(Saftmakaren.Ui_MainWindow, QtWidgets.QMainWindow):
    #det som körs i början när man startar programmet
    def __init__(self):
        super(SaftApp, self).__init__()
        self.setupUi(self)
        self.showMaximized()#öppnar i fullscreen
        self.setWindowTitle("Saftmakaren") #på window står det stringen
        self.PopulateRecipeTree()
        self.RecipesTree.itemSelectionChanged.connect(self.EditSelectedRecipe)
        self.save_Recipe_PB.clicked.connect(self.SaveRecipeChanges)
        
    def getSelectedIndex(self):
        selectedItem = self.RecipesTree.currentItem()
        selectedIndex = self.RecipesTree.indexOfTopLevelItem(selectedItem)
        return selectedIndex
    def SaveRecipeChanges(self):
        currentUser.recipes[self.getSelectedIndex()].title = self.recipeName_LE.text()
        currentUser.recipes[self.getSelectedIndex()].batchSize = self.batchSize_LE.text()
        currentUser.recipes[self.getSelectedIndex()].description = self.description_LE.text()
        currentUser.recipes[self.getSelectedIndex()].boilTime = self.boilTime_LE.text()
        currentUser.recipes[self.getSelectedIndex()].efficiency = self.efficiency_LE.text()
        currentUser.recipes[self.getSelectedIndex()].mashGuide.startThick = self.startThickness_LE.text()
        currentUser.recipes[self.getSelectedIndex()].mashGuide.time = self.mashTime_LE.text()
        currentUser.recipes[self.getSelectedIndex()].mashGuide.temp = self.mashTemp_LE.text()
        currentUser.recipes[self.getSelectedIndex()].mashGuide.amount = self.mashAmount_LE.text()
        currentUser.recipes[self.getSelectedIndex()].primeInfo.method = self.method_LE.text()
        currentUser.recipes[self.getSelectedIndex()].primeInfo.temp = self.primeTemp_Le.text()
        currentUser.recipes[self.getSelectedIndex()].primeInfo.co2Level = self.co2Level_LE.text()
        currentUser.recipes[self.getSelectedIndex()].primeInfo.amount = self.primeAmount_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.sourceWater.ca2 = self.sourceCa2_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.sourceWater.mg2 = self.sourceMg2_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.sourceWater.na = self.sourceNa_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.sourceWater.cl = self.sourceCl_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.sourceWater.so42 = self.sourceSo42_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.sourceWater.hco3 = self.sourceHco3_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.targetWater.ca2 = self.modifiedCa2_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.targetWater.mg2 = self.modifiedMg2_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.targetWater.na = self.modifiedNa_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.targetWater.cl = self.modifiedCl_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.targetWater.so42 = self.modifiedSo42_LE.text()
        currentUser.recipes[self.getSelectedIndex()].waterChem.targetWater.hco3 = self.modifiedHco3_LE.text()
        rf.RecepieFactory.SaveUser(currentUser)
        #self.PopulateRecipeTree()##här failar den, kmr inte längre.
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
        self.PopulateRecipeData(currentUser.recipes[self.getSelectedIndex()])
        print(self.getSelectedIndex())
        print(currentUser.recipes[self.getSelectedIndex()].title)
    
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
        self.PopulateHopsList(currentRecipe.hops)
        self.PopulateFermentationList(currentRecipe.fermentables)

    def PopulateHopsList(self, hops):
        self.hopListWidget.clear()
        item = ['{}kg {} {}min {}AA'.format(str(hop.amount),str(hop.hopType),str(hop.boilTime),str(hop.AA)) for hop in hops]
        self.hopListWidget.addItems(item)

    def PopulateFermentationList(self, fermentations):
        self.ferListWidget.clear()
        item = ['{}kg {}  {}L'.format(str(fermentation.kg),str(fermentation.ferType),str(fermentation.lovibond)) for fermentation in fermentations]
        self.ferListWidget.addItems(item)

    
    
    def CreateNewRecipe(self):
        defaultRecipe = rf.RecepieFactory.createEmptyRecipe()
        self.PopulateRecipeData(defaultRecipe)
        pass

    def RemoveRecipe(self):
        pass
       




